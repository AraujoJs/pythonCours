# -*- coding: utf-8 -*-
"""
Quelle est la valeur de la variable val après l'exécution de ce programme ?
Ce programme return 15 comme valeur.
@author: j.dearaujofirmino
"""

def ma_fct(a):
    b = 3
    while a > 0:
        b = b + a
        a = a - 2
    return b


val = ma_fct(6)

print(val)