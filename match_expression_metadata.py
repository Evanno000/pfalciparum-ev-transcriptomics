import pandas as pd
from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Load metadata and expression column names
metadata = pd.read_csv(DATA_DIR / "organised_metadata.csv")

expression = pd.read_excel(
    DATA_DIR / "GSE241277_Fourier_transformed_nTPM.xlsx",
    nrows=0
)

# Extract expression column identifiers from metadata titles
parts = metadata["Title"].str.extract(
    r"^(41107_\d+)_(\d+)_"
)

metadata["Expression_Column"] = (
    parts[0] + "#" + parts[1]
)

# Validate mapping
expression_columns = set(expression.columns[1:])
mapped_columns = set(metadata["Expression_Column"])

assert len(metadata) == 140
assert metadata["Expression_Column"].nunique() == 140
assert mapped_columns == expression_columns

# Save validated sample mapping
output_file = DATA_DIR / "sample_mapping.csv"
metadata.to_csv(output_file, index=False)

print("SAMPLE MAPPING VALIDATION")
print("-------------------------")
print("Metadata samples:", len(metadata))
print("Expression columns:", len(expression_columns))
print("Unique mappings:", metadata["Expression_Column"].nunique())
print("Unmatched samples:", len(mapped_columns - expression_columns))
print("Unmatched columns:", len(expression_columns - mapped_columns))

print("\nMapping successfully saved!")
print("Output:", output_file)