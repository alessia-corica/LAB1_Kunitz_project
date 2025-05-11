import matplotlib.pyplot as plt

# Thresholds and corresponding MCC values extracted from both performance files
thresholds = [1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-1, 1e-2, 1e-3, 1e-4]
mcc_set1 = [1.0, 1.0, 1.0, 0.9945, 0.9918, 0.9918, 0.9862, 0.9862, 0.9862, 0.9862]
mcc_set2 = [1.0, 1.0, 1.0, 0.9945, 0.9918, 0.9918, 0.9862, 0.9862, 0.9862, 0.9862]

plt.figure(figsize=(8, 5))
plt.plot(thresholds, mcc_set1, marker='o', label='Set 1')
plt.plot(thresholds, mcc_set2, marker='s', label='Set 2')
plt.xscale('log')
plt.ylim(0.98, 1.01)
plt.xlabel('E-value Threshold (log scale)')
plt.ylabel('MCC')
plt.title('MCC vs E-value Threshold')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('/mnt/data/mcc_vs_threshold.png')
plt.show()
