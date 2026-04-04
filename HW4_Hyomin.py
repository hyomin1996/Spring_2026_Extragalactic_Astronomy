#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 03:59:29 2026

@author: kimhyomin
"""

import numpy as np
import matplotlib.pyplot as pl
import uncertainties as uc
from uncertainties import ufloat
from uncertainties import unumpy as unp

tb = np.loadtxt('table4.txt')
period = np.zeros(len(tb))
mf = np.zeros(len(tb))
F = np.zeros(len(tb))
sig_F= np.zeros(len(tb))
a_0 = -6.29 #mag
for i in range(len(tb)):
    p = tb[i][7]
    period[i] =  p #days
    F[i] = tb[i][-4] #mag
    mf[i] = a_0 -3.35*(np.log10(p)-2.3)
    sig_F = tb[i][-3]
D = 10**((F-mf+5)/5)/1e6 #Mpc

print(np.average(D))

# D_avg = 6.40 Mpc

###uncertainty

x_val = unp.uarray(F, sig_F)
a_0_sig = ufloat(-6.29,0.033)
slope = ufloat(3.55, 0.12) #slope uncertainty

mf_sig = a_0_sig -slope*(np.log10(p)-2.3)
D_sig = 10**((x_val-mf_sig+5)/5)
mu_sig = np.average(x_val-mf_sig)

D_sig_avg = np.average(D_sig)
print(D_sig_avg)
print(mu_sig)