import numpy as np
import matplotlib.pyplot as plt #importation des bibliothèques nécessaires au graphes
from math import sqrt

x = np.arange(0, 20, 1); #x va de 0 a 20 avec un pas de 1

def u(n): #Syntaxe pour créer une fonction
    return u(n-1)*0.5+3

y = [] #Creation d'un tableau qui contiendra les valeurs des ordonnés du graphe
for i in x:
    y.append(u(i)) #ajoute une case a y valant ce que renvois la fonction u a un rang i


def f(x): #fonction qui parle d'elle meme
    return 3+1/x

def rec(i): #fonction necessaire a la creation du graphe
    G = 3 # ordonné commencant a 3 
    x = [] #creation de tableaux
    y = []
    
    y.append(G)
    x.append(0)
    print(0,G) #premiere ligne d'affichage sur la console.
    for n in range(1,i):
        G = f(G)
        y.append(G)
        x.append(n)
        print(n,G,sqrt(10)-G)
    return G,x,y

G,x,y = rec(15)

plt.plot(x, y, 'r-')
plt.show()

