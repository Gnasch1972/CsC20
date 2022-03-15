#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.12 - Greater than the sum of two others
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 13, 2022
#
# This program will take 3 postive integers from the command line.  It will
# then print False if any one of the integers is greater than the sum of
# the other two and True otherwise.
#--------------------------------------------------------------------------

import sys, stdio

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

sumBC = b + c
sumCA = c + a
sumAB = a + b

logicalA = a < sumBC
logicalB = b < sumCA
logicalC = c < sumAB

stdio.writeln(logicalA and logicalB and logicalC)
