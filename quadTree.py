import matplotlib.pyplot as plt
import numpy as np
import random

from numpy.lib.function_base import median
import sys
sys.setrecursionlimit(10000)




QTREE_VARIABLE = 4



class quadTree:


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
    
    

    def quadTreeSubdivision(self,dataList,depth = 0):

        parentSubtree = dataList

        if len(dataList) <= QTREE_VARIABLE:
            
            return {
                    'subtree' : dataList,
                    'depth' : depth,
                }

        else:
            pass


        x1,x2,x3,x4 = ([] for i in range(4))

        
        medianWidth = (min(x[0] for x in dataList)+max(x[0] for x in dataList))
        medianHeight = (min(x[1] for x in dataList)+max(x[1] for x in dataList))


        for item in dataList:

            if item[0] > medianWidth/2 and item[1] > medianHeight/2:
                x1.append(item)
            elif item[0] > medianWidth/2 and item[1] < medianHeight/2:
                x2.append(item)
            elif item[0] < medianWidth/2 and item[1] < medianHeight/2:
                x3.append(item)
            else:
                x4.append(item)

        

        for subtree in [x1,x2,x3,x4]:
            depth = depth+1
            treeVisualizationList.append(self.quadTreeSubdivision(subtree,depth))

        return treeVisualizationList
        
    def findNearestNeighbors(self,point):

        nearestNeighbors = []

        initialData = self.initialData
        treeData = self.initialData
        treeData.append(point)

        sampleTree__ = quadTree(treeData)

        treeData = sampleTree__.data
        

        treeQueryData = self.quadTreeSubdivision(treeData)

        for subtree in range(len(treeQueryData)):
            try:
                for x in treeQueryData[subtree]['subtree']:
                    if x == treeData[-1]:

                        for x in treeQueryData[subtree]['subtree']:
                            if x != treeData[-1]:
                                nearestNeighbors.append(x)
                        
                        for neighborCounter in range(3):

                            if not nearestNeighbors:
                                for x in treeQueryData[subtree-neighborCounter]['subtree']:
                                    if x != treeData[-1]:
                                        nearestNeighbors.append(x)


                                for x in treeQueryData[subtree+neighborCounter]['subtree']:
                                    if x != treeData[-1]:
                                        nearestNeighbors.append(x)

                                for x in treeQueryData[neighborCounter]['subtree']:
                                    if x != treeData[-1]:
                                        nearestNeighbors.append(x)

                                                
            except:
                pass
        
        nearestNeighborsList = []

        for item in nearestNeighbors:
            nearestNeighborsList.append(initialData[treeData.index(item)])

        return nearestNeighborsList


        


            

                
counter = 0


for x in range(120):
    

    data = []

    for x in range(100):
        tempList = []
        for y in range(5):
            tempList.append(random.randint(1, 500))
        data.append(tempList)

    treeVisualizationList = []
    sampleTree = quadTree(data)
    nearestNeighbors = sampleTree.findNearestNeighbors([400,105,105,435,125])
        
    if bool(nearestNeighbors) == False:        
        counter+=1
    else:
        pass

print(nearestNeighbors)