import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend (no GUI)

import matplotlib.pyplot as plt

# Thresholds ordered from most to least stringent
thresholds = ['1e-10', '1e-9', '1e-8', '1e-7', '1e-6', '1e-5', '0.0001', '0.001', '0.01', '0.1']

# MCC values
mcc_set1 = [1.0, 1.0, 1.0, 0.9945, 0.9918, 0.9918, 0.9862, 0.9862, 0.9862, 0.9862]

mcc_set2 = [0.9891, 0.9918, 0.9918, 0.9918, 0.9918, 0.9918, 0.9891, 0.976, 0.9589, 0.9038]

# Compute average MCC
mean_mcc = [(x + y) / 2 for x, y in zip(mcc_set1, mcc_set2)]

# Find index of best mean MCC
best_index_mean = mean_mcc.index(max(mean_mcc))
best_threshold_mean = thresholds[best_index_mean]
best_mcc_mean = mean_mcc[best_index_mean]

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(thresholds, mcc_set1, marker='o', label='Set 1', color='blue')
plt.plot(thresholds, mcc_set2, marker='s', label='Set 2', color='orange')

# Add only the mean-best point in red
plt.scatter(best_threshold_mean, best_mcc_mean, color='red', zorder=5)
plt.text(best_threshold_mean, best_mcc_mean + 0.001, f'Best: {best_threshold_mean}', color='red', ha='center')

# Final layout
plt.xlabel('E-value Threshold')
plt.ylabel('MCC (Matthews Correlation Coefficient)')
plt.title('MCC vs Threshold – Mean Best Point Only')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save output
plt.savefig("mcc_thresholds_.png")
print("Saved as: mcc_thresholds_.png")