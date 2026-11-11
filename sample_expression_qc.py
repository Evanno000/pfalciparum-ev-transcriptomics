import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Load expression matrix
df = pd.read_excel(
    DATA_DIR / "GSE241277_Fourier_transformed_nTPM.xlsx"
)

# Extract expression values
expression = df.drop(columns=["GeneID"])

# Calculate statistics for every sample
summary = pd.DataFrame({
    "Sample": expression.columns,
    "Mean": expression.mean().values,
    "Median": expression.median().values,
    "Standard_Deviation": expression.std().values,
    "Minimum": expression.min().values,
    "Maximum": expression.max().values
})

# Save results
output = DATA_DIR / "sample_expression_summary.csv"
summary.to_csv(output, index=False)

print("SAMPLE-LEVEL EXPRESSION QC")
print("--------------------------")
print("Samples analysed:", len(summary))

print("\nLowest 5 sample means:")
print(
    summary.nsmallest(5, "Mean").round(3).to_string(index=False)
)

print("\nHighest 5 sample means:")
print(
    summary.nlargest(5, "Mean").round(3).to_string(index=False)
)

print("\nOverall sample mean range:")
print(
    round(summary["Mean"].min(), 3),
    "to",
    round(summary["Mean"].max(), 3)
)

print("\nSaved:", output)