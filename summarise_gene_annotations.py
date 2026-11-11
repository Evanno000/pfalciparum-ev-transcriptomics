import pandas as pd

# Load annotation data
annotations = pd.read_csv("data/top20_gene_annotations.csv")

# Summarise gene types
print("GENE TYPE DISTRIBUTION")
print("----------------------")
print(annotations["Gene Type"].value_counts())

# Identify pseudogenes
print("\nPSEUDOGENES")
print("------------")
print(
    annotations.loc[
        annotations["Is Pseudo"] == "Yes",
        ["Gene ID", "Product Description"]
    ].to_string(index=False)
)

# Identify missing gene symbols
print("\nMISSING GENE SYMBOLS")
print("--------------------")
print(
    annotations[
        annotations["Gene Name or Symbol"].isna()
    ][["Gene ID", "Product Description"]].to_string(index=False)
)

# Save functional annotation summary
annotations.to_csv(
    "data/functional_annotation_summary.csv",
    index=False
)

print("\nFunctional annotation summary saved!")