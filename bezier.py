# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:36:07 2017

@author: Montanari, Daniel (dmontanari@gmail.com)
"""

from pylab import plot
import matplotlib.pyplot as plt
import numpy as np
from scipy import special

from quadraticBezier import quadraticBezier as quadBezier

class cubicBezier(quadBezier):
    def __init__(self, minX=0, minY=0, maxX=0, maxY=0):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
    
    def generateBezierCurve(self):
        deltaT = np.arange(0, 1, self.tDivisor)
        self.bezierPointsX.clear()
        self.bezierPointsY.clear()
        print('Calculating Bezier points for ', len(self.xControl), ' control points\n')
        for t in deltaT:
            pX, pY = self.__calculateBezierPoints(self.xControl, self.yControl, t)
            self.bezierPointsX.append(pX)
            self.bezierPointsY.append(pY)
        
    def __calculateBezierPoints(self, controlX, controlY, t):
        #
        # Apply the Newton binomial theorem in (x + t) ** (len(controlX)-1)
        # https://en.wikipedia.org/wiki/Binomial_theorem
        #
        x   = (1-t)
        n   = len(controlX)
        pX  = 0
        pY  = 0
        order = n-1
        for i in range(0, n):
            coef = special.binom(order, i)
            expX = (n-i-1)
            expA = i
            pX = pX + coef * x**(expX) * t ** i * controlX[expA]
            pY = pY + coef * x**(expX) * t ** i * controlY[expA]
        return (pX, pY)

    def draw(self, showGrid = False, showArrows = False):
        #fig = plt.figure()
        plt.axis('equal')
        x = [self.maxX, self.minX]
        y = [self.minY, self.maxY]
        [ plot( [dot_x,dot_x] ,[0,dot_y], '-', linewidth = 1, c='k' ) for dot_x,dot_y in zip(x,y) ] 
        [ plot( [0,dot_x] ,[dot_y,dot_y], '-', linewidth = 1, c='k' ) for dot_x,dot_y in zip(x,y) ]
        plt.scatter(self.xControl, self.yControl, c='r')
        plt.scatter(self.bezierPointsX, self.bezierPointsY, c='b', s=self.pointSize)

        if showGrid is True:
            plt.grid()

        if showArrows is True:
            n = len(self.xControl)
            for i in range(0, n-1):
                x1 = self.xControl[i]
                y1 = self.yControl[i]
                x2 = self.xControl[i+1] - x1
                y2 = self.yControl[i+1] - y1
                #print('arrows (', x1, ',', y1,') to (', x2, ',', y2,') \n')
                plt.arrow(x1, y1, x2,  y2, length_includes_head = True, head_width = 1)
        plt.show()

