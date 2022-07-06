import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

df = pd.read_csv('genus.tsv', delimiter='\t', header=0)
df = df.sort_values(by=['W'], ascending=False)
df['family'] = df['id'].map(lambda x: x.split(';')[-2][3:])
df['genus'] = df['id'].map(lambda x: x.split(';')[-1][3:] if x.split(';')[-1][3:]!="" else "Unassigned")
df = df[:8]

ticklabels = []
for i in range(len(list(df['family']))):
    x = list(df['family'])[i]
    if x == 'Lachnospiraceae':
        ticklabels.append(list(df['genus'])[i]+" (L)")
    elif x == 'Ruminococcaceae':
        ticklabels.append(list(df['genus'])[i]+" (R)")
    elif x == 'Clostridiaceae':
        ticklabels.append(list(df['genus'])[i]+" (C)")
    elif x == 'Erysipelotrichaceae':
        ticklabels.append(list(df['genus'])[i]+" (E)")
    elif x == 'Pasteurellaceae':
        ticklabels.append(list(df['genus'])[i]+" (P)")
phylumColorsInOrder = ['green','blue','green','green','green','green','green','green']
tickColorsInOrder = ['red','blue','purple','green','red','orange','orange','red']

fig = plt.figure(figsize=(8,5))
fig.set_dpi(300)
plt.rcParams.update({'font.size': 15})
plt.bar(x=list(range(8)), height=list(df['W']), tick_label=ticklabels, color=phylumColorsInOrder)
patch1 = mpatches.Patch(label='Firmicutes', facecolor='green')
patch2 = mpatches.Patch(label='Proteobacteria', facecolor='blue')
patches = [patch1, patch2]
plt.legend(handles=patches, title='Phylum')
plt.xticks(rotation=45, ha='right')
plt.yticks(fontsize=18)
for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), tickColorsInOrder):
    ticklabel.set_color(tickcolor)
plt.yticks([0,100,200])
plt.tight_layout()
plt.savefig('differential.tiff', dpi=300)
plt.show()