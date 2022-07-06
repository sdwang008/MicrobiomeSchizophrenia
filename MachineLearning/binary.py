import pandas as pd
import numpy as np

df = pd.read_csv("row-normalized-table.csv", delimiter=',', header=0)
labels = np.array(df['diagnosis'])
features = df.drop(['sampleid', 'diagnosis'], axis=1)
Y_binary = [1 if y=='SZ' else 0 for y in labels]
features['diagnosis'] = Y_binary
features.to_csv('feature-table.csv',index=False)