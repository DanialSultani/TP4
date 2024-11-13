# -*- coding: utf-8 -*-
"""
EX1 TP2 PYTHON OBJET
@author: Danial
"""

def afficher(p):
    termes = []
    for i, coef in enumerate(p):
        if coef != 0:
            if i == 0:
                termes.append(f"{coef}")
            elif i == 1:
                termes.append(f"{coef}X")
            else:
                termes.append(f"{coef}X^{i}")
    polynome = " + ".join(termes[::-1])  # Inverser les termes pour commencer par la plus grande puissance
    print(polynome)
       
polynome = ["1","2","3","4"]

def get_veleur(p,x):
    i = 0 
    valeur =  0
    for i in range (len(p)):
        valeur += p[i]*x**i
    print (valeur)
        
liste = [eval(i) for i in polynome]

get_veleur(liste, 4)
#COMMENTAIRE TEST GITHUB
    