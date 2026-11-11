import pandas as pd

# Load duplicate profile groups
expression = pd.read_excel(
    "data/GSE241277_Fourier_transformed_nTPM.xlsx"
)

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
    "data/top20_gene_annotations.csv"
)

print("DUPLICATE GENE ANNOTATION INVESTIGATION")
print("---------------------------------------")

for number, group in enumerate(duplicate_groups, start=1):

    print(f"\nGROUP {number}")
    print("Genes:", ", ".join(group))

    results = annotations[
        annotations["Gene ID"].isin(group)
    ]

    if results.empty:
        print("No annotations available in current annotation file.")

    else:
        print(
            results[
                ["Gene ID", "Product Description",
                 "Gene Type", "Transcript Length",
                 "Gene Name or Symbol", "Chromosome"]
            ].to_string(index=False)
        )

print("\nInvestigation completed.")