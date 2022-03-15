#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.16 - Random number generator
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
#
# This program accepts to positive integers from the command line.  It will
# then output a random integer between those two numbers
#--------------------------------------------------------------------------

import sys, random, stdio

a = int(sys.argv[1])
b = int(sys.argv[2])

stdio.writeln('Number = ' + str(random.randrange(a, b)))
