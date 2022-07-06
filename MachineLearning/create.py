from operator import index
import pandas as pd
import numpy as np

df = pd.read_csv("data/normalized-table.csv", header=0)
# df = pd.read_csv("data/genus-table-normalized.csv", header=0)
taxonomy = pd.read_csv('data/taxonomy1.csv', header=0, index_col=0)

df1 = pd.read_csv('genus1.tsv', delimiter='\t', header=0)
df1 = df1.sort_values(by=['W'], ascending=False)
# df1['family'] = df1['id'].map(lambda x: ";".join(x.split(';')[:-2]))
df1 = df1[:8]
genus = list(df1['id'])

features = []
for c in df.columns[:-1]:
    if taxonomy.at[c, 'Genera'] in genus:
    # if taxonomy.at[c, 'Family'] in ['f__Lachnospiraceae', 'f__Pasteurellaceae', 'f__Clostridiaceae', 'f__Erysipelotrichaceae', 'f__Ruminococcaceae']:
    # if taxonomy.at[c, 'Family'] in ['f__Lachnospiraceae', 'f__Ruminococcaceae']:
    # if 'f__Lachnospiraceae' in c or 'f__Ruminococcaceae' in c:
    # if 'f__Lachnospiraceae' in c or 'f__Ruminococcaceae' in c or 'f__Pasteurellaceae' in c or 'f__Clostridiaceae' in c or 'f__Erysipelotrichaceae' in c:
        features.append(c)
features.append('diagnosis')

df = df[features]
print(df.shape)
# df.to_csv('five-family-table-species.csv', index=False)