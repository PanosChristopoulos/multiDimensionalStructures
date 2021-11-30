import math
import collections
import operator
import sys
import random
from statistics import median


def distance(point1,point2):

    if len(point1) == len(point2):
        tempDistanceAxes = []
        squaresSum = 0

        for x in range(len(point1)):
            tempDistanceAxes.append(point1[x]-point2[x])

        for item in tempDistanceAxes:
            squaresSum+=item*item

        return math.sqrt(squaresSum)

    else:

        print("Points",point1,point2,"of unequal length")
        
def closestNeighbor(pointsData, newPoint):
    closestPoint = None
    minDistance = None

    for point in pointsData:
        currentDistance = distance(newPoint, point)

        if minDistance == None or currentDistance < minDistance:
            minDistance = currentDistance
            closestPoint = point

    print(closestPoint)
    print(minDistance)



preset =  3


def checkLength(pointsData):
    individualLength = len(pointsData[0])
    

    for element in pointsData:
        if len(element) != individualLength:
            print('Points of unequal length')
            sys.exit()
    
    print('All points are of equal length')
    print('Building KD Tree with point length',individualLength)


def kdTree(pointsData, depth=0):

    length_ = len(pointsData)

    if length_ <= 0:
        return None
    
    axis = depth % preset

    sortedPoints = sorted(pointsData, key=lambda point: point[axis])


    tempLength = int(length_/2)
    return {
        'depth' : depth+1,
        'point': sortedPoints[tempLength],
        'left_tree': kdTree(sortedPoints[:tempLength], depth+1),
        'right_tree' : kdTree(sortedPoints[tempLength +1:], depth+1)
    }   
    



testData = [(2,4,3,7),(3,3,5,4),(3,3,5,4),(2,4,3,2),(5,12,3,9),(7,37,3,2),(24,21,42,1),(23,24,1,5),(42,4,4,1),(3,5,2,4),(72,3,3,89)]
checkLength(testData)
print(kdTree(testData))
