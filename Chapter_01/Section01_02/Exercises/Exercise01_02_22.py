#!/usr/bin/env python3
#---------------------------------------------------------------------
# Program: Exercise 1.2.22 - Wind Chill
# Programmer: Joseph Cunningham
# Project: CsC 15 - Python
# Date: March 14, 2022
#
# This program will take 2 float command line arguments:
#
#       v = wind speed (miles per hour) float
#       t = temperatue (Fahrnheit) float
#
# It will calcualte the effective temperature (wind chill) using:
#
#       w = 35.74 + 0.6215t + (0.4275t -35.75) v^0.16
#
# for:
#
#       |t| > 50
#       3 < v < 120
#---------------------------------------------------------------------

import sys, stdio

t = float(sys.argv[1])
v = float(sys.argv[2])

w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v**(0.16)

stdio.writeln('Wind chill = ' + str(w))

