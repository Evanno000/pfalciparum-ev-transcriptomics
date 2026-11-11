import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Load gene-level results
df = pd.read_csv(
    DATA_DIR / "gene_level_ev_wp_summary.csv"
)

# Calculate absolute expression differences
df["Absolute_Difference"] = df["EV_minus_WP"].abs()

# Select top 20 genes
top20 = df.nlargest(20, "Absolute_Difference")

# Save gene IDs and expression results
output = DATA_DIR / "top20_gene_list.csv"

top20[[
    "GeneID",
    "EV_mean",
    "WP_mean",
    "EV_minus_WP"
]].to_csv(output, index=False)

print("TOP 20 GENES EXTRACTED")
print("---------------------")
print(top20[["GeneID", "EV_mean", "WP_mean"]].to_string(index=False))

print("\nSaved:", output)
