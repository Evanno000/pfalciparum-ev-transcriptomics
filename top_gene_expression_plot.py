import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FIGURE_DIR = BASE_DIR / "figures"

FIGURE_DIR.mkdir(exist_ok=True)

# Load gene-level results
df = pd.read_csv(
    DATA_DIR / "gene_level_ev_wp_summary.csv"
)

# Select the 20 genes with the largest absolute differences
df["Absolute_Difference"] = df["EV_minus_WP"].abs()

top20 = df.nlargest(20, "Absolute_Difference")

# Prepare plot
plt.figure(figsize=(12, 8))

x = range(len(top20))
width = 0.4

plt.bar(
    [i - width/2 for i in x],
    top20["EV_mean"],
    width,
    label="EV"
)

plt.bar(
    [i + width/2 for i in x],
    top20["WP_mean"],
    width,
    label="WP"
)

plt.xticks(
    list(x),
    top20["GeneID"],
    rotation=60,
    ha="right"
)

plt.xlabel("Plasmodium falciparum genes")
plt.ylabel("Mean expression value")
plt.title("Top 20 Genes: EV vs WP Expression")
plt.legend()

plt.tight_layout()

# Save figure
output = FIGURE_DIR / "top20_gene_expression.png"

plt.savefig(output, dpi=300)
plt.show()

print("TOP 20 GENE EXPRESSION PLOT")
print("--------------------------")
print("Genes displayed:", len(top20))
print("Figure saved to:", output)