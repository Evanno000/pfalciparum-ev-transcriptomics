# Duplicate Expression Profile Quality Control

## Dataset
- GEO accession: GSE241277
- Organism: Plasmodium falciparum
- Total genes analysed: 5,239
- Total samples: 140
- Expression data: Fourier_transformed_nTPM.xlsx

## Method
Expression profiles were compared across all 140 samples.

Candidate duplicate groups were identified using profile hashes and subsequently verified through exact numerical comparisons using NumPy.

## Results

- Total genes: 5,239
- Genes belonging to duplicate groups: 30
- Number of duplicate groups: 13
- Groups confirmed by exact numerical comparison: 13

All 13 groups contained genes with exactly identical expression values across all 140 samples.

## Example: EPF1 gene family

Three genes shared identical profiles:

- PF3D7_0222000
- PF3D7_0324000
- PF3D7_0601300

All three are annotated as protein-coding genes belonging to the exported protein family 1 (EPF1).

## Interpretation

The presence of identical expression profiles across distinct gene identifiers raises questions about the independence of some gene-level expression estimates.

Possible explanations include shared transcript quantification, sequence similarity or features of the data-processing pipeline.

Further investigation of gene annotations and transcript quantification is required.

## Limitation

Identical expression profiles alone do not establish the cause of the repeated values or demonstrate that the dataset contains errors.

These observations should be considered when interpreting gene-level expression differences.

## Conclusion

Thirteen groups containing 30 genes were identified with exactly identical expression profiles across 140 samples. This finding was confirmed using exact numerical comparisons and documented as a dataset quality-control observation.

## 5. Transcript Length Comparison

Transcript annotations for all 30 genes were examined.

Results:
- 13 duplicate expression groups were identified.
- All 13 groups had identical transcript lengths within each group.
- The matching lengths ranged from 135 bp to 930 bp.
- Genes within each group also had identical expression profiles across all 140 samples.

These observations show a consistent pattern between transcript length and expression-profile similarity. However, matching transcript lengths do not establish identical nucleotide sequences or explain the cause of the matching expression values.

Further sequence-level investigation would be needed to determine whether sequence similarity or transcript quantification contributes to this pattern.