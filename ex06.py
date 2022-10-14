# -*- coding: utf-8 -*-
"""
Araujo José
Le message qui est montre dans le console est:
"le train n° 4242 en provenance de Paris entre en gare. Ce train est terminus Triffouillis-les-Oies."

"""

def annonce(num, prov, dest):
 if dest != "0":
     msg = f"le train n° {num} en provenance de {prov} et à destination de {dest}, entre engare."
 else:
     msg = f"le train n° {num} en provenance de {prov} entre en gare. Ce train est terminus Triffouillis-les-Oies."
 return msg
mon_msg = annonce(4242, "Paris", "0")
print(mon_msg)