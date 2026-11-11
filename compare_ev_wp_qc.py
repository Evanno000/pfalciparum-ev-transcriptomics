import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FIGURE_DIR = BASE_DIR / "figures"

FIGURE_DIR.mkdir(exist_ok=True)

# Load sample-level expression statistics
summary = pd.read_csv(
    DATA_DIR / "sample_expression_summary.csv"
)

# Load sample information
metadata = pd.read_csv(
    DATA_DIR / "sample_mapping.csv"
)

# Connect expression statistics to sample conditions
combined = summary.merge(
    metadata[["Expression_Column", "Treatment_Type"]],
    left_on="Sample",
    right_on="Expression_Column",
    how="inner"
)

# Check sample matching
print("EV AND WP SAMPLE QC")
print("-------------------")
print("Matched samples:", len(combined))
print("\nSamples per condition:")
print(combined["Treatment_Type"].value_counts())

# Summarise variability
print("\nStandard deviation by condition:")
print(
    combined.groupby("Treatment_Type")["Standard_Deviation"]
    .agg(["mean", "median", "min", "max"])
    .round(3)
)

# Plot variability
plt.figure(figsize=(8, 6))

combined.boxplot(
    column="Standard_Deviation",
    by="Treatment_Type"
)

plt.title("Expression Variability: EV vs WP")
plt.suptitle("")
plt.xlabel("Sample condition")
plt.ylabel("Standard deviation of expression")

plt.tight_layout()

output = FIGURE_DIR / "ev_wp_variability.png"
plt.savefig(output, dpi=300)
plt.show()

print("\nPlot saved to:", output)