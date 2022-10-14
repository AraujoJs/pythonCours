# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:39:51 2022

@author: j.dearaujofirmino
"""

def ma_fct(a):
    b = 0
    while a > 2:
        b = b + 1
        a = a - 2
    return b


val = ma_fct(6)

print(val)