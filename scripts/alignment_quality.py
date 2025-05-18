import matplotlib.pyplot as plt

# PDB IDS
pdb_ids = [
    "5NX1:C", "6BX8:B", "4BQD:A", "1YC0:I", "4DTG:K", "1F5R:I", "1ZR0:B", "3WNY:A", "1BUN:B",
    "3M7Q:B", "6Q61:A", "4NTW:B", "5YV7:A", "1DTX:A", "3BYB:A", "4U30:X", "6YHY:A", "1KNT:A",
    "5JB7:A", "5M4V:A", "1YLD:B", "1FAK:I", "4U32:X", "5JBT:Y"
]
nres = [
    54, 55, 78, 66, 60, 57, 63, 56, 61, 61, 59, 60, 60, 59, 58, 54, 59, 55, 56, 57, 56, 55, 54, 38
]
rmsd = [
    0.4107, 0.4000, 0.3730, 0.3357, 0.4430, 0.6203, 0.4310, 0.6027, 0.7111, 0.5230, 0.4646, 0.7731,
    0.5173, 0.5102, 0.4520, 0.5816, 0.4311, 0.5897, 0.5488, 0.4397, 0.5875, 0.4866, 0.3114, 2.9166
]

# Scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(pdb_ids, rmsd, color='steelblue')
plt.xticks(rotation=90)
plt.axhline(1.0, color='gray', linestyle='--', label="Reference threshold")
plt.scatter("5JBT:Y", 2.9166, color='red', label="Excluded entry")

# Final layout
plt.title("Structural Alignment Quality (RMSD per PDB entry)")
plt.xlabel("PDB Entry")
plt.ylabel("RMSD (Å)")
plt.tight_layout()
plt.legend()
plt.grid(True)

# Save output
plt.savefig("alignment_quality.png")
print("Saved as: alignment_quality.png")
