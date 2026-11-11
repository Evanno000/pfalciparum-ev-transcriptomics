# Comparative Transcriptomic Analysis of *Plasmodium falciparum* Extracellular Vesicle and Intracellular RNA Profiles

**Author:** Evans Kioko  
**Project Type:** Bioinformatics | Transcriptomics | Malaria Research  
**Dataset:** GEO GSE241277  
**Organism:** *Plasmodium falciparum*

## Project Overview

This project presents a computational reanalysis of publicly available RNA-sequencing data from *Plasmodium falciparum*.

It investigates differences between extracellular vesicle-associated RNA (EV) and whole-parasite intracellular RNA (WP) profiles using Python-based bioinformatics approaches.

The analysis includes dataset inspection, metadata organisation, expression quality control, descriptive expression comparisons, functional annotation and investigation of genes with identical expression profiles.

## Research Background

Extracellular vesicles are membrane-bound particles that can carry biological molecules, including RNA.

Investigating their RNA content alongside intracellular parasite RNA may provide insights into the molecular composition of extracellular vesicles and potential post-transcriptional processes.

This project uses publicly available data to explore these differences computationally.

## Research Objectives

1. Inspect and organise publicly available transcriptomic data.
2. Extract and match sample metadata with expression data.
3. Perform exploratory expression analysis and sample-level quality control.
4. Compare EV-associated and whole-parasite RNA profiles.
5. Investigate genes with large differences in group mean expression.
6. Classify selected genes using functional annotations.
7. Identify genes with identical expression profiles.
8. Investigate sequence similarity among selected EPF1 genes.

## Dataset

**GEO accession:** GSE241277

**Dataset link:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241277

**Original publication:** https://doi.org/10.1038/s41467-023-42103-x

The dataset contains 140 samples:

| RNA category | Number of samples |
|---|---:|
| Extracellular vesicle-associated RNA (EV) | 70 |
| Whole-parasite RNA (WP) | 70 |
| **Total** | **140** |

Six *P. falciparum* parasite lines were represented.

The processed expression matrix contained 5,239 genes and 140 sample columns.

## Methodology

The project was conducted using Python and publicly available biological datasets.

### 1. Dataset inspection
- Examined expression matrix dimensions.
- Checked missing values and duplicate gene identifiers.
- Calculated basic expression statistics.

### 2. Metadata processing
- Extracted sample information from GEO metadata.
- Organised parasite lines, RNA categories and time points.
- Matched metadata records to expression-matrix columns.

### 3. Exploratory data analysis
- Examined sample-level mean expression.
- Calculated median expression and standard deviation.
- Generated expression distribution visualisations.

### 4. EV versus WP comparison
- Compared sample-level expression variability.
- Calculated gene-level group means.
- Identified genes with the largest absolute differences in group mean expression.

### 5. Functional annotation
- Retrieved gene annotations from PlasmoDB.
- Examined gene descriptions and transcript information.
- Classified selected genes into broad functional categories.

### 6. Duplicate expression profile investigation
- Identified genes with identical expression profiles across 140 samples.
- Verified candidate groups using exact numerical comparisons.
- Investigated transcript lengths and gene annotations.

### 7. EPF1 sequence comparison
Three EPF1 genes were selected for further investigation:

- PF3D7_0222000
- PF3D7_0324000
- PF3D7_0601300

Their annotated coding DNA sequences were retrieved from PlasmoDB and compared using Python.

## Key Findings

### Expression matrix quality control

| Parameter | Result |
|---|---:|
| Total genes | 5,239 |
| Total samples | 140 |
| Missing values | 0 |
| Duplicate gene IDs | 0 |

### EV and WP expression variability

| Group | Mean sample-level standard deviation |
|---|---:|
| EV | 0.916 |
| WP | 1.305 |

WP samples showed greater expression variability across genes than EV samples.

### Identical expression profiles

A total of 30 genes were identified in 13 groups with exactly identical expression profiles across all 140 samples.

### EPF1 sequence investigation

The three selected EPF1 genes had:

- Identical CDS lengths of 849 bp.
- Zero nucleotide differences in all pairwise comparisons.
- Identical expression profiles across all 140 samples.

This observation raises an important question about sequence similarity and ambiguity in transcript-level quantification.

The precise cause of the identical expression profiles has not been established.

## Visualisations

The project generated the following figures:

| Figure | Description |
|---|---|
| `sample_mean_distribution.png` | Distribution of sample mean expression |
| `ev_wp_variability.png` | Comparison of EV and WP expression variability |
| `top20_gene_expression.png` | Expression comparison of selected top 20 genes |
| `functional_category_expression_difference.png` | Expression differences across functional categories |

All figures are stored in the `figures/` directory.

## Repository Structure

```text
pfalciparum-ev-transcriptomics/
│
├── data/
│   ├── Expression data
│   ├── Sample metadata
│   ├── Gene annotations
│   ├── Functional classifications
│   └── EPF1 FASTA sequences
│
├── figures/
│   ├── sample_mean_distribution.png
│   ├── ev_wp_variability.png
│   ├── top20_gene_expression.png
│   └── functional_category_expression_difference.png
│
├── report/
│   ├── preliminary_dataset_summary.md
│   ├── ev_wp_qc_summary.csv
│   ├── duplicate_expression_profile_qc.md
│   ├── duplicate_transcript_length_analysis.md
│   ├── epf1_sequence_investigation.md
│   └── final_project_report.md
│
├── scripts/
│   ├── Dataset inspection and metadata scripts
│   ├── Expression analysis and QC scripts
│   ├── Functional annotation scripts
│   ├── Duplicate expression investigation scripts
│   └── EPF1 sequence comparison script
│
└── README.md
```

## Tools and Technologies

- **Python:** Data processing and computational analysis.
- **pandas:** Tabular data manipulation.
- **NumPy:** Numerical calculations and sequence-profile comparisons.
- **Matplotlib:** Data visualisation.
- **Visual Studio Code:** Development environment.
- **GEO:** Public transcriptomic data source.
- **PlasmoDB:** Parasite genome and gene annotation resource.

## Limitations

- The analysis used a processed supplementary expression matrix rather than raw sequencing reads.
- Expression comparisons were descriptive and were not formal differential-expression tests.
- Functional classification was restricted to selected genes.
- The complete transcript sequences of the three EPF1 genes were not compared.
- The original Kallisto quantification was not independently reproduced.
- Identical expression profiles do not establish their underlying biological or computational cause.

## Scientific Significance

This project demonstrates the application of computational biology and bioinformatics techniques to malaria-related transcriptomic research.

It also highlights the importance of considering sequence similarity when interpreting transcript-level expression estimates.

## References

1. GEO Series GSE241277: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241277
2. Original research publication: https://doi.org/10.1038/s41467-023-42103-x
3. PlasmoDB: https://plasmodb.org/

---

**Project status:** Public-data computational reanalysis.

**Reproducibility:** Python analysis scripts, generated figures and supporting reports are included in this repository.