###############################################
## Local Outlier Factor (LOF) Implementation ##
###############################################

### Import Python Libraries ###
import pandas as pd
from pandas import DataFrame
from numpy import array, matrix

### Import R Libraries ###
import rpy2.robjects as R
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
pandas2ri.activate()
base = importr("base")
utils = importr("utils")
odtpackage = importr("dbscan")


######################
## Global LOF Class ##
######################
class DBSCAN(object):

    ### Global LOF Class Constructor ###
    def __init__(self, xdf, epsilon, minPts):
        self.xdf = xdf
        self.epsilon = epsilon
        self.minPts = minPts
        self.label = []
        self.cluster = []

    ### [TODO:] Implement Nromalization functionality ###
    def normalizeData(self):
        pass

    ### DBSCAN clustering estimation Function ###
    def DBSCAN(self, xdf):
        if len(xdf) > 100000:
            print "Warning! DBSCAN might fail for large dataset."

        rdf = pandas2ri.py2ri(xdf)
        return odtpackage.dbscan(base.as_matrix(rdf), self.epsilon, self.minPts)

    ### DBSCAN Execution Function ###
    def getOutlier(self):
        cls = self.DBSCAN(self.xdf)
        print cls
        for i in array(cls.rx2('cluster')):
            self.cluster.append(i)
            if i == 0:
                self.label.append('outlier')
            else:
                self.label.append('normal')

        return DataFrame({'Cluster': self.cluster, 'Label': self.label})


if __name__ == "__main__":
    url = '/Users/warchief/Documents/Projects/DataRepository/AnomalyDetection/test.csv'
    df = DataFrame.from_csv(path=url, header=0, sep=',', index_col=False)

    X = df['SL_RRC_CONN_AVG_PER_CELL'].values
    Y = df['I_DL_DRB_CELL_TPUT_MBPS'].values

    d = {'x': X, 'y': Y}
    pdf = DataFrame(data=d)
    db = DBSCAN(pdf, 0.5, 50)
    print db.getOutlier()





