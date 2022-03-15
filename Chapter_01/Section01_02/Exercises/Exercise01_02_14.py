#!/usr/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.14 - Force of gravity
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 13, 2022
#
# This program corrects the students mistakes:
#--------------------------------------------------------------------------

import stdio

GRAVITY = 6.673E-11   # gravitational constant Nm^2/kg^2
m1 = 68               # mass of human in kg
m2 = 5.98E24          # mass of the earth
r = 6.38E6             # distance from center of earth of center of human

forceStudent = GRAVITY * m1 * m2 / r * r
forceCorrect  = (GRAVITY * m1 * m2) / r**2

stdio.writeln('Student force = ' + str(forceStudent))
stdio.writeln('Correct force = ' + str(forceCorrect))


