#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.11 - Evenly Divides the other
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 13, 2022
#
# This program will take two positive integers from the command line and
# print true if one evenly divides the other.
#--------------------------------------------------------------------------

import stdio
import sys

a = int(sys.argv[1])
b = int (sys.argv[2])

stdio.writeln(a % b == 0 or b % a == 0)
