from joblib import Parallel, delayed
import pandas as pd
import os
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.impute import KNNImputer
from sklearn.impute import SimpleImputer
# import pyreadstat
import data_preprocess as pre
import uni_multiStats as stats 
import scoring as score 
import ranking_subset_run as rsr
# import boost_bag_run as bbg
import stats as st
# import FeatureOrganize as fo

def NormalRun(data, directory_path, datafile, target, classifiers, score_func, kvals, n_seed, splits):    
    target_path = directory_path+'NormalDataAnalysis/'+datafile+"_"+target+"/"

    feature_path = target_path+"features/"
    STATS_path = target_path+"STATS/"
    results_path = target_path+"resultsparallel/"
    data_path = target_path+"dataparallel/"

    if not os.path.exists(feature_path):
        os.makedirs(feature_path)
    if not os.path.exists(STATS_path):
        os.makedirs(STATS_path)
    if not os.path.exists(results_path):
        os.makedirs(results_path)
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    datacopy = data.copy(deep=True)
    datacopy.replace('', np.nan,regex=True, inplace=True)
    datacopy = pre.remove_invalid_data(datacopy, target)

    # stats.baseline(datacopy, target, STATS_path)

    columns_org = datacopy.columns
    [datacopy, continuous] = pre.modify_data(datacopy)
    columns_dummified = datacopy.columns
    n_features = datacopy.shape[1]-1

    runs = stats.runSKFold(n_seed, splits, data=datacopy,target=target, columns_org=columns_org, continuous=continuous, columns_dummified=columns_dummified)

    for c in classifiers:
        for fs in score_func:
            score.score(rsr.normal_run(target_path, columns_dummified.drop([target]), n_seed, splits, fs, c, runs, n_features),n_seed)

def different_k():
    Parallel(n_jobs=-1)(delayed(run_with_k)(k, data, target, ))

def run_with_k():
