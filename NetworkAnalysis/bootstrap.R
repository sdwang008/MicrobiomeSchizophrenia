source("SingleNetwork.R")
library(parallel)
library(MASS)

createNetwork <- function(i) {
  healthy=SingleNetwork(F=paste(paste("df0clrs/df0_clr",toString(i), sep=""),".csv", sep=""))
  result = healthy$PCorBootOmega
  write.csv(result, paste(paste("df0PCors/df0_PCor",toString(i), sep=""),".csv", sep=""))
  
  schizo=SingleNetwork(F=paste(paste("df1clrs/df1_clr",toString(i), sep=""),".csv", sep=""))
  result = schizo$PCorBootOmega
  write.csv(result, paste(paste("df1PCors/df1_PCor",toString(i), sep=""),".csv", sep=""))
}

mclapply(0:99, createNetwork, mc.cores = 32)
