#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.1 - Number trace
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 12, 2022
#
# Trace the variables!
#--------------------------------------------------------------------------

import stdio

a = 1
b = 2

stdio.writeln("Before swap")
stdio.writeln('a = ' + str(a))
stdio.writeln('b = ' + str(b))

t = a
b = t
a = b

stdio.writeln("After swap")
stdio.writeln('a = ' + str(a))
stdio.writeln('b = ' + str(b))

