# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:28:11 2022

@author: j.dearaujofirmino
"""

from random import randint

def somme_hasard(n):
    print("=" * 35)
    somme = 0
    numGenere = 1
    while numGenere != 0:
        numGenere = randint(0, n)
        somme = somme + numGenere
        print(f"Nombre généré : {numGenere}, somme : {somme}")
    print("=" * 10 + "fin du programe" + "=" * 10)
        

somme_hasard(int(input("Valeur de n: ")))
