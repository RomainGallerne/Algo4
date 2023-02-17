from matplotlib import pyplot as plt
from matplotlib import collections  as mc
from math import *
from random import *
from time import *

### Dessins ###

def __points(ax, Points, color, markersize):
    ax.plot(*zip(*Points),marker='.',markersize=markersize,linestyle='',color=color)

def __aretes(ax, Points, Adj, color, markersize, lw):
    liste = []
    for s in Adj:
        for v in Adj[s]:
            liste.append([Points[s], Points[v]])
    lc = mc.LineCollection(liste, linewidth=lw, color=color)
    ax.add_collection(lc)
    ax.autoscale()

def __parcours(ax, Points, Parcours, Adj, color1, color2, markersize):
    n = len(Points)
    liste1 = []
    liste2 = []
    for i in range(len(Parcours)):
        if len(Adj) == 0 or Parcours[(i+1)%n] in Adj[Parcours[i]]: 
            liste1.append([Points[Parcours[i]], Points[Parcours[(i+1)%n]]])
        else:
            liste2.append([Points[Parcours[i]], Points[Parcours[(i+1)%n]]])
    lc1 = mc.LineCollection(liste1, linewidth=1, color=color1)
    lc2 = mc.LineCollection(liste2, linewidth=1, color=color2)
    ax.add_collection(lc1)
    ax.add_collection(lc2)
    ax.autoscale()

    if len(Parcours) < 100:
        for s in range(len(Parcours)):
            ax.annotate(str(s+1), Points[Parcours[s]])

def dessinPoints(Points, color="C0",markersize=5):
    fig, ax = plt.subplots()
    __points(ax, Points, color, markersize)
    plt.axis('equal')
    plt.show()

def dessinGraphe(Points, Adj, color="C0",markersize=5):
    fig, ax = plt.subplots()
    __points(ax, Points, color, markersize)
    __aretes(ax, Points, Adj, color, markersize, 1)
    plt.axis('equal')
    plt.show()

def dessinArbre(Points, Arbre, Adj={}, color1="C0",color2="C1",markersize=5):
    fig, ax = plt.subplots()
    __points(ax, Points, color1, markersize)
    __aretes(ax, Points, Adj, color1, markersize, 0.5)
    __aretes(ax, Points, Arbre, color2, markersize,1)
    plt.axis('equal')
    plt.show()



def dessinParcours(Points, Parcours, Adj = {}, color1="C0", color2="C1", markersize=5):
    n = len(Points)
    assert sorted(Parcours) == list(range(n)), "le parcours ne visite pas chaque sommet une fois et une seule"

    fig, ax = plt.subplots()
    __points(ax, Points, color1, markersize)
    if len(Adj) > 0: __aretes(ax, Points, Adj, 'gray', markersize, .5)
    __parcours(ax, Points, Parcours, Adj, color1, color2, markersize)

    plt.axis('equal')
    plt.show()


def distance(A,B):
    return sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)

def aretes(P):
    A = []
    for a in range(0,len(P)):
        for b in range(a+1,len(P)):
            A.append((a,b,distance(P[a],P[b])))
    return A

def pointsAleatoires(n,xmax,ymax):
    P = []
    for i in range(n):
        P.append((uniform(0,xmax),uniform(0,ymax)))
    return P

def listesAdjacence(n,A):
    dico = {}
    for i in range(n):
        listeAjout = []
        for a in A:
            if(a[0]==i and a[1] not in listeAjout): listeAjout.append(a[1])
            elif(a[1]==i and a[0] not in listeAjout): listeAjout.append(a[0])
        dico[i] = listeAjout
    return dico

def arbreCouvrant(n,A):
    Couleur = [i for i in range(n)]
    At = A.copy()
    At.sort(key=lambda a: a[2])
    T = []
    for i in range(len(At)):
        ancienCouleur = Couleur[At[i][1]]
        nouvelleCouleur = Couleur[At[i][0]]
        if(nouvelleCouleur != ancienCouleur):
            if(At[i] not in T): 
                T.append(At[i])
                for c in range(len(Couleur)):
                    if(Couleur[c] == ancienCouleur): Couleur[c] = nouvelleCouleur
    return T

def parcoursProfondeur(lA):
    P = [0]
    C = []
    while(len(P)>0):
        s = P.pop()
        C.append(s)
        for v in lA[s]:
            if(v not in C):
                P.append(v)
    return C

def VdC(P):
    n = len(P)
    A = aretes(P)
    aC = arbreCouvrant(n,A)
    lAc = listesAdjacence(n,aC)
    pP = parcoursProfondeur(lAc)
    dessinParcours(P,pP,lAc)


################# Programme ###################

"""
A , B , C = (121 ,77) , (48 ,70) , (12 ,72)
print(distance(A,B),distance(A,C),distance(B,C))

P = [(6,20),(67,18),(96,4),(32,45)]
print(aretes(P))

print(pointsAleatoires(3,10,20))
dessinPoints(pointsAleatoires(20,10,20))

A = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
print(listesAdjacence(4,A))

P = pointsAleatoires(10,20,20)
A = listesAdjacence(10,aretes(P))
dessinGraphe(P,A)

A = aretes([(6,20),(67,18),(96,4),(32,45)])
print(A)
print(arbreCouvrant(4,A))

t = 5
P = pointsAleatoires(t,20,20)
A = aretes(P)

dessinArbre(P,listesAdjacence(t,arbreCouvrant(t,A)),listesAdjacence(t,A))

P = [(6,20),(67,18),(96,4),(32,45)]
A = aretes(P)
print(arbreCouvrant(4,A))
dessinArbre(P,listesAdjacence(4,arbreCouvrant(4,A)),listesAdjacence(4,A))

VdC([(6 ,60) ,(67 ,62) ,(96 ,76) ,(32 ,35) ,(70 ,39) ,(98 ,24) ,(129 ,30) ,(121 ,3) ,(48 ,10) ,(12 ,8)])
"""

#TEST MAX COUVRANT EN 10s
"""
n = 0
t1,t2 = 0,0
while(t2-t1 < 10):
    t1 = time()
    P = pointsAleatoires(n,10000,10000)
    A = aretes(P)
    listesAdjacence(n,A)
    AC = arbreCouvrant(n,A)
    listesAdjacence(n,AC)
    t2 = time()
    n += 50
    print(n)
print("\n n final : ",n)

P = pointsAleatoires(800,10000,10000)
A = aretes(P)
AC = arbreCouvrant(800,A)
dessinArbre(P,listesAdjacence(800,AC),listesAdjacence(800,A))
"""

n = 10
P = pointsAleatoires(n,1000,1000)
A = aretes(P)
aC = arbreCouvrant(n,A)
lA = listesAdjacence(n,A)
lAc = listesAdjacence(n,aC)
pP = parcoursProfondeur(lAc)
dessinGraphe(P,lA)
dessinArbre(P,lAc,lA)
dessinParcours(P,pP,lA)
VdC(P)

#TEST MAX VDC EN 10s
"""
n = 50
t1,t2 = 0,0
while(t2-t1 < 10):
    t1 = time()
    P = pointsAleatoires(n,10000,10000)
    VdC(P)
    t2 = time()
    n += 50
    print(n)
print("\n n final : ",n)
"""