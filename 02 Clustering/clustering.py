'''
Created on May 15, 2017

@author: Nate
'''
import numpy as np
import matplotlib.pyplot as plt
import random

def barOf(list):
    return sum(list) / len(list)

def sampleStandardDeviation(list):
    sum = 0
    xBar = barOf(list)
    for i in list:
        sum += (i - xBar) ** 2
    return np.sqrt(sum / (len(list) - 1))

def pickInitialCentroids(xs, ys, k):
    clusters = []
    x = xs
    y = ys
    randomNums = random.sample(range(0, len(x)), k)
    for n in range(0, k):
        clusters.append([x[randomNums[n]], y[randomNums[n]]])
    return clusters

def calculateDistances(centroids, x, y, k):  # works
    distanceFromCentroids = [[] for _ in range(len(x))]
    # print('begin calc distances')
    # calculate the distance from centroids and the datapoints
    for n in range(0, len(x)):
        for i in range(0, k):
            distanceFromCentroids[n].append(np.sqrt(np.power(centroids[i][0] - x[n], 2) + np.power(centroids[i][0] - y[n], 2)))
    return distanceFromCentroids

def assignPoints(xData, yData, k, distanceFromCentroids):  # works
    # print('begin assign points')
    # assign points to closest centroid
    clusterID = []
    clusterNum = -1
    for n in range(0, len(distanceFromCentroids)):
        least = float('inf')
        for i in range(0, len(distanceFromCentroids[n])):
            if distanceFromCentroids[n][i] < least:
                least = distanceFromCentroids[n][i]
                clusterNum = i
        clusterID.append(clusterNum)
    # print(clusterID)
    return clusterID

def recalculateCentroids(xData, yData, clusterID, k):  # works
    # print('begin recalc centroids')

    centroids = []
    for n in range(0, k):
        sumX = 0.0
        sumY = 0.0
        num = 0
        for i in range(0, len(xData)):
            if clusterID[i] == n:
                sumX += xData[i]
                sumY += yData[i]
                num += 1
        print("sumX: {0}  sumY: {1}  number: {2}".format(sumX, sumY, num))
        if num == 0:
            point = random.randint(0, len(xData) - 1)
            centroids.append([xData[point], yData[point]])
        else:
            centroids.append([sumX / num, sumY / num])
    # print(newCentroids)
    
                
    return centroids

def mergeCentroids(xData, yData, clusterID, centroids):
    badClusters = []
    ssd = (sampleStandardDeviation(xData) + sampleStandardDeviation(yData)) / 2
    print(ssd)
    for n in range(0, len(centroids) - 1):
        for i in range(n, len(centroids[0])):
            if np.sqrt((centroids[n][0] - centroids[i][0]) ** 2 + (centroids[n][1] - centroids[i][1]) ** 2) < ssd: 
                badClusters.append([n])
                badClusters.append([i])
    for n in range(0, len(xData)):
        for clusterNum in range(0, len(badClusters)): 
            if clusterID[n] == badClusters[clusterNum] or clusterID[n] == badClusters[clusterNum]:
                clusterID[n] = badClusters[0]
    return clusterID

def shouldStop(old, new, iterations):
    if iterations >= 1000:
        return True
    return old == new

def main():
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    xData = (1, 1, 2, 2, 7, 8, 7, 9, 10, 15, 16, 15, 17, 0, 1, 1, 0, 1)
    yData = (0, 1, 2, 1, 9, 7, 8, 9, 8, 15, 16, 16, 15, 10, 12, 10, 11, 12)
    
    # necessary variables
    k = 4
    lastRun = []
    i = 0
    print("Number of points= {}".format(len(xData)))
    newCentroids = pickInitialCentroids(xData, yData, k)
    print("centroids: {}".format(newCentroids))
    while not shouldStop(lastRun, newCentroids, i):
        i += 1
        lastRun = newCentroids
        print("Run {}:".format(i))
        distances = calculateDistances(newCentroids, xData, yData, k)
        print("distances: {}".format(distances))
        
        clusterids = assignPoints(xData, yData, k, distances)  
        #clusterids = mergeCentroids(xData, yData, clusterids, newCentroids)
        print("clusterids: {}".format(clusterids))
        
        newCentroids = recalculateCentroids(xData, yData, clusterids, k)
        print("newCentroids: {}".format(newCentroids))
        
        
        for n in range(0, len(newCentroids)):
            plt.scatter(newCentroids[n][0], newCentroids[n][1], c=colors[i % len(colors)])        
        for n in range(0, len(clusterids)):
            print("point: [{},{}]  id: {}  centroid location: {} distances: {}".format(xData[n], yData[n], clusterids[n], newCentroids[clusterids[n]], distances[n]))
            
        plt.scatter(xData, yData, marker='+')
        plt.axis([-1, 20, -1, 20])
        plt.show()  # data works, two distinct clusters
main()
