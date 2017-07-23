#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:09:14 2017
@author: Montanari, Daniel (dmontanari@gmail.com)
"""

#import quadraticBezier as Bezier

from bezier import cubicBezier as Bezier

#bezier = Bezier.quadraticBezier(0, 0, 50, 50)
bezier = Bezier()

xControl = [0 ,  25, 50, 75]
yControl = [0 ,  10, -8, -35]

bezier.setControlPoints(xControl, yControl)
bezier.setDeltaT(0.002)
bezier.generateBezierCurve()
bezier.draw(showGrid = True, showArrows=True)
