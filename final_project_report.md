# Comparative Transcriptomic Analysis of Plasmodium falciparum Extracellular Vesicle and Intracellular RNA Profiles

**Author:** Evans Kioko  
**Study organism:** *Plasmodium falciparum*  
**Dataset:** GEO GSE241277  
**Analysis type:** Public-data bioinformatics reanalysis

---

## 1. Abstract

Extracellular vesicles (EVs) are membrane-bound particles that can transport biological molecules, including RNA. This project investigated differences between extracellular vesicle-associated RNA and whole-parasite intracellular RNA profiles in *Plasmodium falciparum* using publicly available transcriptomic data.

The analysis used GEO dataset GSE241277, comprising 140 samples representing EV-associated RNA and whole-parasite RNA across six parasite lines and multiple developmental time points.

Python was used for metadata processing, expression-data inspection, sample-level quality control, group-level expression comparisons, functional annotation summaries and investigation of identical expression profiles.

The analysis identified 5,239 genes and 140 samples. Sample-level expression variability was greater in the whole-parasite group than in the EV group. Additional investigation identified 13 groups containing 30 genes with exactly identical expression profiles across all samples. Three EPF1 genes within one of these groups also had identical annotated coding DNA sequences.

These findings provide a descriptive computational comparison of EV-associated and intracellular RNA profiles while highlighting the importance of sequence similarity and transcript quantification when interpreting expression data.

## 2. Introduction

*Plasmodium falciparum* is the parasite responsible for the most severe form of human malaria.

Extracellular vesicles have attracted research interest because they can transport molecular cargo, including RNA, between biological environments.

Understanding the RNA profiles associated with extracellular vesicles compared with intracellular parasite RNA may provide insight into molecular composition and potential post-transcriptional processes.

Bioinformatics provides computational approaches for examining such transcriptomic datasets, identifying expression patterns, investigating gene annotations and evaluating data quality.

This project reanalyses publicly available transcriptomic data to explore differences between EV-associated RNA and whole-parasite RNA profiles.

## 3. Aim

To computationally investigate differences in extracellular vesicle-associated RNA and whole-parasite intracellular RNA profiles in *Plasmodium falciparum*.

## 4. Specific objectives

1. Retrieve and inspect publicly available transcriptomic data.
2. Extract and organise sample metadata.
3. Match sample metadata to expression-matrix columns.
4. Perform exploratory expression-data analysis and quality control.
5. Compare EV and whole-parasite expression profiles descriptively.
6. Investigate highly differing genes and their functional annotations.
7. Identify genes with identical expression profiles.
8. Investigate sequence similarity among selected EPF1 genes.

## 5. Dataset description

The project used GEO Series GSE241277.

**Dataset source:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241277

**Associated publication:** https://doi.org/10.1038/s41467-023-42103-x

The dataset contains RNA-sequencing information from six *P. falciparum* parasite lines:

- KE04
- KE01
- sKE01
- Dd2
- KE06
- KE02

Two RNA categories were investigated:

- EV: extracellular vesicle-associated RNA.
- WP: whole-parasite intracellular RNA.

The study included 140 samples:

| Category | Samples |
|---|---:|
| EV | 70 |
| WP | 70 |
| Total | 140 |

Samples covered multiple parasite developmental time points.

The processed supplementary expression workbook contained 5,239 gene rows and 140 sample columns.

## 6. Methodology

### 6.1 Data retrieval

The GEO supplementary expression workbook and sample metadata were retrieved.

The expression workbook was imported into Python for inspection and analysis.

### 6.2 Metadata extraction and organisation

GEO metadata was extracted and organised into a structured CSV file.

The metadata included:

- GEO sample identifiers
- Sample titles
- Parasite cell lines
- Genotypes
- RNA categories
- Developmental time points

### 6.3 Expression and metadata matching

A sample-mapping script was developed to match the GEO sample metadata to the expression-matrix columns.

The matching process produced 140 unique mappings, with no unmatched samples or expression columns.

### 6.4 Exploratory data analysis

The expression matrix was examined for:

- Number of genes
- Number of samples
- Missing values
- Duplicate gene identifiers
- Minimum and maximum expression values
- Overall mean and median expression

### 6.5 Sample-level quality control

Mean expression, median expression and standard deviation were calculated for each sample.

The results were used to examine variation in expression distributions across the samples.

### 6.6 EV and WP comparison

Expression variability was compared between the EV and WP groups.

Gene-level group means were also calculated, and genes were ranked according to the absolute difference between their EV and WP mean expression values.

These comparisons were descriptive and were not treated as formal differential-expression tests.

### 6.7 Functional annotation

Selected genes were annotated using PlasmoDB.

Gene descriptions, gene types, transcript lengths and other available annotation fields were examined.

The 20 genes with the largest absolute EV-WP mean differences were assigned broad functional categories.

### 6.8 Investigation of identical expression profiles

Gene expression profiles were compared across all 140 samples.

Candidate groups with identical profiles were identified and verified using exact numerical comparisons.

A total of 13 groups containing 30 genes were identified.

### 6.9 EPF1 sequence investigation

Three genes with identical expression profiles were selected:

- PF3D7_0222000
- PF3D7_0324000
- PF3D7_0601300

Their annotated CDS sequences were downloaded from PlasmoDB and compared using Python.

## 7. Results

### 7.1 Expression matrix inspection

The processed expression matrix contained:

| Parameter | Result |
|---|---:|
| Genes | 5,239 |
| Samples | 140 |
| Missing values | 0 |
| Duplicate gene identifiers | 0 |
| Minimum value | 2.274 |
| Maximum value | 14.879 |
| Overall mean | 6.406 |
| Overall median | 6.377 |

### 7.2 Sample-level expression quality control

