import matplotlib.pyplot as plt
import numpy as np
import random

from numpy.lib.function_base import median

class rangeTree:

    def __init__(self,data):

        self.data = data

    def dataVisualization(self):

        max = np.max(self.data, axis=1).tolist()
        min = np.min(self.data, axis=1).tolist()

        plt.scatter(max, min, marker='x')

        dataList = []

        for item in range(len(max)):
            dataList.append([max[item],min[item]])

        return dataList

    def insertPoint(self,point):

        treeData = self.data
        treeData.append(point)

        return treeData


    def rangeTreeDivision(self, dataList, coordinates = True, depth = 0):
        
        parentSubtree = dataList

        if len(pare)




data = []

for x in range(10):
    tempList = []
    for y in range(5):
        tempList.append(random.randint(1, 500))
    data.append(tempList)

sampleTree = rangeTree(data)
sampleTree.rangeTreeDivision()