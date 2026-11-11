import pandas as pd
import numpy as np

file_path = "data/GSE241277_Fourier_transformed_nTPM.xlsx"

df = pd.read_excel(file_path)

genes = [
    "PF3D7_0222000",
    "PF3D7_0324000",
    "PF3D7_0601300"
]

print("EPF1 IDENTICAL EXPRESSION INVESTIGATION")
print("--------------------------------------")

for gene in genes:

    row = df[df["GeneID"] == gene]

    values = row.iloc[0, 1:].astype(float).values

    print(f"\nGene: {gene}")
    print("First 10 expression values:")
    print(values[:10])

    print("Mean:", np.mean(values))
    print("Standard deviation:", np.std(values))

print("\nAll three profiles identical:",
      np.array_equal(
          df[df["GeneID"] == genes[0]].iloc[0, 1:].values,
          df[df["GeneID"] == genes[1]].iloc[0, 1:].values
      ) and np.array_equal(
          df[df["GeneID"] == genes[0]].iloc[0, 1:].values,
          df[df["GeneID"] == genes[2]].iloc[0, 1:].values
      ))