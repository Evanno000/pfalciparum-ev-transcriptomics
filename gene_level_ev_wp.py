import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Load expression matrix
df = pd.read_excel(
    DATA_DIR / "GSE241277_Fourier_transformed_nTPM.xlsx"
)

# Load sample mapping
metadata = pd.read_csv(
    DATA_DIR / "sample_mapping.csv"
)

# Identify EV and WP expression columns
ev_samples = metadata.loc[
    metadata["Treatment_Type"] == "EV",
    "Expression_Column"
].tolist()

wp_samples = metadata.loc[
    metadata["Treatment_Type"] == "WP",
    "Expression_Column"
].tolist()

# Calculate average expression for each gene
df["EV_mean"] = df[ev_samples].mean(axis=1)
df["WP_mean"] = df[wp_samples].mean(axis=1)

# Calculate descriptive difference
df["EV_minus_WP"] = df["EV_mean"] - df["WP_mean"]

# Save complete gene-level results
output = DATA_DIR / "gene_level_ev_wp_summary.csv"

df[[
    "GeneID",
    "EV_mean",
    "WP_mean",
    "EV_minus_WP"
]].to_csv(output, index=False)

# Display genes with largest absolute differences
top_genes = df.reindex(
    df["EV_minus_WP"].abs().sort_values(
        ascending=False
    ).index
).head(10)

print("GENE-LEVEL EV VS WP ANALYSIS")
print("----------------------------")
print("Total genes analysed:", len(df))
print("EV samples:", len(ev_samples))
print("WP samples:", len(wp_samples))

print("\nTop 10 genes by absolute difference:")
print(
    top_genes[[
        "GeneID",
        "EV_mean",
        "WP_mean",
        "EV_minus_WP"
    ]].round(3).to_string(index=False)
)

print("\nSaved:", output)