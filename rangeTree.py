import matplotlib.pyplot as plt
import numpy as np
import random

from numpy.lib.function_base import median

class rangeTree:

    def __init__(self, data):
        
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



    def rangeTreeDivision(self, subtree=[-1,-1,-1], coordinates = True, depth = 0):

            
        if subtree == [-1,-1,-1]:
            dataList = self.data
        else:
            dataList = subtree

        print(dataList)

        if len(dataList) <= 2:

            return {
                'subtree' : dataList,
                'depth' : depth,
            }

        else:
            pass

        
        leftSubtree,rightSubtree = ([] for i in range(2))

        if coordinates == True:
            currentCoordinate = 0
        else:
            currentCoordinate = 1

        nodeToDivide = dataList[0]
        

        for subtree in dataList:
            pass








data = []

for x in range(10):
    tempList = []
    for y in range(5):
        tempList.append(random.randint(1, 500))
    data.append(tempList)

sampleTree = rangeTree(data)
sampleTree.rangeTreeDivision(data)