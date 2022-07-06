# Beta Diversity Commands
Change ```p-sampling-depth``` accordingly (9465 for this dataset is best)
```
qiime diversity core-metrics-phylogenetic \
--i-phylogeny rooted-tree.qza \
--i-table feature-table.qza \
--p-sampling-depth 9465 \
--m-metadata-file metadata.tsv \
--output-dir core-metrics-results
```
Change the input distance matrix file accordingly
```
qiime diversity beta-group-significance \
--i-distance-matrix core-metrics-results/bray_curtis_distance_matrix.qza \
--m-metadata-file metadata.tsv \
--m-metadata-column diagnosis \
--o-visualization core-metrics-results/bray-curtis-significance.qzv \
--p-pairwise
```

# Sub-group Beta Diversity Commands
## 0. Commands to import rep sequences and tree to QIIME 2 format
```
qiime tools import \
--input-path reference-hit.seqs.fa \
--type 'FeatureData[Sequence]' \
--output-path rep-seqs.qza

qiime tools import \
--input-path insertion_tree.relabelled.tre \
--type 'Phylogeny[Rooted]' \
--output-path rooted-tree.qza
```

## 1. Filter table depending on clinical factor
Change ```p-where``` to get different filtered tables ([QIIME 2 documentation](https://docs.qiime2.org/2019.10/tutorials/filtering/))
```
qiime feature-table filter-samples \
--i-table feature-table.qza \
--m-metadata-file metadata.tsv \
--p-where "[diagnosis]='HC'" \
--o-filtered-table sex/healthy-table.qza
```

## 2. Diversity analysis
Change ```output-dir``` accordingly
```
qiime diversity core-metrics-phylogenetic \
--i-phylogeny rooted-tree.qza \
--i-table sex/healthy-table.qza \
--p-sampling-depth 9465 \
--m-metadata-file metadata.tsv \
--output-dir sex/healthy-h-vs-s
```

## 3. PERMANOVA for group significance
Can change bray-curtis to other available distance metrics (unweighted UniFrac)
```
qiime diversity beta-group-significance \
--i-distance-matrix sex/healthy-h-vs-s/bray_curtis_distance_matrix.qza \
--m-metadata-file metadata.tsv \
--m-metadata-column diagnosis \
--o-visualization sex/healthy-h-vs-s/bray-curtis-significance.qzv \
--p-pairwise
```