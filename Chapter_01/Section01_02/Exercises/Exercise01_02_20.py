#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.20 - This must be the day
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 13, 2022
#
# This program will accept 2 integers from the command line:
#
#     m - month, 1-Jan, 2-Feb ,...etc
#     d - day
#
# It will then output TRUE is the combination is between March 20 and June
# 20 and FALSE otherwise.
#--------------------------------------------------------------------------

import sys, stdio

m = int(sys.argv[1])
d = int(sys.argv[2])

isBetween = (m == 3 and d > 20) or  (m == 6 and d < 20)
isBetween = isBetween or (m > 3 and m < 6)

stdio.writeln(isBetween)
