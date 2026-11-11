# EPF1 Sequence Identity Investigation

## 1. Objective

To investigate three *Plasmodium falciparum* exported protein family 1 (EPF1) genes that exhibited identical expression profiles across 140 samples in GEO dataset GSE241277.

## 2. Genes investigated

- PF3D7_0222000
- PF3D7_0324000
- PF3D7_0601300

## 3. Methodology

Coding DNA sequences (CDS) were retrieved from PlasmoDB using the FASTA format.

Python was used to:
- Read the three FASTA files.
- Determine sequence lengths.
- Perform pairwise nucleotide sequence comparisons.
- Count differences between corresponding nucleotide positions.

## 4. Results

All three sequences were 849 base pairs long.

| Comparison | Sequence identity | Differences |
|---|---:|---:|
| PF3D7_0222000 vs PF3D7_0324000 | 100% | 0 |
| PF3D7_0222000 vs PF3D7_0601300 | 100% | 0 |
| PF3D7_0324000 vs PF3D7_0601300 | 100% | 0 |

All three genes also exhibited identical expression profiles across the 140 samples analysed.

## 5. Interpretation

The identical CDS sequences and expression profiles indicate a strong sequence-level similarity among the three EPF1 genes.

Because the original study used Kallisto for transcript quantification, identical coding sequences could contribute to ambiguity when assigning sequencing reads to individual transcripts.

However, this investigation does not establish the precise cause of the identical expression profiles.

## 6. Limitations

- Complete transcript sequences, including untranslated regions, were not compared.
- The original sequencing reads and Kallisto abundance estimates were not independently reanalysed.
- The investigation does not establish how individual sequencing reads were assigned.
- The results do not demonstrate that the three genes have identical biological functions or regulation.

## 7. Conclusion

The three investigated EPF1 genes possess identical annotated CDS sequences of 849 bp and identical expression profiles across the 140 samples in GSE241277.

This finding highlights the importance of sequence similarity when interpreting transcript-level expression estimates in *Plasmodium falciparum*.