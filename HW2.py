#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 21:24:44 2026

@author: kimhyomin
"""

import numpy as np
import scipy.integrate as integrate

tH = 4.58e17
def f(z):
    zz = 1+z
    result = np.sqrt(0.3153*zz**5 + 1e-5*zz**6+0.6847*zz**2)
    return 1/result
tt = integrate.quad(f, 0, 4.912)[0]
print(tt*tH)
