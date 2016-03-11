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
## Global KNN Class ##
######################
class GlobalKNN(object):

    ### Global KNN Class Constructor ###
    def __init__(self, xdf, minPts):
        self.xdf = xdf
        self.minPts = minPts
        self.score = []
        self.label = []

    ### [TODO:] Implement Nromalization functionality ###
    def normalizeData(self):
        pass

    ### Global KNN Distance estimation Function ###
    def kNNDistance(self, xdf):
        rdf = pandas2ri.py2ri(xdf)
        return odtpackage.kNNdist(base.as_matrix(rdf), self.minPts)

    ### Global KNN Execution Function ###
    def getOutlier(self, threshold=0.5, label=False):
        distance = array(self.kNNDistance(self.xdf))
        for i in range(0, len(distance)):
            self.score.append(reduce(lambda x, y: x+y, list(distance[i]))/self.minPts)
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
    nn = GlobalKNN(pdf, 200)
    print nn.getOutlier(0.5)





