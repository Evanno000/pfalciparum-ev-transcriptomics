import pandas as pd

# Load expression dataset
expression = pd.read_excel(
    "data/GSE241277_Fourier_transformed_nTPM.xlsx"
)

# Identify identical expression profiles
hashes = pd.util.hash_pandas_object(
    expression.drop(columns=["GeneID"]),
    index=False
)

groups = {}

for gene, profile_hash in zip(expression["GeneID"], hashes):
    groups.setdefault(profile_hash, []).append(gene)

duplicate_groups = [
    group for group in groups.values()
    if len(group) > 1
]

# Load gene annotations
annotations = pd.read_csv(
    "data/duplicate_gene_annotations.csv"
)

results = []

print("DUPLICATE GENE FUNCTIONAL CLASSIFICATION")
print("----------------------------------------")

for number, group in enumerate(duplicate_groups, start=1):

    selected = annotations[
        annotations["Gene ID"].isin(group)
    ]

    print(f"\nGROUP {number}")

    for _, row in selected.iterrows():

        print(
            row["Gene ID"],
            "|",
            row["Product Description"],
            "|",
            row["Gene Type"],
            "| Chromosome:",
            row["Chromosome"]
        )

        results.append({
            "Group": number,
            "Gene ID": row["Gene ID"],
            "Product Description": row["Product Description"],
            "Gene Type": row["Gene Type"],
            "Gene Symbol": row["Gene Name or Symbol"],
            "Transcript Length": row["Transcript Length"],
            "Chromosome": row["Chromosome"]
        })

# Save results
output = pd.DataFrame(results)

output.to_csv(
    "data/duplicate_gene_group_annotations.csv",
    index=False
)

print("\nTotal genes classified:", len(output))
print("Groups analysed:", len(duplicate_groups))
print("Saved to data/duplicate_gene_group_annotations.csv")