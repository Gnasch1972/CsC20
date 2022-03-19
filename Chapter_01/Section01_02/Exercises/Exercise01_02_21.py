#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.21 - Continuously Compounded Interest
# Programmer: Joseph Cunningham
# Project: CsC 15 - Python
# Date: March 14, 2021
#
# This program will take 3 command line arguments:
#
#       t - number of years - float
#       p - principle of the loan - float
#       r - annual interest rates - float
#
# It will then calculate the future value of the load.
#--------------------------------------------------------------------------

import stdio, sys, math

t = float(sys.argv[1])
p = float(sys.argv[2])
r = float(sys.argv[3])

fV = p * math.exp(r * t)

stdio.writeln('$' + str(fV))
