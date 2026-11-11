import pandas as pd

# Load gene annotations
file_path = "data/top20_gene_annotations.csv"

annotations = pd.read_csv(file_path)

# Display dataset dimensions
print("ANNOTATION DATASET")
print("------------------")
print("Rows:", annotations.shape[0])
print("Columns:", annotations.shape[1])

# Display column names
print("\nAVAILABLE COLUMNS")
print("-----------------")
print(annotations.columns.tolist())

# Display first five records
print("\nFIRST FIVE RECORDS")
print("------------------")
print(annotations.head().to_string(index=False))