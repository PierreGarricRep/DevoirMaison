import numpy as np
import matplotlib.pyplot as plt #importation des bibliothèques nécessaires au graphes
from math import sqrt #et ici de la racine carrée



y = [] #Creation d'un tableau qui contiendra les valeurs des ordonnés
x = [] #idem pour les abscisses



def f(x): #fonction qui parle d'elle meme
    return 3+1/x

def rec(i): #fonction necessaire a la creation du graphe
    G = 3 # ordonné commencant a 3 
    y.append(G)#ajoute une case au tableau qui vaut G
    x.append(0)
    print(0,G)#affiche les valeurs 0 et la valeur de G (ici 3) dans la console
    for n in range(1,i):
        G = f(G)
        y.append(G)
        x.append(n)
        print(n,G)#ici des valeurs de n et G
    return G,x,y #tableaux necessaires par la suite pour faire le graphe.

G,x,y = rec(10)

plt.plot(x, y, 'r-')#configuration du graphe.
plt.show() #puis affichage.

