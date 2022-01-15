import matplotlib.pyplot as plt
import numpy as np
import random

from numpy.lib.function_base import median
import sys
sys.setrecursionlimit(10000)




QTREE_VARIABLE = 4

class rTree:

    def __init__(self,data):
        self.initialData = data

        max = np.max(self.initialData, axis=1).tolist()
        min = np.min(self.initialData, axis=1).tolist()

        plt.scatter(max, min, marker='x')
        #plt.show()

        dataList = []

        for item in range(len(max)):
            dataList.append([max[item],min[item]])

        self.data = dataList
        self.depth = 0

    def rTreeDivision(self,dataList,depth=0):

        parentSubtree = dataList
        
        if len(dataList) <= QTREE_VARIABLE:

            return {
                'subtree' : dataList,
                'depth' : depth
            }

        else:
            pass