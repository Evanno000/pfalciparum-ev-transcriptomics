import pandas as pd

# Load datasets
expression = pd.read_csv("data/top20_gene_list.csv")
annotations = pd.read_csv("data/functional_annotation_summary.csv")

# Rename GeneID to Gene ID
expression = expression.rename(columns={"GeneID": "Gene ID"})

# Merge datasets
merged = pd.merge(
    expression,
    annotations,
    on="Gene ID",
    how="left"
)

# Classify biological functions
def classify_function(description):

    description = str(description).lower()

    if "histone" in description or "high mobility group" in description:
        return "Chromatin organisation"

    elif "ribosomal protein" in description:
        return "Protein synthesis"

    elif "exported protein" in description:
        return "Parasite protein export"

    elif "small nucleolar rna" in description:
        return "RNA processing"

    elif "alba" in description:
        return "DNA/RNA-associated functions"

    else:
        return "Other / unknown functions"


merged["Functional_Category"] = merged[
    "Product Description"
].apply(classify_function)

# Display classification
print("\nGENE FUNCTIONAL CLASSIFICATION")
print("--------------------------------")

print(
    merged[
        ["Gene ID", "Product Description", "Functional_Category"]
    ].to_string(index=False)
)

# Category summary
print("\nFUNCTIONAL CATEGORY COUNTS")
print("--------------------------")

print(merged["Functional_Category"].value_counts())

# Save results
merged.to_csv(
    "data/top20_functional_classification.csv",
    index=False
)

print("\nFunctional classification saved successfully!")