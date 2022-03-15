#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.15
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 13, 2022
#
# This program will calculate the distance between a point and the origin
#--------------------------------------------------------------------------

import stdio, math, sys

x = float(sys.argv[1])
y = float(sys.argv[2])

distance = math.sqrt(x**2 + y**2)

stdio.writeln('Distance is ' + str(distance))
