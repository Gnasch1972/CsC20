#!/usr/bin/env python3
#-------------------------------------------------------------------------
# Program: Exercise 1.2.2 - Euler Equation Equality
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 12, 2022
#
# This program will take a command line argument for theta in radians.  It
# will then see if the following equality holds:
#
#     cos^2(theta) + sin^2(theta) == 1
#--------------------------------------------------------------------------
import sys
import math
import stdio

theta = float(sys.argv[1])

cosSquared = (math.cos(theta)) ** 2
sinSquared = (math.sin(theta)) ** 2
total = cosSquared + sinSquared

stdio.writeln(str(cosSquared) + '+' + str(sinSquared) + '==' + str(1))
stdio.writeln(total)

