# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:09:14 2017
@author: Montanari, Daniel (dmontanari@gmail.com)
"""

#import quadraticBezier as Bezier

from bezier import quadraticBezier as Bezier

#bezier = Bezier.quadraticBezier(0, 0, 50, 50)
bezier = Bezier.quadraticBezier()

xControl = [0 ,  25, 50]
yControl = [0 ,  75,  0]

bezier.setControlPoints(xControl, yControl)
bezier.setDeltaT(0.002)
bezier.generateBezierCurve()
#bezier.definePointSize(1)

bezier.draw(showGrid = True, showArrows=True)

