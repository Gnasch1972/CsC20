#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.13 - Explain the output
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 13, 2022
#---------------------------------------------------------------------------

import stdio

# Part 1
a = 1
stdio.writeln('a = ' + str(a))
a = a + a
stdio.writeln('a = ' + str(a))
a = a + a
stdio.writeln('a = ' + str(a))
a = a + a
stdio.writeln('a = ' + str(a))

# Part 2
a = True
stdio.writeln('a = ' + str(a))
a = not a
stdio.writeln('a = ' + str(a))
a = not a
stdio.writeln('a = ' + str(a))
a = not a
stdio.writeln('a = ' + str(a))

# Part 4
a = 2
stdio.writeln('a = ' + str(a))
a = a * a
stdio.writeln('a = ' + str(a))
a = a * a
stdio.writeln('a = ' + str(a))
a = a * a
stdio.writeln('a = ' + str(a))
