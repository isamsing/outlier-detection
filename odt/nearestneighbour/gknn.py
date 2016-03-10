###############################
## Global KNN Implementation ##
###############################

### Import Python Libraries ###
import pandas as pd
from pandas import DataFrame
from numpy import array

### Import R Libraries ###
import rpy2.robjects as R
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
base = importr("base")
utils = importr("utils")
odtpackage = importr("dbscan")


######################
## Global KNN Class ##
######################
class GlobalKNN(object):

    ### Global KNN Class Constructor ###
    def __init__(self, xdf, minPts):
        self.xdf = xdf
        self.minPts = minPts

    ### Global KNN Distance estimation Function ###
    def kNNDistance(self):
        return odtpackage.kNNdist( base.as_matrix(self.xdf), self.minPts)

    ### Global KNN Execution Function ###
    def getOutlier(self, threshold, label= False):
        knn = self.kNNDistance()
        self.distance = knn['distance']
        self.indices = knn['indices']
        self.k = knn['k']

if __name__ == "__main__":
    pass



