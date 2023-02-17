def lecture_sudoku(nom):
    with open(nom) as f:
        G = []
        for ligne in f:
            G += ligne.split()
        n=G[0]
        G.pop(0)
    return G,n

def affiche_sudoku(G,n):
    compteur = 0
    affiche = "\n"
    for i in G:
        if(compteur == int(n)**2):
            compteur = 0
            affiche += "\n"
        compteur += 1
        if(int(i)==0):
            affiche += "_ "
        else:
            affiche += i+" "
    return affiche

def zone(G,n,u):
    z = []
    ligne = u/n
    colonne = u%n
    for i in len(G)-1:
        if(i/n==ligne and i%n==colonne):
            z.append(i)
    return z


##################################################
print("-------------------------------------------------------")
Fichier="./sudokus/sudoku-3-moyen-9.txt"
print("Formule du fichier: "+Fichier)
G,n=lecture_sudoku(Fichier)
print("Récupérée sous forme de tableau: ",G)
print("Nombre de variables: ",n)
print("Grille sudoku: ",affiche_sudoku(G,n))
print("Affichage de la zone: ",zone(G,n,4))