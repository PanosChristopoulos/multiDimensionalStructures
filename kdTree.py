import collections
import operator
import sys
import random
from statistics import median




def kdTree(points):

    #check length of points

    length = len(points[0])
    print('Building KD Tree with point length',length)

    for element in points:
        if len(element) != length:
            print('Points of unequal length')
            sys.exit()
    
    print('All points are of equal length')


    dimList = []
    for lengthPoint in range(length):
        dimList.append(lengthPoint)

    treeVisualizationDict = {0:[points]}

    depth = 1
        
    for i in range(depth):

        currentDimension = random.choice(dimList)

        tempList = []
        for element in points:
            tempList.append(element[currentDimension])

        tempListL = []
        tempListR = []

        for item in range(len(tempList)):
            if item>median(tempList):
                tempListR.append(points[item])
            else:
                tempListL.append(points[item])

        #print(tempListL)
        #print(tempListR)
        #print(len(tempListL),len(tempListR))
        treeVisualizationDict[i+1] = [tempListL,tempListR]

    print(treeVisualizationDict)

    


testData = [(2,4,3,7),(3,3,5,4),(2,4,3,2),(5,12,3,9),(7,37,3,2),(24,21,42,1),(23,24,1,5),(42,4,4,1),(3,5,2,4),(72,3,3,89)]

kdTree(testData)
