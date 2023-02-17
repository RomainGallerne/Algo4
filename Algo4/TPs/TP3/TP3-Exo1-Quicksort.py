import matplotlib.pyplot as plt
from random import *
import time

###########################################

def TableauAuHasard(n):
    TabHasard=[0]*n
    for i in range(0,n):
        TabHasard[i]=randint(1,n*n)
    return TabHasard

def TriFusion(n,T):
    if n>1:
        n1=n//2 
        n2=n-n1 
        T1=[0]*n1
        T2=[0]*n2
        for i in range(0,n1):
            T1[i] = T[i]
        for j in range(n1,n):
            T2[j-n1] = T[j]
        Fusion(n1,n2,TriFusion(n1,T1),TriFusion(n2,T2),T)
    return T


def Fusion(n1, n2, T1, T2, T):
    i1 = 0
    i2 = 0
    for i in range(0,n1+n2):
        if(i1<n1):
            if(i2 >= n2 or T1[i1] <= T2[i2]):
                    T[i] = T1[i1]
                    i1+=1
            else:
                T[i] = T2[i2]
                i2+=1
        else:
            T[i] = T2[i2]
            i2+=1 
    return T

def TriBulles(n,T):
    for i in range(0,n):
        for j in range(i,n):
            if T[j] < T[i]:
                T[i],T[j] = T[j],T[i]
    return T

def Quicksort(n,T):
    if n==0: return []
    elif n==1: return [T[0]]
    else: p = T[randint(0,n-1)]
    T0,T1,Tm= [],[],[]
    for i in range(n):
        if T[i]<p:
            T0.append(T[i])
        elif T[i]>p:
            T1.append(T[i])
        else:
            Tm.append(T[i])
    return Quicksort(len(T0),T0)+Tm+Quicksort(len(T1),T1)

def Quickselect(k,T):
    p = T[randint(0,n)]
    n0 = 0
    T0,T1 = [],[]
    for i in range(n):
        if T[i]<p:
            n0 += 1
            T0.append(T[i])
        else:
            T1.append(T[i])
    if n0 == k-1: return p
    elif n0 >= k:
        return Quickselect(k,T0)
    else:
        return Quickselect(k-n0-1,T1)

#######Programme Principal########

choix=int(input("Taper 1 pour un test sur un exemple simple, 2 pour un comparatif TriFusion/TriBulles/Quicksort/Python: "))
if choix==1:
    n=6
    T=TableauAuHasard(n)
    print("Tableau de depart: ",T)

    Tbulles=T.copy()
    TriBulles(n, Tbulles)
    print("Apres tri bulles: ",Tbulles)

    Tfusion=T.copy()
    TriFusion(n, Tfusion)
    print("Apres tri fusion: ",Tfusion)

    Tquick=T.copy()
    Tquick = Quicksort(n, Tquick)
    print("Apres QuickSort",Tquick)

    Tpython=T.copy()
    Tpython = sorted(T)
    print("Apres tripython",Tpython)
    
else:
    #Valeurs de n choisies    
    abscisses = [n for n in range(1,1000,10)]
    #Temps de calcul
    tps1 = []
    tps2 = []
    tps3 = []
    tps4 = []

    n = 10
    print("\n-------------------------------------- Séquence d'exemple pour n=10 ----------------------------------------")
    T=TableauAuHasard(n)
    print("Tableau de départ: ",T)
    T1=T.copy()
    TriBulles(n, T1)
    print("Tableau tri bulles: ",T1)
    T2=T.copy()
    TriFusion(n, T2)
    print("Tableau tri fusion: ",T2)
    T3=T.copy()
    T3 = Quicksort(n, T3)
    print("Tableau quick sort: ",T3)
    T4=T.copy()
    T4 = sorted(T4)
    print("Tableau python: ",T4)

    for n in range(1,1000,10):
        T=TableauAuHasard(n)
        T1=T.copy()
        t=time.time()
        TriBulles(n, T1)
        tps1.append(time.time()-t)
        T2=T.copy()
        t=time.time()
        TriFusion(n, T2)
        tps2.append(time.time()-t)
        T3=T.copy()
        t=time.time()
        T3 = Quicksort(n, T3)
        tps3.append(time.time()-t)
        T4=T.copy()
        t=time.time()
        T4 = sorted(T4)
        tps4.append(time.time()-t)
    
    #Tracé
    plt.plot(abscisses, tps1, label="Tri bulles")
    plt.plot(abscisses, tps2, label="Tri Fusion")
    plt.plot(abscisses, tps3, label="Quicksort")
    plt.plot(abscisses, tps4, label="Python")
    plt.legend(loc="upper left")
    plt.show()