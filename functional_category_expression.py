import pandas as pd

# Load classified genes
df = pd.read_csv("data/top20_functional_classification.csv")

# Separate the pseudogene
df["Analysis_Category"] = df["Functional_Category"]

df.loc[
    df["Is Pseudo"].astype(str).str.lower() == "yes",
    "Analysis_Category"
] = "Pseudogene"

# Calculate expression summaries by category
summary = (
    df.groupby("Analysis_Category")
    .agg(
        Number_of_Genes=("Gene ID", "count"),
        Mean_EV_Expression=("EV_mean", "mean"),
        Mean_WP_Expression=("WP_mean", "mean"),
        Mean_EV_minus_WP=("EV_minus_WP", "mean")
    )
    .reset_index()
)

# Round numerical values
summary = summary.round(3)

# Display results
print("\nFUNCTIONAL CATEGORY EXPRESSION SUMMARY")
print("--------------------------------------")

print(summary.to_string(index=False))

# Save results
summary.to_csv(
    "data/functional_category_expression_summary.csv",
    index=False
)

print("\nCategory expression summary saved successfully!")