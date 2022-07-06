from operator import index
import pandas as pd
import numpy as np
from collections import Counter

# count = Counter()

# path = "GenusFinal/genus-table-normalized_diagnosis/features/"
# # path = "Species300/normalized-table_diagnosis/features/"
# fnames = ["rdforest_infogain_100_FEATURES.csv", "rdforest_jmi_100_FEATURES.csv", "rdforest_mrmr_100_FEATURES.csv", "rdforest_variance_100_FEATURES.csv"]
# # fnames = ["rdforest_infogain_300_FEATURES.csv", "rdforest_jmi_300_FEATURES.csv", "rdforest_mrmr_300_FEATURES.csv", "rdforest_variance_300_FEATURES.csv"]

# for fname in fnames:
#     df = pd.read_csv(path+fname, header=0, index_col=0)
#     counter = Counter()
#     for c in df.columns:
#         counter.update(df[c])

#     for f, v in counter.items():
#         if v >= 95:
#             count.update({f:1})

# robust_features = []
# for f, v in count.items():
#     # robust_features.append(f.split('_')[0])
#     if not '.' in f.split('_')[-1]:
#         robust_features.append(f)

# print(len(robust_features))

# count = Counter()
# for c in robust_features:
#     count.update({c.split(";")[4]:1})
# print(count.most_common(10))

# table = pd.read_csv('genus-table-final.csv', header=0)
# table = pd.read_csv('normalized-table.csv', header=0)
# robust_features.append("diagnosis")
# table = table[robust_features]
# print(table.shape)
# table.to_csv("robust-table-95.csv", index=False)

df = pd.read_csv("robust-table-95.csv", header=0)
taxonomy = pd.read_csv("taxonomy1.csv", header=0, index_col=0)
count = Counter()
for c in df.columns[:-1]:
    print(c)
    count.update({taxonomy.at[c,'Family']:1})
print(count.most_common(10))