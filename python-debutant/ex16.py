# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:07:26 2022

@author: j.dearaujofirmino
"""

def bissextile(a):
    if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
        print(f"L'anne {a} est bissextile!")
    else:
        print(f"L'anne {a} n'est pas bissextile!")
        
bissextile(2020)
bissextile(2024)
bissextile(2028)
bissextile(1900)
bissextile(2100)
bissextile(2200)
bissextile(2000)