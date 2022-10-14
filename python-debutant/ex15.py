# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:57:26 2022

@author: j.dearaujofirmino
"""

def tableOf(n):
    print("=" * 10)
    for x in range(11):
        print(f"{x} * {n} = {x * n}")
    print("=" * 10)

tableOf(int(input("Vous voulez le tableau de quel numero?: ")))