import pandas as pd

df = pd.read_csv('data/taxonomy.csv', header=0)
genera = []
for row in df.itertuples():
    g = row.Kingdom
    if not pd.isna(row.Phylum):
        g += ";"+row.Phylum
        if not pd.isna(row.Class):
            g += ";"+row.Class
            if not pd.isna(row.Order):
                g += ";"+row.Order
                if not pd.isna(row.Family):
                    g += ";"+row.Family
                    if not pd.isna(row.Genus):
                        g += ";"+row.Genus
    g = g.replace("-",";")
    g = g.replace("[","").replace("]","")
    g = g.replace("g__d","g__02d06")
    genera.append(g)
df['Genera'] = genera
df.to_csv('data/taxonomy1.csv',index=False)