'''
This script is based on the heatmap() function in stats.py
'''

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
from matplotlib.ticker import PercentFormatter

path = "Species300/normalized-table_diagnosis"
df1 = pd.read_csv(path+"/STATS/max_scores_in_summary.csv", index_col=0, header=0)
df2 = pd.read_csv(path+"/STATS/8gs.csv", index_col=0, header=0)
df2['filename'] = df2['filename'].map(lambda x: x.replace("AllFeatures", "Top8Genus"))

df = pd.concat([df1,df2])

df['Accuracy'] = round(df['Accuracy'],3)
df['F1'] = round(df['F1'],3)
filenames = df["filename"]
featureselection = []
group = []
classifier = []
boostbag = []
for name in filenames:  
    if "elasticnet" in name:
        classifier.append("EN")
    elif "knn" in name:
        classifier.append("KNN")
    elif "naive_bayes" in name:
        classifier.append("NB")
    elif "rdforest" in name:
        classifier.append("RF")
    elif "svm" in name:
        classifier.append("SVM")
    elif "xgboost" in name: 
        classifier.append("XGB")
    elif "logreg" in name: 
        classifier.append("LR")
        
    if "bag_finalscore" in name:
        boostbag.append("bag")
    elif "boost_finalscore" in name:
        boostbag.append("boost")
    else:  
        boostbag.append("none")
    
    if "cfs" in name:
        featureselection.append("CFS")
        group.append(1)
    elif "fcbf" in name:
        featureselection.append("FCBF")
        group.append(1)
    elif "lasso" in name:
        featureselection.append("LASSO")
        group.append(1)
    elif "mrmr" in name:
        if len(name.split('_'))==2:
            featureselection.append("MRMR")
        else:
            featureselection.append("MRMR-"+name.split('_')[1])
        group.append(1)
    elif "infogain" in name:
        featureselection.append("IG-"+name.split('_')[1])
        group.append(2)
    elif "reliefF" in name:
        featureselection.append("ReF-"+name.split('_')[1])
        group.append(2)
    elif "variance" in name:
        featureselection.append("Var-"+name.split('_')[1])
        group.append(3)
    elif "prevalence" in name:
        featureselection.append("Prev-"+name.split('_')[1])
        group.append(3)
    elif "jmi" in name:
        if len(name.split('_'))==2:
            featureselection.append("JMI")
        else:
            featureselection.append("JMI-"+name.split('_')[1])
        group.append(1)
    elif "AllFeatures" in name:
        featureselection.append("All")
        group.append(0)
    elif "Genus" in name:
        featureselection.append("Top8Genus")
        group.append(0)
        
df["Feature Selection"] = featureselection
df["Classifier"] = classifier
df["Boost or Bag"] = boostbag
df["group"] = group
df = df[df["Feature Selection"]!="notselected"]
df = df.sort_values(by = 'group').reset_index().drop('index', axis=1)
df.to_csv(path+'/STATS/'+"filenamesorted1.csv", index=False)

none = df[df["Boost or Bag"] == "none"]
result = none.pivot(index = ['group', 'Feature Selection'],columns = 'Classifier', values = 'Accuracy')
result.reset_index(drop=True, inplace=True, level='group')
if not result.empty:
    fig,ax = plt.subplots(figsize=(8,5))
    plt.xlabel("Feature Selection", fontsize = 16)
    plt.ylabel("Classifier", fontsize = 16)
    ax.tick_params(labelsize=14)
    
    # ax.set_title(title, fontsize = 32)
    res = sns.heatmap(result,fmt ='.1%',cmap ='RdYlGn',annot = True,annot_kws={"size": 16},linewidths=0.30,ax=ax )
    cbar = res.collections[0].colorbar
    cbar.ax.yaxis.set_major_formatter(PercentFormatter(1, 1))
    cbar.ax.tick_params(labelsize=14)
    cbar.ax.locator_params(nbins=2, tight=True)
    cbar.ax.autoscale(enable=False)
    plt.tight_layout()
    plt.savefig('heatmap.tiff', dpi=300)
    plt.show()