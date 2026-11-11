import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FIGURE_DIR = BASE_DIR / "figures"

FIGURE_DIR.mkdir(exist_ok=True)

summary = pd.read_csv(
    DATA_DIR / "sample_expression_summary.csv"
)

plt.figure(figsize=(10, 6))

plt.hist(
    summary["Mean"],
    bins=20,
    edgecolor="black"
)

plt.xlabel("Mean expression value")
plt.ylabel("Number of samples")
plt.title("Distribution of Mean Expression Across 140 Samples")

plt.tight_layout()

output = FIGURE_DIR / "sample_mean_distribution.png"
plt.savefig(output, dpi=300)
plt.show()

print("Plot saved to:", output)