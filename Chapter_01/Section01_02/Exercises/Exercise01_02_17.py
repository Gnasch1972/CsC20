#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.17 - Die roll
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 13, 2022
#
# This program will output two random number between 1 and 6
#--------------------------------------------------------------------------

import stdio, random

stdio.writeln('Die 1 = ' + str(random.randrange(1,7)))
stdio.writeln('Die 2 = ' + str(random.randrange(1,7)))
