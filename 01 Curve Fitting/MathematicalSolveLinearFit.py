'''
Created on May 14, 2017

@author: Nate
'''
import math as m
import matplotlib.pyplot as plt
import numpy as np

def productSum(xList, yList):
    i = 0
    sum = 0
    while i < len(xList):
        sum += xList[i] * yList[i]
        i += 1
    return sum

def barOf(list):
    return sum(list) / len(list)

def sampleStandardDeviation(list):
    sum = 0
    xBar = barOf(list)
    for i in list:
        sum += (i - xBar) ** 2
    return m.sqrt(sum / (len(list) - 1))

def squaredBar(list):
    sum = 0
    for i in list:
        sum += i ** 2
    return sum

    
def main():
    xs = np.array([3.0, 5.0, 6.0])
    x = np.arange(0, 10, .1)
    ys = [2.0, 5.0, 5.0]
    xBar = barOf(xs)
    yBar = barOf(ys)
    xYBar = productSum(xs, ys)
    Sx = sampleStandardDeviation(xs)
    Sy = sampleStandardDeviation(ys)
    xSquaredBar = squaredBar(xs)
    ySquaredBar = squaredBar(ys)
    Rxy = (xYBar - xBar * yBar) / m.sqrt((xSquaredBar - xBar ** 2) * (ySquaredBar - yBar ** 2))
    slope = Rxy * Sy / Sx
    intercept = yBar - xBar * Rxy * Sy / Sx
    print("Equation:  f(x) = {0}x + {1}".format(slope, intercept))
    equation = slope * x + intercept
    plt.plot(xs, ys, 'bo')
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.plot(x, equation, color='red', linewidth=1.0)
    plt.show()
main()
