import pandas as pd
import numpy as np

# Load expression data
df = pd.read_excel(
    "data/GSE241277_Fourier_transformed_nTPM.xlsx"
)

# Separate gene IDs and numerical expression values
expression = df.set_index("GeneID")

# Identify candidate groups using profile hashes
hashes = pd.util.hash_pandas_object(
    expression,
    index=False
)

groups = {}

for gene, profile_hash in zip(expression.index, hashes):
    groups.setdefault(profile_hash, []).append(gene)

print("EXACT DUPLICATE PROFILE VERIFICATION")
print("------------------------------------")

verified_groups = 0

for group in groups.values():

    if len(group) < 2:
        continue

    reference = expression.loc[group[0]].to_numpy(dtype=float)

    identical = all(
        np.array_equal(
            reference,
            expression.loc[gene].to_numpy(dtype=float)
        )
        for gene in group[1:]
    )

    print("\nGenes:", group)
    print("Exact profiles identical:", identical)

    if identical:
        verified_groups += 1

print("\nTotal verified duplicate groups:", verified_groups)
print("Verification completed.")