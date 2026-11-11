import pandas as pd

# Load expression dataset
df = pd.read_excel(
    "data/GSE241277_Fourier_transformed_nTPM.xlsx"
)

# Genes to investigate
genes = [
    "PF3D7_0222000",
    "PF3D7_0324000",
    "PF3D7_0601300"
]

# Extract their expression profiles
selected = df[df["GeneID"].isin(genes)].set_index("GeneID")

print("REPEATED GENE PROFILE INVESTIGATION")
print("-----------------------------------")

print("Genes found:", len(selected))
print("Samples analysed:", selected.shape[1])

# Compare expression profiles
for i in range(len(genes)):
    for j in range(i + 1, len(genes)):

        gene_a = genes[i]
        gene_b = genes[j]

        if gene_a in selected.index and gene_b in selected.index:

            profile_a = selected.loc[gene_a]
            profile_b = selected.loc[gene_b]

            identical = profile_a.equals(profile_b)

            print(f"\n{gene_a} vs {gene_b}")
            print("Identical profiles:", identical)
            print(
                "Maximum absolute difference:",
                abs(profile_a - profile_b).max()
            )

print("\nInvestigation completed.")