'''
Created on Mar 1, 2017

@author: Nathanael Mathieu, Avi Stein, Kevin McMorrow, Jesse Galganov

A can only pair with U, and only when the U is 2 away from it
U can only pair with A, and only when the A is 2 away from it
C can only pair with G, and only when the G is 2 away from it
G can only pair with C, and only when the C is 2 away from it

'''
import numpy as np
pairs = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
def possibleBasePairs(data):
    i = 0
    n = 0
    possiblePairs = []
    while n < len(data):
        while i < len(data) - 2:
            if data[n] == pairs[data[i + 2]]:
                possiblePairs.append([n, i + 2])
            i += 1
        i = n
        n += 1
    return possiblePairs
def basePairMatrixCreator(possibleBasePairs):
    x = 0
    y = 0
    i = 0
    n = len(possibleBasePairs)
    matrix = np.zeros(shape=(n, n))
    
    while i < n:
        x = possibleBasePairs[i][0]
        y = possibleBasePairs[i][1]
        matrix[x][y] = 1
        i += 1
    return matrix
        
        
data = ('C', 'C', 'C', 'A', 'A', 'A', 'G', 'G', 'G', 'U', 'C', 'A')
#        0    1    2    3    4    5    6    7    8    9    10   11

pairs = basePairMatrixCreator(possibleBasePairs(data))
# print(pairs)
# print("Pairs Matrix:")
# print(np.matrix(basePairMatrixCreator(pairs)))

paths = []
ones = []

# for i in range(0,len(bluh)):
#     for j in range(0, len(bluh)):
#         if bluh[i,j] != 0:
#             ones.append((i,j))
#
# twos = [[] for i in range(0,len(ones))]
#
# for i in range(0, len(ones)):
#     (x,y) = ones[i]
#     for j in range(x-1, -1, -1):
#         for k in range(y+1, len(bluh)):
#             tup = (j,k)
#             (twos[i]).append(tup)
#             paths.append([ones[i], tup])

def rabbithole(matrix):
    global paths
    maxList = []
    ones = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            # print(matrix[i][j])
            if matrix[i][j] != 0:
                ones.append([(i, j)])
                paths.append([(i, j)])
    # print(len(ones), ones)
    prev_list = list(ones)
    while prev_list != []:
        new_list = []
        for i in range(0, len(prev_list)):
            place = prev_list[i]
            (x, y) = place[len(place) - 1]
            for j in range(x - 1, -1, -1):
                for k in range(y + 1, len(matrix)):
                    hold = list(place)
                    hold.append((j, k))
                    new_list.append(hold)
                    paths.append(hold)
        # print(len(new_list), new_list)
        prev_list = new_list  
    for i in range(0, len(paths)):
        score = 0
        maxScore = 0
        temp = paths[i]
        for base in temp:
            if data[base[0]] == 'G' or data[base[0]] == 'C':
                score += 3
            else:
                score += 2
        if maxScore < score:
            maxList = paths[i]
            maxScore = score
    return [maxList, score]
maxList = rabbithole(pairs)
    

print("Max Pairs List {}\nWith Score Of: {}".format(maxList[0], maxList[1]))



# bottom
