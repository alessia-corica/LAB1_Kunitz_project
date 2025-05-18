import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fold1_updated = pd.DataFrame(
    [[286417, 0],  # TN, FP
     [0, 180]],   # FN, TP
    index=["Actual Negative", "Actual Positive"],
    columns=["Predicted Negative", "Predicted Positive"]
)

fold2_updated = pd.DataFrame(
    [[286415, 2],  # TN, FP
     [1, 182]],   # FN, TP
    index=["Actual Negative", "Actual Positive"],
    columns=["Predicted Negative", "Predicted Positive"]
)

plt.figure(figsize=(6, 5))
sns.heatmap(fold1_updated, annot=True, fmt='d', cmap='Blues', linewidths=0.5, linecolor='gray', cbar=True)
plt.title("Confusion Matrix – Fold 1 (Set 1, Threshold = 1e-9)", fontsize=13)
plt.xlabel("Predicted Class", fontsize=11)
plt.ylabel("Actual Class", fontsize=11)
plt.tight_layout()
plt.savefig("confusion_matrix_fold1.png")
plt.close()

plt.figure(figsize=(6, 5))
sns.heatmap(fold2_updated, annot=True, fmt='d', cmap='Oranges', linewidths=0.5, linecolor='gray', cbar=True)
plt.title("Confusion Matrix – Fold 2 (Set 2, Threshold = 1e-9)", fontsize=13)
plt.xlabel("Predicted Class", fontsize=11)
plt.ylabel("Actual Class", fontsize=11)
plt.tight_layout()
plt.savefig("confusion_matrix_fold2.png")
plt.close()

print("Confusion matrices saved: Set 1 = Blue, Set 2 = Orange")
