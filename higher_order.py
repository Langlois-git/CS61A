"""Generalization"""

from math import pi, sqrt

def area_square(r):
    assert r > 0, 'A length must be positive'
    return r*r

def area_circle(r):
    return r * r * pi

def area_hexagon(r):
    return r * r * 3 * sqrt(3) / 2




