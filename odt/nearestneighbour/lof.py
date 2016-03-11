###############################
## Global KNN Implementation ##
###############################

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
class LOF(object):

    ### Global LOF Class Constructor ###
    def __init__(self, xdf, minPts):
        self.xdf = xdf
        self.minPts = minPts
        self.score = []
        self.label = []

    ### [TODO:] Implement Nromalization functionality ###
    def normalizeData(self):
        pass

    ### Global LOF Distance estimation Function ###
    def LOF(self, xdf):
        rdf = pandas2ri.py2ri(xdf)
        return odtpackage.lof(base.as_matrix(rdf), self.minPts)

    ### Global KNN Execution Function ###
    def getOutlier(self, threshold=1):
        lof = array(self.LOF(self.xdf))
        for i in range(0, len(lof)):
            self.score.append(lof[i])
            if self.score[i] > threshold:
                self.label.append('outlier')
            else:
                self.label.append('normal')

        return DataFrame(data={'Score': self.score, 'Label': self.label}, )


if __name__ == "__main__":
    url = '/Users/warchief/Documents/Projects/DataRepository/AnomalyDetection/test.csv'
    df = DataFrame.from_csv(path=url, header=0, sep=',', index_col=False)

    X = df['SL_RRC_CONN_AVG_PER_CELL'].values
    Y = df['I_DL_DRB_CELL_TPUT_MBPS'].values

    d = {'x': X, 'y': Y}
    pdf = DataFrame(data=d)
    lf = LOF(pdf, 200)
    print lf.getOutlier()





