#!/usr/bin/env python
"""
Example program for calculating the escape velocity from Earth

Based on Stackoverflow question "Python Equation - Wrong Answer"
http://stackoverflow.com/questions/19417072/python-equation-wrong-answer/19418457
"""
from math import pi

from src.units_thing import UnitsThing

g = UnitsThing(6.67428e-11, "mmm/kgss")
user_circum = UnitsThing(40075, "km")
user_acc = UnitsThing(9.81, "m/ss")
radius = user_circum / (2 * pi)
mass = (user_acc * (radius * radius))/g
vEscape = ((g * mass * 2.0) / radius).sqrt()

print "Escape velocity from Earth is: {0}".format(vEscape)
