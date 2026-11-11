
from pathlib import Path

# Locate the project and data folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# The three EPF1 genes
gene_ids = [
    "PF3D7_0222000",
    "PF3D7_0324000",
    "PF3D7_0601300"
]


def read_fasta(file_path):
    """Read a single-sequence FASTA file."""
    lines = file_path.read_text().splitlines()

    sequence = "".join(
        line.strip()
        for line in lines
        if line.strip() and not line.startswith(">")
    )

    return sequence.upper()


# Load all three sequences
sequences = {}

for gene in gene_ids:
    fasta_file = DATA_DIR / f"{gene}.fasta"

    if not fasta_file.exists():
        raise FileNotFoundError(f"Missing file: {fasta_file}")

    sequences[gene] = read_fasta(fasta_file)


# Display sequence lengths
print("EPF1 CDS SEQUENCE COMPARISON")
print("-" * 40)

for gene, sequence in sequences.items():
    print(f"{gene}: {len(sequence)} bp")


# Compare every pair of sequences
print("\nPAIRWISE SEQUENCE COMPARISON")
print("-" * 40)

for i in range(len(gene_ids)):
    for j in range(i + 1, len(gene_ids)):

        gene_a = gene_ids[i]
        gene_b = gene_ids[j]

        seq_a = sequences[gene_a]
        seq_b = sequences[gene_b]

        identical = seq_a == seq_b

        print(f"\n{gene_a} vs {gene_b}")
        print(f"Identical sequences: {identical}")

        if len(seq_a) == len(seq_b):
            differences = sum(
                base_a != base_b
                for base_a, base_b in zip(seq_a, seq_b)
            )

            print(f"Different nucleotide positions: {differences}")
        else:
            print("Sequences have different lengths.")
