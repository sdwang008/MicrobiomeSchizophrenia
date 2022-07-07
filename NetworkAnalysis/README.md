# Network Analysis

The network analysis procedures are similar to [Loftus et al. (2021)](https://www.nature.com/articles/s41598-021-82449-0#Sec9). 

```cd``` into this folder to proceed. 

## Network Construction, Analysis and Visualization
We construct two networks for the healthy and schizophrenic groups. [network0.ipynb](network0.ipynb) is used for some preliminary findings (determining prevalence distribution). 

Run through [network1.ipynb](network1.ipynb) to clean up healthy and schizophrenic feature tables. The resulting output should be healthy_clr.csv and schizo_clr.csv

Then, run [ConstructNetwork.Rmd](ConstructNetwork.Rmd) to get the adjacency matrices (healthy_PCor.csv and schizo_Pcor.csv). 

Finally, run through [network2.ipynb](network2.ipynb) for network property analysis and visualization. 

## Bootstrap Network Comparison
To determine the statistical significance of network properties between healthy and schizophrenic subjects, we used bootstrapping to create 100 healthy and schizophrenic networks each, and compared their average property measures using t-test. 

Run through [bootstrap1.ipynb](bootstrap1.ipynb) to generate clr-transformed tables (stored in df0clrs and df1clrs folders).

Then, run [bootstrap.R](bootstrap.R) (with a cluster) or bootstrap.Rmd to generate 100 partial correlation matrices each. 

Finally, run through [bootstrap2.ipynb](bootstrap2.ipynb) to obtain the results. 