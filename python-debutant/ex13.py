# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:46:12 2022

@author: j.dearaujofirmino
"""

import math

r = int(input("r du cercle: "))
def aire_cercle(r):
    aire = math.pi * (r**2)
    return aire

laire = aire_cercle(r)

print(f"L'aire d'un cercle de r = {r}, est de à peu près: {laire:.2f}")