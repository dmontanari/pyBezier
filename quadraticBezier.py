# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 17:05:07 2017

@author: Montanari, Daniel (dmontanari@gmail.com)
"""

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

class quadraticBezier:
    
    tDivisor = 0.1
    bezierPointsX = list()
    bezierPointsY = list()
    pointSize = 0.2
    minX = 0
    minY = 0
    maxX = 0
    maxY = 0
    def __init__(self, minX=0, minY=0, maxX=0, maxY=0):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
    
    def setControlPoints(self, controlX, controlY):
        self.xControl = controlX
        self.yControl = controlY
        for x in controlX:
            if (x > self.maxX):
                self.maxX
            if ( x < self.minX):
                self.minX = x;
        for y in controlY:
            if (y > self.maxY):
                self.maxY = y;
            if (y < self.minY):
                self.minY = y;
    
    def setDeltaT(self, tDivisor):
        self.tDivisor = tDivisor
    
    def generateBezierCurve(self):
        deltaT = np.arange(0, 1, self.tDivisor)
        deltaT = np.arange(0, 1, self.tDivisor)
        deltaT.resize(len(deltaT) + 1)
        deltaT[-1] = 1
        self.bezierPointsX.clear()
        self.bezierPointsY.clear()
        for d in deltaT:
            pX, pY = self.__calculateQuadraticBezier(self.xControl, self.yControl, d)
            self.bezierPointsX.append(pX)
            self.bezierPointsY.append(pY)

    def definePointSize(self, pSize):
        self.pointSize = pSize

    def __calculateQuadraticBezier(self, controlX, controlY, t):
        # Calculate point X and Y for current t
        pX = ((1-t)**2) *controlX[0] + 2*t*(1-t)* controlX[1] + t**2*controlX[2]
        pY = ((1-t)**2) *controlY[0] + 2*t*(1-t)* controlY[1] + t**2*controlY[2]
        
        return (pX, pY)
 
    def draw(self, showGrid = False, showArrows = False):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.axis('equal')
        # Define the cartesian space
        x = [self.maxX, self.minX]
        y = [self.minY, self.maxY]
        [ plot( [dot_x,dot_x] ,[0,dot_y], '-', linewidth = 1, c='k' ) for dot_x,dot_y in zip(x,y) ] 
        [ plot( [0,dot_x] ,[dot_y,dot_y], '-', linewidth = 1, c='k' ) for dot_x,dot_y in zip(x,y) ]
        scatter(self.xControl, self.yControl, c='r')
        scatter(self.bezierPointsX, self.bezierPointsY, c='b', s=self.pointSize)

        if showGrid is True:
            grid()
        
        if showArrows is True:
            arrow(  self.xControl[0],  self.yControl[0],  self.xControl[1]-self.xControl[0],  self.yControl[1]-self.yControl[0], length_includes_head = True, head_width = 0.30)
            arrow(  self.xControl[1],  self.yControl[1],  self.xControl[2]-self.xControl[1],  self.yControl[2]-self.yControl[1], length_includes_head = True, head_width = 0.30)
        
        show()

        

