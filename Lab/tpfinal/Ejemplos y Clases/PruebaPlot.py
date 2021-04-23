import matplotlib.pyplot as plt
import numpy as np
import random

#Grafo A Dibujar
grafo1 = ([0,1,2,3,4],[(0,2),(0,3),(2,4),(1,3)])

posx = []
posy = []

#Asigno coordenadas aleatorias

for i,v in enumerate(grafo1[0]):
    posx.append(random.random())
    posy.append(random.random())
    #print(posx[i],posy[i])

#Dibujo puntos
plt.scatter(posx,posy)

#Dibujo Aristas
for e in grafo1[1]:
    plt.plot([posx[e[0]],posx[e[1]]],[posy[e[0]],posy[e[1]]])

plt.show()

'''
def Frucht:
    Grafo = ([0,1,2,3,4],[(0,2),(0,3),(2,4),(1,3)])

    PosX = []
    PosY = []

    for i in enumerate(Grafo[0]):
        PosX.append(random.random())
        PosY.append(random.random())
        print(PosX[i],PosY[i])

    for v in enumerate(Grafo[0]):
        '''
