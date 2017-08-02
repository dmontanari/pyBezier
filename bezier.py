# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:36:07 2017

@author: Montanari, Daniel (dmontanari@gmail.com)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import special

class BezierCurve():
    """
    BezierCurve
    -----------
    Provides:
        * Calculation of S-PLine points
        * Draw the curve
    
    Example
    -------
    >>> from bezier import BezierCurve as Bezier
    >>> bezier = Bezier()
    >>> xControl = [0 ,  25, 50, 75]
    >>> yControl = [0 ,  10, -8, -35]
    >>> bezier.setControlPoints(xControl, yControl)
    >>> bezier.setDeltaT(0.002)
    >>> bezier.generateBezierCurve()
    >>> bezier.draw(showGrid = True, showArrows=True)
     
    Wikipedia
    ---------
    https://en.wikipedia.org/wiki/B%C3%A9zier_curve

    """
    tDivisor        = 0.1
    bezierPointsX   = list()
    bezierPointsY   = list()
    pointSize       = 0.2
    minX            = 0
    minY            = 0
    maxX            = 0
    maxY            = 0
    def __init__(self, minX=0, minY=0, maxX=0, maxY=0):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
    
    def setControlPoints(self, controlX, controlY):
        """
        Define the control points
        
        Parameters:
        -----------
            controlX : Array with X coordinate for the control points
            
            controlY : Array with Y coordinate for the control points
       
        
        Examples
        ---------
            >>> xControl = [0 ,  25, 50, 75]
            >>> yControl = [0 ,  10, -8, -35]
            >>> bezier.setControlPoints(xControl, yControl)
        """
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

    def getSPlinePoints(self):
        return (self.bezierPointsX, self.bezierPointsY)
    
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

    def definePointSize(self, pSize):
        self.pointSize = pSize


    def draw(self, showGrid = False, showArrows = False):
        #fig = plt.figure()
        plt.axis('equal')
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
                plt.arrow(x1, y1, x2,  y2, length_includes_head = True, head_width = len(self.xControl)-2)
        plt.show()

