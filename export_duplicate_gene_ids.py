import pandas as pd

df = pd.read_excel(
    "data/GSE241277_Fourier_transformed_nTPM.xlsx"
)

hashes = pd.util.hash_pandas_object(
    df.drop(columns=["GeneID"]),
    index=False
)

groups = {}

for gene, profile_hash in zip(df["GeneID"], hashes):
    groups.setdefault(profile_hash, []).append(gene)

duplicate_groups = [
    group for group in groups.values()
    if len(group) > 1
]

gene_ids = [
    gene
    for group in duplicate_groups
    for gene in group
]

output = pd.DataFrame({"Gene ID": gene_ids})

output.to_csv(
    "data/duplicate_gene_ids.csv",
    index=False
)

print("Duplicate genes exported:", len(gene_ids))
print("Saved to data/duplicate_gene_ids.csv")