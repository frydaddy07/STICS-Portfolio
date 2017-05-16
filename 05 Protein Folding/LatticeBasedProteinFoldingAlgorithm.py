'''
Created on Mar 8, 2017
Last Modification on May 1, 2017

This program

@author: Nathanael Mathieu, Avi Stein, Kevin McMorrow, Jesse Galganov
'''
import numpy as np
import pylab as pl
import math

a = np.zeros((9, 9), dtype=int)  # create a 10x10 matrix -- max size needed is 2*n where n = bead number

# first entry is at origin of matrix - (over n, up n)
a[4, 4] = 1

def test_m(n):  # n = number of beads
    matrix = np.zeros((2 * n, 2 * n), dtype=int)  # initial matrix 
    i = 0
    score = 0
    return(score, matrix)


 
test_array = np.zeros((10, 10), dtype=int)  # score should be +1 at the row = 1 columns 1->2 
test_array[0, 0] = 1
test_array[0, 1] = 2
test_array[1, 1] = 3
test_array[2, 1] = 4
test_array[2, 2] = 5
test_array[1, 2] = 6
test_array




# check every row, increase count if x != 0, x-1, or x+1, then check every column 
import numpy as np
from numpy import matrix
data = [[ 1., 2., 0., 0.],
        [ 0., 3., 0., 0.],
        [ 0., 4., 5., 0.],
        [ 0., 7., 6., 0.]]

newData = np.fliplr(data)

'''print("data:", data)
print("reversed data:",newData)'''
n = 0
i = 0
score = 0

bestScore = -1
bestMatrix = [0]
def bestFold(matrixOfPoints, score):  # requires variables bestScore, bestMatrix
    if score > bestScore:
        bestScore = score
        bestMatrix = matrixOfPoints
    return

def scoreThis(data):
    for n in range(0, len(data) - 1):
        score = 0
        for i in range(0, len(data[n])):
            if data[n][i] != 0:
                val = data[n][i]
                below = data[n + 1][i]
                beside = data[n][i + 1]
                if below != 0 and (val - 1 > below or val + 1 < below):
                    score = +1
                elif beside != 0 and (val - 1 > beside or val + 1 < beside):
                    score = +1
    return score
print(scoreThis(data))
