import pandas as pd

df = pd.read_csv(
    "data/duplicate_gene_group_annotations.csv"
)

print("DUPLICATE GROUP TRANSCRIPT LENGTH ANALYSIS")
print("------------------------------------------")

for group_number, group in df.groupby("Group"):

    print(f"\nGROUP {group_number}")

    print(
        group[
            ["Gene ID", "Product Description",
             "Transcript Length", "Chromosome"]
        ].to_string(index=False)
    )

    lengths = group["Transcript Length"].unique()

    print("Identical transcript lengths:", len(lengths) == 1)
    print("Distinct transcript lengths:", len(lengths))

print("\nAnalysis completed.")