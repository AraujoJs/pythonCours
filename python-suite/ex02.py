# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:45:26 2022

@author: j.dearaujofirmino
"""


def nb_chifrres(n):
    count = 0
    for i in n:
        count = count + 1
    return count

nbChifre = nb_chifrres(str(input("Un numero:")))
print(nbChifre)
