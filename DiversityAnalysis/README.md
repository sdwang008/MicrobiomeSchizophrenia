# Diversity Analysis

All analysis is done through QIIME 2, except graphing PCoA is done in [pcoa.ipynb](pcoa.ipynb) using scikit-bio. 

Refer to QIIME 2's [tutorial](https://docs.qiime2.org/2022.2/tutorials/moving-pictures/#alpha-and-beta-diversity-analysis) for diversity analysis. For sub-group beta diversity analysis, refer to Qiime 2's tutorial and [Commands.md](qiime2/Commands.md) for specific commands. 

## Sub-group Diversity

First, obtain feature table, phylogenetic tree, representative sequences and convert them into QIIME 2 formats. Then, filter feature table based on the feature (diagnosis, sex, race, etc.). Use QIIME 2 commands on the filtered table to conduct beta diversity analysis. 