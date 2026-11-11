import pandas as pd

# Load expression data
df = pd.read_excel(
    "data/GSE241277_Fourier_transformed_nTPM.xlsx"
)

# Separate gene IDs from expression values
expression = df.drop(columns=["GeneID"])

# Generate a hash for each expression profile
profile_hashes = pd.util.hash_pandas_object(
    expression,
    index=False
)

# Group genes with matching profile hashes
groups = {}

for gene, profile_hash in zip(df["GeneID"], profile_hashes):
    groups.setdefault(profile_hash, []).append(gene)

# Keep groups containing multiple genes
duplicate_groups = [
    genes for genes in groups.values()
    if len(genes) > 1
]

print("DUPLICATE EXPRESSION PROFILE INVESTIGATION")
print("------------------------------------------")

print("Total genes:", len(df))
print("Genes in duplicate groups:",
      sum(len(group) for group in duplicate_groups))
print("Number of duplicate groups:", len(duplicate_groups))

for number, group in enumerate(duplicate_groups, start=1):
    print(f"\nGroup {number}:")
    print(group)

print("\nInvestigation completed.")