# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:45:26 2022

@author: j.dearaujofirmino
"""

def nb_chifrres(n):
    size = 0
    m = 10
    end = False
    while end != True:
        count = 1
        if n < (m * count) :
            size = size + 1
            count = count + 1
        else:
            end = True
    print(size)


 
nb_chifrres(int(input("Valeur n: ")))