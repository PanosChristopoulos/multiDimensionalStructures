import matplotlib.pyplot as plt
import numpy as np
import random

from numpy.lib.function_base import median


QTREE_VARIABLE = 4

data = []

for x in range(80):
    tempList = []
    for y in range(3):
        tempList.append(random.randint(1, 100))
    data.append(tempList)

treeVisualizationList = []


class quadTree:


    def __init__(self, data):
        self.data = data

        max = np.max(self.data, axis=1).tolist()
        min = np.min(self.data, axis=1).tolist()

        plt.scatter(max, min, marker='x')
        plt.show()

        dataList = []

        for item in range(len(max)):
            dataList.append([max[item],min[item]])

        self.dataList = dataList
        self.depth = 0
    
    

    def quadTreeSubdivision(self,dataList,depth = 0):

        parentSubtree = dataList

        if len(dataList) <= QTREE_VARIABLE:
            
            return {
                    'subtree' : dataList,
                    'parent_subtree': parentSubtree,
                    'depth' : depth,
                }

        x1,x2,x3,x4 = ([] for i in range(4))

        
        medianWidth = (min(x[0] for x in dataList)+max(x[0] for x in dataList))
        medianHeight = (min(x[1] for x in dataList)+max(x[1] for x in dataList))


        for item in dataList:
            if item[0] > medianWidth/2 and item[1] > medianHeight/2:
                x1.append(item)
            if item[0] > medianWidth/2 and item[1] < medianHeight/2:
                x2.append(item)
            if item[0] < medianWidth/2 and item[1] < medianHeight/2:
                x3.append(item)
            if item[0] < medianWidth/2 and item[1] > medianHeight/2:
                x4.append(item)

        

        for subtree in [x1,x2,x3,x4]:
            depth = depth+1
            treeVisualizationList.append(self.quadTreeSubdivision(subtree,depth))

        return treeVisualizationList
        
        
            

                


sampleTree = quadTree(data)
print(sampleTree.quadTreeSubdivision(data))





