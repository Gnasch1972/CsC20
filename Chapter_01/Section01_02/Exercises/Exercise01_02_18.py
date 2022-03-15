#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.18 - Sin and Cos values
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 13, 2022
#
# This program will take a float number from the command line in radians,
# calculate and output:
#
#     sin(2t) + sin(3t)
#--------------------------------------------------------------------------

import math, stdio, sys

t = float(sys.argv[1])

fX = math.sin(2 * t) + math.sin(3 * t)

stdio.writeln('f(' + str(t) +') = ' + str(fX))
