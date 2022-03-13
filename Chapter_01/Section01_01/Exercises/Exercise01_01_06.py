#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.1.6 - Reverse the iput
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 12, 2022
#
# This program will take 3 command line arguments as strings.  Each will
# be a name.  The output will print a greeting with the inputs reversed
#-------------------------------------------------------------------------

import sys
import stdio

stdio.write('Hello ')
stdio.writeln(sys.argv[3])
stdio.write('Hello ')
stdio.writeln(sys.argv[2])
stdio.write('Hello ')
stdio.writeln(sys.argv[1])