The mean expression values across samples ranged from approximately 6.322 to 6.513.

The relatively narrow range of sample means provided a useful initial overview of sample-level expression distributions.

**Figure 1:** Sample mean expression distribution.

File: `figures/sample_mean_distribution.png`

### 7.3 Comparison of EV and WP expression variability

The average sample-level standard deviation was:

| Group | Mean standard deviation |
|---|---:|
| EV | 0.916 |
| WP | 1.305 |

The WP samples exhibited greater expression variability across genes than the EV samples.

This is a descriptive observation and does not independently establish a biological explanation.

**Figure 2:** Comparison of EV and WP expression variability.

File: `figures/ev_wp_variability.png`

### 7.4 Gene-level expression comparison

The expression means of individual genes were compared between EV and WP samples.

Genes were ranked according to the absolute difference between their group means.

The resulting top 20 genes included genes associated with:

- Chromatin organisation
- Protein synthesis
- RNA processing
- DNA/RNA-associated functions
- Parasite protein export
- Other or unknown functions

**Figure 3:** Top 20 genes ranked by absolute EV-WP mean expression difference.

File: `figures/top20_gene_expression.png`

These results represent differences in group averages rather than statistically validated differential expression.

### 7.5 Functional annotation summary

The selected top 20 genes were classified into broad functional categories.

| Functional category | Number of genes |
|---|---:|
| Chromatin organisation | 4 |
| DNA/RNA-associated functions | 2 |
| Other or unknown functions | 2 |
| Parasite protein export | 5 |
| Protein synthesis | 5 |
| Pseudogene | 1 |
| RNA processing | 1 |

The functional-category comparison showed higher WP mean expression for several selected categories, while the parasite protein export category showed a higher EV mean.

**Figure 4:** Functional category expression differences.

File: `figures/functional_category_expression_difference.png`

This analysis was limited to the selected top 20 genes and was not a formal gene-set enrichment analysis.

### 7.6 Investigation of identical expression profiles

A comparison of all 5,239 gene profiles identified:

- 30 genes with repeated expression profiles.
- 13 groups of genes with identical profiles.
- All 13 groups were verified through exact numerical comparison.

All genes within each identified group had identical annotated transcript lengths.

The investigation also found that several groups contained genes annotated as exported protein families, while others contained non-coding RNAs, exported protein fragments or pseudogenes.

### 7.7 EPF1 coding sequence comparison

Three EPF1 genes were investigated further:

| Gene | CDS length |
|---|---:|
| PF3D7_0222000 | 849 bp |
| PF3D7_0324000 | 849 bp |
| PF3D7_0601300 | 849 bp |

Pairwise comparison produced the following results:

| Comparison | Nucleotide differences |
|---|---:|
| PF3D7_0222000 vs PF3D7_0324000 | 0 |
| PF3D7_0222000 vs PF3D7_0601300 | 0 |
| PF3D7_0324000 vs PF3D7_0601300 | 0 |

All three annotated CDS sequences were identical across all 849 nucleotide positions.

This observation is consistent with the identical expression profiles previously identified for these genes.

Because the original study used Kallisto for transcript quantification, sequence identity could contribute to ambiguity in assigning reads to individual transcripts.

However, the precise cause of the identical expression estimates has not been established.

## 8. Discussion

This project demonstrates how publicly available transcriptomic data can be investigated using Python-based bioinformatics workflows.

The sample-level analysis showed greater expression variability in WP samples than in EV samples.

The gene-level comparison identified genes with notable differences in average expression between the two RNA categories. Functional annotation provided biological context for selected genes.

An important additional finding was the presence of 13 groups of genes with exactly identical expression profiles across all 140 samples.

The investigation of three EPF1 genes revealed identical annotated CDS sequences, providing a possible sequence-level explanation for their indistinguishable expression profiles.

Nevertheless, identical CDS sequences alone do not establish how transcript quantification software assigned sequencing reads. Further examination of complete transcript sequences and the original quantification outputs would be necessary to establish the mechanism.

## 9. Limitations

1. The analysis used a processed supplementary expression matrix rather than raw sequencing reads.
2. The precise processing provenance of the supplementary expression workbook requires careful interpretation.
3. The expression comparisons were descriptive and did not establish statistically significant differential expression.
4. Functional classification was performed on a selected top 20 gene list rather than the entire genome.
5. The functional-category comparison was not a formal enrichment analysis.
6. Identical expression profiles do not independently establish the biological cause of the observed similarity.
7. The complete transcript sequences of the three EPF1 genes were not compared.
8. The original Kallisto transcript-level estimates were not independently reproduced.

## 10. Conclusion

This project successfully developed a Python-based workflow for examining publicly available *Plasmodium falciparum* transcriptomic data.

The analysis included dataset inspection, metadata organisation, sample mapping, expression quality control, EV-WP descriptive comparisons, functional annotation and investigation of identical gene expression profiles.

The identification of 13 groups containing 30 genes with identical expression profiles, together with the identical CDS sequences of three EPF1 genes, provides an interesting example of how sequence similarity should be considered when interpreting transcriptomic quantification results.

Overall, the project demonstrates practical applications of bioinformatics in malaria-related transcriptomic research.

## 11. Tools and resources

- Python
- pandas
- NumPy
- Matplotlib
- Visual Studio Code
- NCBI Gene Expression Omnibus (GEO)
- PlasmoDB
- Kallisto (as used in the original study)

## 12. Data and publication references

1. GEO dataset GSE241277: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241277
2. Original publication: https://doi.org/10.1038/s41467-023-42103-x
3. PlasmoDB: https://plasmodb.org/

---

**Project status:** Computational reanalysis of publicly available data.  
**Reproducibility:** Analysis scripts and generated outputs are organised in the accompanying repository.