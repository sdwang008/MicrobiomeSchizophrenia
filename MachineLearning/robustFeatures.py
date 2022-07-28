from operator import index
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

# Species
count = Counter()

path = "Species300/normalized-table_diagnosis/features/"
fnames = ["rdforest_infogain_300_FEATURES.csv", "rdforest_jmi_300_FEATURES.csv", "rdforest_mrmr_300_FEATURES.csv", "rdforest_variance_300_FEATURES.csv"]

for fname in fnames:
    df = pd.read_csv(path+fname, header=0, index_col=0)
    counter = Counter()
    for c in df.columns:
        counter.update(df[c])

    for f, v in counter.items():
        if v >= 95:
            count.update({f:1})

robust_features = []
for f, v in count.items():
    if not '.' in f.split('_')[-1]:
        robust_features.append(f)

print(len(robust_features))

count = Counter()
taxonomy = pd.read_csv("data/taxonomy1.csv", header=0, index_col=0)
for c in robust_features:
    count.update({str(taxonomy.at[c,'Family'])+"+"+str(taxonomy.at[c,'Phylum']):1})
print(count.most_common(10))

# table = pd.read_csv('genus-table-final.csv', header=0)
# table = pd.read_csv('normalized-table.csv', header=0)
# robust_features.append("diagnosis")
# table = table[robust_features]
# print(table.shape)
# table.to_csv("robust-table-95.csv", index=False)



# Genus
# count = Counter()

# path = "GenusFinal/genus-table-normalized_diagnosis/features/"
# fnames = ["rdforest_infogain_100_FEATURES.csv", "rdforest_jmi_100_FEATURES.csv", "rdforest_mrmr_100_FEATURES.csv", "rdforest_variance_100_FEATURES.csv"]

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


# Visualize
fig = plt.figure(figsize=(8,5))
fig.set_dpi(300)
plt.rcParams.update({'font.size': 14})

keys = [x[0][3:].split("+")[0] for x in count.most_common(8) if not pd.isna(x[0])]
keys[2] = 'Unassigned'
values = [x[1] for x in count.most_common(8) if not pd.isna(x[0])]
fig = sns.barplot(x=keys, y=values, palette=['g','g','g','orange','g','g','orange','orange'])
patch1 = mpatches.Patch(label='Firmicutes', facecolor='green')
patch2 = mpatches.Patch(label='Bacteroidetes', facecolor='orange')
patches = [patch1, patch2]
plt.legend(handles=patches, title='Phylum')
plt.xticks(rotation=45, ha='right')
tickcolors = ['orange','red','black','black','black','black','black','black']
for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), tickcolors):
    ticklabel.set_color(tickcolor)
plt.yticks(fontsize=18)
plt.yticks([0,40,80])
plt.tight_layout()
plt.savefig('robust.tiff', dpi=300)
plt.show()