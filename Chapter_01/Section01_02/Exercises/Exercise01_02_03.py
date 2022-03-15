#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exericse 1.2.3 - Proof of Logical Expression
# Programmer: Joseph Cunningham
# Project: CsC20 - Python
# Date: March 13, 2022
#
# This program will show that the following logical expression is always
# true.
#
#   (not (a and b) and (a or b)) or ((a and b) or not(a or b))
#--------------------------------------------------------------------------
import stdio

expression= lambda a, b:(not (a and b) and (a or b)) or ((a and b) or not(a or b))

# When a = b = False
stdio.writeln("a = b = False")
stdio.writeln("Expression = " + str(expression(False, False)))
stdio.writeln("")

# When a = False and b = True
stdio.writeln("a = False, b = True")
stdio.writeln("Expression = " + str(expression(False, True)))
stdio.writeln("")

# When a = True and b = False
stdio.writeln("a = True, b = False")
stdio.writeln("Expression = " + str(expression(True, False)))
stdio.writeln("")


# When a = True and b = True
stdio.writeln("a = True, b = True")
stdio.writeln("Expression = " + str(expression(True, True)))
stdio.writeln("")

