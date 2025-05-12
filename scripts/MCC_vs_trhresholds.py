import matplotlib.pyplot as plt

# Thresholds usati nei file
thresholds = ["1e-10", "1e-09", "1e-08", "1e-07", "1e-06", "1e-05", "0.1", "0.01", "0.001", "0.0001"]

# MCC dal nuovo file set1
mcc_set1 = [1.0, 1.0, 1.0, 0.9945, 0.9918, 0.9918, 0.9862, 0.9862, 0.9862, 0.9862]

# MCC dal nuovo file set2
mcc_set2 = [1.0, 1.0, 0.9973, 0.9973, 0.9973, 0.9973, 0.9973, 0.9973, 0.9973, 0.9945]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(thresholds, mcc_set1, marker='o', label='Set 1')
plt.plot(thresholds, mcc_set2, marker='s', label='Set 2')
plt.xlabel('Threshold')
plt.ylabel('MCC')
plt.title('MCC vs Threshold for Set 1 and Set 2')
plt.ylim(0.98, 1.01)
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
