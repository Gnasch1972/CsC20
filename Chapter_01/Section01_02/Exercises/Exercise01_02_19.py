#!/use/bin/env python3
#--------------------------------------------------------------------------
# Program: Exercise 1.2.19 - Projectile motion
# Programmer: Joseph Cunningham
# Project: CsC 20 - Python
# Date: March 13, 2022
#
# This program will take 3 float from the command line:
#
#   xo - initial postion (m)
#   vo - initial velocity (m/s)
#    t - the time elapsed (s)
#
# It will calcualte the diplacement in meters
#--------------------------------------------------------------------------

import sys, stdio

xo = float(sys.argv[1])
vo = float(sys.argv[2])
t = float(sys.argv[3])

GRAVITY = 9.80665

x = xo + vo * t - (GRAVITY * t**2) / 2

stdio.writeln("Displacement = " + str(x))
