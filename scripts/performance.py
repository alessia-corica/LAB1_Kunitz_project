#!/usr/bin/python3

import sys
import math

# =========================
# Utility Functions
# =========================

def get_cm(filename, threshold=1e-3, pe=2, pr=1):
    # Computes the 2x2 confusion matrix using a given e-value threshold
    cm = [[0, 0], [0, 0]]
    with open(filename) as f:
        for line in f:
            values = line.strip().split()              # Split line into columns
            evalue = float(values[pe])                 # Get e-value (default column 2)
            true_label = int(values[pr])               # Get true class label (default column 1)
            pred_label = 1 if evalue <= threshold else 0  # Predict 1 if below threshold, else 0
            cm[pred_label][true_label] += 1            # Update the confusion matrix
    return cm

def get_q2(cm):
    # Q2 = Accuracy = (TP + TN) / Total
    total = sum([sum(row) for row in cm])
    if total > 0:
        return (cm[0][0] + cm[1][1]) / total
    else:
        return 0.0

def get_mcc(cm):
    # MCC = Matthews Correlation Coefficient
    tp = cm[1][1]
    tn = cm[0][0]
    fp = cm[1][0]
    fn = cm[0][1]
    denom = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    if denom != 0:
        return (tp * tn - fp * fn) / denom
    else:
        return 0.0

def get_tpr(cm):
    # TPR = True Positive Rate = TP / (TP + FN)
    tp = cm[1][1]
    fn = cm[0][1]
    if (tp + fn) > 0:
        return tp / (tp + fn)
    else:
        return 0.0

def get_ppv(cm):
    # PPV = Precision = TP / (TP + FP)
    tp = cm[1][1]
    fp = cm[1][0]
    if (tp + fp) > 0:
        return tp / (tp + fp)
    else:
        return 0.0

# =========================
# Main Script
# =========================

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 performance.py <input.class> <threshold>")
        sys.exit(1)

    filename = sys.argv[1]                      # Path to input file (.class format)
    threshold = float(sys.argv[2])              # E-value threshold for classification

    cm = get_cm(filename, threshold, pe=2, pr=1)  # Compute confusion matrix using full-sequence e-value

    # Print results
    print("")
    print("Confusion Matrix:")
    print("TN =", cm[0][0], "FN =", cm[0][1])   # True Negatives and False Negatives
    print("FP =", cm[1][0], "TP =", cm[1][1])   # False Positives and True Positives
    print("Threshold:", threshold)
    print("Q2 (Accuracy):", round(get_q2(cm), 4))
    print("MCC:", round(get_mcc(cm), 4))
    print("TPR (Recall):", round(get_tpr(cm), 4))
    print("PPV (Precision):", round(get_ppv(cm), 4))

