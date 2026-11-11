import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

file = DATA_DIR / "GSE241277_Fourier_transformed_nTPM.xlsx"

df = pd.read_excel(file)

# Extract numerical expression values
expression = df.drop(columns=["GeneID"])

print("EXPRESSION DATA SUMMARY")
print("-----------------------")

print("\nOverall statistics:")
print(expression.describe().round(3))

print("\nMinimum expression:", expression.min().min())
print("Maximum expression:", expression.max().max())
print("Mean expression:", round(expression.mean().mean(), 3))
print("Median expression:", round(expression.stack().median(), 3))