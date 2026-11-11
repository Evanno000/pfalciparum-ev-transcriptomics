import pandas as pd

# Load annotation file
df = pd.read_csv(
    "data/duplicate_gene_annotations.csv"
)

print("DUPLICATE GENE ANNOTATION QC")
print("----------------------------")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nAvailable columns:")
print(df.columns.tolist())

print("\nFirst five records:")
print(df.head().to_string(index=False))

print("\nUnique gene IDs:", df.iloc[:, 0].nunique())

print("\nMissing values:")
print(df.isnull().sum())