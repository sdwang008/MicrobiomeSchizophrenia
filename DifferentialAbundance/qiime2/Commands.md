## 0. Get Taxonomy (need to download the classifier file first)
```
qiime feature-classifier classify-sklearn \
--i-classifier gg-13-8-99-515-806-nb-classifier.qza \
--i-reads rep-seqs.qza \
--o-classification taxonomy.qza
```

## 1. Get Table on the Genus Level and Filter
```
qiime taxa collapse \
--i-table feature-table.qza \
--i-taxonomy taxonomy.qza \
--p-level 6 \
--o-collapsed-table genus-table.qza
```
```
qiime feature-table filter-features \
  --i-table genus-table.qza \
  --p-min-frequency 10 \
  --p-min-samples 10 \
  --o-filtered-table filtered-genus-table.qza
```

## 2. ANCOM
```
qiime composition add-pseudocount \
--i-table filtered-genus-table.qza \
--o-composition-table filtered-genus-table-comp.qza
```

```
qiime composition ancom \
--i-table filtered-genus-table-comp.qza \
--m-metadata-file metadata.tsv \
--m-metadata-column diagnosis \
--o-visualization filtered-ancom-genus.qzv
  ```