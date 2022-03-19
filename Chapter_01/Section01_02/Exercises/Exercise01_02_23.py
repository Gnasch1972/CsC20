#!/usr/bin/env python3
#---------------------------------------------------------------------
# Program: Exercise 1.2.23 - Polar Coordinates
# Programmer: Joseph Cunningham
# Project: CsC 15 - Python
# Date: March 14, 2022
#
# This program will accept 2 command line arguments:
#
#   x = x coordinate
#   y = y coordinate
#
# It will calculate the polar coordiantes:
#
#     r = sqrt(x^2 + y^2)
#     theta = atan2(y, x)  -pi < theta < pi
#---------------------------------------------------------------------

import sys, stdio, math

x = float(sys.argv[1])
y = float(sys.argv[2])

r = math.sqrt(x**2 + y**2)
theta = math.atan2(y, x)

stdio.writeln('(' + str(r) + ',' + str(theta) + ')')
