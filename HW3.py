#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 22:29:01 2026

@author: kimhyomin
"""

import numpy as np
import scipy.integrate as integ

def number(m):
    if m>= 0.01 and m < 0.08:
        result = m**(-0.3)
    elif m >= 0.08 and m < 0.5:
        result = m**(-1.3)
    else: result = m**(-2.3)
    return result

def mass(m):
    if m>= 0.01 and m < 0.08:
        result = m**(0.7)
    elif m >= 0.08 and m < 0.5:
        result = m**(-0.3)
    else: result = m**(-1.3)
    return result

def luminosity(m):
    if m>= 0.01 and m < 0.08:
        result = m**(3.7)
    elif m >= 0.08 and m < 0.5:
        result = m**(2.7)
    else: result = m**(1.7)
    return result

m1_num = integ.quad(number, 0.01, 1, points = [0.08,0.5])[0]

m10_num = integ.quad(number, 10, 300)[0]

print(m1_num, m10_num, m1_num/m10_num)

m1_mass = integ.quad(mass, 0.01, 1, points = [0.08, 0.5])[0]

m10_mass = integ.quad(mass, 10, 300)[0]

print(m1_mass, m10_mass, m1_mass/ m10_mass)

m1_lum = integ.quad(luminosity, 0.01, 1, points = [0.08, 0.5])[0]

m10_lum = integ.quad(luminosity, 10, 300)[0]

print(m1_lum, m10_lum, m1_lum/ m10_lum)