def clause(s):
    L = s.split()
    return [int(v) for v in L[:-1]]

def parseur(nom):
    with open(nom) as f:
        F = []
        n = 0
        for ligne in f:
            if ligne[0] == 'c': continue
            if ligne[0] == 'p':
                L = ligne.split()
                n = int(L[-2])
            else: 
                F.append(clause(ligne))
    return F, n

def affiche(F):
    s=''
    for j in range(0,len(F)):
        C=F[j]
        s=s+'('
        for i in range(0,len(C)):
            if C[i]<0:
                s=s+'¬'
            s=s+'x'+str(abs(C[i]))
            if i==len(C)-1:
                s=s+')'
            else:    
                s=s+' ∨ '
        if j!=len(F)-1:
            s=s+' ∧ '
    return s

################################################################

def valide(F, A):
    for c in F: #Pour chaque clause
        clause = False
        for l in c: #Pour chaque litteral
            if(l<0):
                if(A[abs(l)-1] == -1):
                    clause = True
            else:
                if(A[l-1] == 1):
                    clause = True
        if(not(clause)):
            return False
    return True

################################################################

def aff_suivante(A):
    i = 0
    while(i<len(A) and A[i]==1):
        A[i] = -1
        i += 1
    if(i==len(A)): return None
    else:
        A[i] = 1
        return A

def test_aff_suivante(n):
    A = [-1]*n
    while(A != None):
        print(A)
        A = aff_suivante(A)
    return None
        
#########################################################################

def sat_exhau(F, n):
    A = [-1] * n
    while(not(valide(F,A))):
        A = aff_suivante(A)
        if(A==None): return "Insatisfiable"
    return A

def elimination(F, n, b):
    psi=[]
    for C in F:
        clause=[]
        sat=False
        for l in C:
            if(abs(l)==n and l*b>0):
                sat=True
            elif(abs(l)!=n):
                clause.append(l)
        if(not(sat)):
            if(not(clause==[] and ([] in psi))):psi.append(clause)
    return psi

def sat_backtrack(F, n):
    if(F==[]):return [1]*n
    elif(F==[[]]):return "Insatisfiable"
    else:
        for b in [-1,1]:
            P = elimination(F,n,b)
            A = sat_backtrack(P,n-1)
            if(P!=[[]] and A!="Insatisfiable"):return A+[b]
    return "Insatisfiable"

###############################################################################

print("-------------------------------------------------------")
Fichier="./cnf/hole6.cnf"
print("Formule du fichier: "+Fichier)
F,n=parseur(Fichier)
print("Récupérée sous forme de tableau: ",F)
print("Nombre de variables: ",n)
print("Formule SAT: ",affiche(F))
print("-------------------------------------------------------")
#print("Valide 1 ? : ",valide(F, [1,1,-1]))
#print("Valide 2 ? : ",valide(F, [-1,-1,1]))
#print("-------------------------------------------------------")
#print(test_aff_suivante(4))
#print("-------------------------------------------------------")
#print("Satisfiabilité normale: ",sat_exhau(F, n))
#print("-------------------------------------------------------")
#print("Formule post-Elimination: ",elimination(F,n,1))
print("Sat_backtrack: ",sat_backtrack(F, n))