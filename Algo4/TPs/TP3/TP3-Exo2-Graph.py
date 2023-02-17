import matplotlib.pyplot as plt
from random import *
import time

###########################################

def GenereGraph(n,p):
    Contract = [i for i in range(n)]
    E = []
    for c1 in Contract:
        for c2 in Contract:
            if (c1 < c2 and random()<=p):
                E.append((c1,c2))
    return E,Contract


def ContractArrete(E,Contract):
    a = E[randint(0,len(E)-1)]
    for i in range(len(E)):
        el = list(E[i])
        if E[i][0] == a[0]: el[0] = a[1]
        elif E[i][1] == a[0]: el[1] = a[1]
        E[i] = tuple(el)
    while (a[1],a[1]) in E:
        E.remove((a[1],a[1]))
    for i in range(len(Contract)):
        if Contract[i] == a[0]:
            Contract[i] = a[1]


def CoupeMin(E,Contract):
    Ecoupe,Ecouleur = E.copy(),E.copy()
    Ccoupe = Contract.copy()
    for i in range(len(Contract)-2):
        ContractArrete(Ecoupe,Ccoupe)
    Ecoupe = list(set(Ecoupe))

    for i in range(len(Ecouleur)):
        ecl = list(Ecouleur[i])
        ecl[0] = Ccoupe[ecl[0]]
        ecl[1] = Ccoupe[ecl[1]]
        Ecouleur[i] = tuple(ecl)

    Asup = []
    for i in range(len(Ecouleur)):
        if (Ecouleur[i][0] == Ecouleur[i][1]):
            Asup.append(Ecouleur[i])
    
    for j in range(len(Asup)):
        Ecouleur.remove(Asup[j])

    print(Ecouleur)
    return Ccoupe,len(Ecouleur)








#######Programme Principal########
n = 8
p = 0.3
E,C = GenereGraph(n,p)

Etest = [(0,1),(0,2),(1,3),(2,3),(3,5),(2,4),(4,5)]
Ctest = [0,1,2,3,4,5]
print("Contract initial=", C)
print("E initial =",E)

"""
ContractArrete(E,Contract)
print("Contract contrac=", Contract)
print("E contrac =",E)
"""

ContractMin,eMin = CoupeMin(E,C)
print("Contract CoupeMin=", ContractMin)
print("taille CoupeMin =",eMin)