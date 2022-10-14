# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:55:06 2022

@author: j.dearaujofirmino
"""

import math

def pair_impair(n):
    if n % 2 == 0:
        return "pair"
    else :
        return "impair"
    
print(pair_impair(int(input("Digite un numero: "))))