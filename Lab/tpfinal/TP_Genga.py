#! /usr/bin/python

# 6ta Practica Laboratorio 
# Complementos Matematicos I
# Ejemplo parseo argumentos

import argparse
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import time
from collections import defaultdict

'''
    Parametros de layout:
    grafo: tupla que representa nuestro grafo en formato Lista
    pos_x: diccionario que tiene como clave los vertices y guarda sus posiciones con respecto al eje x
    pos_y: idem pos_x con el eje y
    accum_x: diccionario que acumula las fuerzas aplicadas a cada uno de los vertices en direccion horizontal
    accum_y: idem accum_x en direccion vertical
    w: ancho de la pantalla donde se dibuja el grafo
    l: alto de la pantalla donde se dibuja el grafo
    g: fuerza de gravedad, genera una atraccion hacia el centro de la pantalla
    t: temperatura inicial
    p: constante de enfriamiento
    iters: cantidad de iteraciones a realizar
    verbose: booleano que al estar activado, hace que el programa nos muestre informacion mientas corre
    optimize: booleano que al estar activado, hace utilizar un algoritmo optimizado
    refresh: Numero de iteraciones entre actualizaciones de pantalla.
    0 -> se grafica solo al final.
    c1: constante usada para calcular la repulsion entre nodos
    c2: constante usada para calcular la atraccion de aristas
    k: constante usada para el calculo de las fuerzas, la cual depende de la cantidad de vertices, dada en el paper
    columns: constante que representa la cantidad de columnas de la grilla.
    rows: constante que representa la cantidad de filas de la grilla.
    grid: grilla utlizada para la optimizacion del calculo de la fuerza de repulsion.
    squares: diccionario que tiene como clave los vertices y como dato el cuadrante al que corresponde.

'''

class LayoutGraph:
    
    def __init__(self, grafo, g, t, iters, refresh, c1, c2, verbose=False):    

        # Guardo el grafo
        self.grafo = grafo

        # Inicializo estado
        self.pos_x = defaultdict(lambda :0)
        self.pos_y = defaultdict(lambda :0)
        self.accum_x = defaultdict(lambda :0)
        self.accum_y = defaultdict(lambda :0)

        self.w = 1000
        self.l = 2000

        self.g = g
        self.t = t
        
        # Guardo opciones
        self.iters = iters
        self.verbose = verbose
        # TODO: faltan opciones
        self.refresh = refresh
        self.c1 = c1
        self.c2 = c2
        self.k = (math.sqrt((self.w*self.l)/len(self.grafo[0])))


    '''
    Toma un mensaje y lo imprime si el modo verbose esta activado
    '''
    def info(self,msg):
        if self.verbose:
            print(msg)


    def info_accum(self):
        vertices=self.grafo[0]
        if self.verbose:
            print("Acumuladores: ")
            for v in vertices:
                print("Vertice "+ str(v) + ": accum_x = " + str(self.accum_x[v]) + ": accum_y = " + str(self.accum_y[v]))
            print("\n")

    
    def info_pos(self):
        vertices=self.grafo[0]
        if self.verbose:
            print("Posiciones: ")
            for v in vertices:
                print("Vertice "+ str(v) + ": pos_x = " + str(self.pos_x[v]) + ": pos_y = " + str(self.pos_y[v]))
            print("\n")

    '''
    Inicializa la posicion de los vertices en posiciones aleatorias    
    '''

    def randomize_position(self):
        vertices=self.grafo[0]
        for n in vertices:
            x = random.randint(1,self.w-1)
            y = random.randint(1,self.l-1)
            self.pos_x[n] = x
            self.pos_y[n] = y

    '''
    Pone los acumuladores en 0 
    '''

    def reset_accum(self):
        vertices=self.grafo[0]
        for n in vertices:
            x = random.randint(1,self.w-1)
            y = random.randint(1,self.l-1)
            self.accum_x[n] = 0
            self.accum_y[n] = 0
    '''
    Calcula la distancia euclidida entre dos puntos
    '''

    def calc_dist(self,x1,x2,y1,y2):
        f = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        return f

    '''
    Toma dos vertices y devuelve la distancia que los separa
    '''
    
    def dist(self,v1,v2):
        f = self.calc_dist(self.pos_x[v1],self.pos_x[v2],self.pos_y[v1],self.pos_y[v2])
        return f

    '''
    Calcula la fuerza de atraccion de dos vertices unidos por una arista y actualiza
    el valor de los acumuladores
    '''

    def f_attraction(self):
        self.info("Calculando fuerzas de atraccion...\n")
        vertices=self.grafo[0]
        aristas=self.grafo[1]
        for (v1,v2) in aristas:
            dist = self.dist(v1,v2)
            if(dist < 0.5):
                continue
            mod_fa = (dist**2 / self.k*self.c2)
            fx = mod_fa*(self.pos_x[v2] - self.pos_x[v1]) / dist
            fy = mod_fa*(self.pos_y[v2] - self.pos_y[v1]) / dist
            self.accum_x[v1] += fx
            self.accum_y[v1] += fy
            self.accum_x[v2] -= fx
            self.accum_y[v2] -= fy
        self.info_accum()

    '''
    Para cada vertice calcula el valor de la fuerza de repulsion ejercida a los demas vertices
    actualizando el valor de los acumuladores
    '''
                      
    def f_repulsion(self):
        self.info("Calculando fuerzas de repulsion...\n")
        vertices=self.grafo[0]
        aristas=self.grafo[1]
        for n1 in vertices:
            for n2 in vertices:
                if (n1 == n2):
                    continue
                dist = self.dist(n1,n2)
                if(dist<1):
                    fx = random.randint(-10,10)
                    fy = random.randint(-10,10)
                else:    
                    mod_fr = ((self.k*self.c1)**2 / dist)
                    fx = mod_fr*(self.pos_x[n2]-self.pos_x[n1]) / dist
                    fy = mod_fr*(self.pos_y[n2]-self.pos_y[n1]) / dist
                self.accum_x[n2] += fx
                self.accum_y[n2] += fy
        self.info_accum()


    '''
    Calcula la fuerza de gravedad de atraccion de cada vertice hacia el centro
    de la pantalla
    '''

    def f_gravedad(self):
        vertices = self.grafo[0]
        for v in vertices:
            dist = self.calc_dist(self.pos_x[v], self.w/2, self.pos_y[v], self.l/2)
            fx = self.g * (self.w/2 - self.pos_x[v]) / dist
            fy = self.g * (self.l/2 - self.pos_y[v]) / dist
            self.accum_x[v] += fx
            self.accum_y[v] += fy
        self.info_accum()
                           
    '''
    Actualiza las posiciones de los vertices en funcion de las fuerzas calculadas
    anteriormente.
    El valor maximo de desplazamiento estara condicionado por el valor actual
    de la temperatura
    '''

    def actual_pos(self):
        vertices=self.grafo[0]
        for v in vertices:
            mod = math.sqrt(self.accum_x[v]**2 + self.accum_y[v]**2)
            if(mod > self.t):
                self.accum_x[v] = (self.accum_x[v] / mod) * self.t
                self.accum_y[v] = (self.accum_y[v] / mod) * self.t
                
            self.pos_x[v] = self.pos_x[v] + self.accum_x[v]
            if(self.pos_x[v]<1):
                self.pos_x[v]=1
            if(self.pos_x[v]>(self.w-1)):
                self.pos_x[v]=(self.w-1)
                
            self.pos_y[v] = self.pos_y[v] + self.accum_y[v]
            if(self.pos_y[v]<1):
                self.pos_y[v]=1
            if(self.pos_y[v]>(self.l-1)):
                self.pos_y[v]=(self.l-1)
        self.info_pos()


    '''
    Disminuye la temperatura en cada step
    '''

    def actual_temp(self):
        self.t = 0.95 * self.t
        

    '''
    Ejecuta las funciones definidas anteriormente. Primero resetea los acumuladores, despues
    calcula las fuerzas de atraccion repulsion y gravedad y por ultimo actualiza las posicoines
    y la temperatura
    '''

    def step(self, grafico):
        self.reset_accum()
        self.f_attraction()
        self.f_repulsion()
        self.f_gravedad()
        self.actual_pos()
        self.actual_temp()

    def ploteo(self):
        plt.ion()
        for vertice in self.grafo[0]:
            plt.scatter(self.pos_x[vertice],self.pos_y[vertice])
        for arista in self.grafo[1]:
            plt.plot([self.pos_x[arista[0]],self.pos_x[arista[1]]],[self.pos_y[arista[0]],self.pos_y[arista[1]]])
        plt.show()
        plt.pause(0.001)
        plt.clf()
        
        

    '''
    Aplica el algortimo y lo muestra en pantalla
    '''
    def layout(self):
        pos = self.randomize_position()
        plt.ion()
        grafico = self.ploteo()
        iniciar_tiempo = time.time()
        it = 0
        if (self.refresh == 0):
                while(self.t > 0.1 and it<self.iters):
                    self.step(grafico)
                    it+=1
        else:
            while(self.t > 0.1 and it<self.iters):
                for i in range(self.refresh):
                    self.step(grafico)
                    it+=1
                    if(self.t <= 0.1):
                        break
                    self.ploteo()
        self.ploteo()
        

def read_file_graph(file_name):
    f = open(file_name, "r")

    lines = f.readlines();
    q = int(lines[0])
    vertices = []
    for i in range(q):
        v = lines[i+1].split()
        vertices.append(str(v[0]))
    lines = lines[q+1:]
    edges = []
    for s in lines:
        l = s.split()
        edges.append((str(l[0]), str(l[1])))

    graph = (vertices, edges)

    return graph



def main():
    # Definimos los argumentos de linea de comando que aceptamos
    parser = argparse.ArgumentParser()

    # Verbosidad, opcional, False por defecto
    parser.add_argument(
        '-v', '--verbose', 
        action='store_true', 
        help='Muestra mas informacion al correr el programa'
    )
    # Cantidad de iteraciones, opcional, 50 por defecto
    parser.add_argument(
        '--iters',
        type=int,
        help='Cantidad de iteraciones a efectuar', 
        default=10000
    )
    # Temperatura inicial
    parser.add_argument(
        '--t',
        type=float, 
        help='Temperatura inicial', 
        default=100.0
    )
    
    # Archivo del cual leer el grafo
    
    parser.add_argument(
        'file_name',
        help='Archivo del cual leer el grafo a dibujar'
    )
    

    # Gravedad
    parser.add_argument(
        '--g',
        type=float,
        help='Gravedad',
        default=0.1
    )

    # c1
    parser.add_argument(
        '--c1',
        type=float,
        help='Atraccion',
        default=1.0
    )

    # c2
    parser.add_argument(
        '--c2',
        type=float,
        help='Repulsion',
        default=2.5
    )
     # Refresh
    parser.add_argument(
        '--refresh',
        type=int,
        help='Cantidad de iteraciones a realizar antes de graficar',
        default=1
    )
    
    args = parser.parse_args()

    
    graph = read_file_graph(args.file_name)
    '''
    grafo1 = ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], 
              [(0,20),(1, 20),(2, 20),(2, 20),(3, 20),(4, 20),(0, 21),(4 ,21),(5 ,21),(9 ,21),(10, 21),(0 ,22),(1 ,22),(5 ,22),(6 ,22),(11, 22),(1 ,23),(2 ,23),(6 ,23),(7 ,23),(12 ,23),(2 ,24),(3 ,24),(7 ,24),(8 ,24),(13 ,24),(3 ,25),(4 ,25),(8 ,25),(9 ,25),(14 ,25),(9 ,26),(10 ,26),(14 ,26),(15 ,26),(19 ,26),(5 ,27),(10 ,27),(11 ,27),(15 ,27),(16 ,27),(6 ,28),(11 ,28),(12 ,28),(16 ,28),(17 ,28),(7 ,29),(12 ,29),(13 ,29),(17 ,29),(18 ,29),(8 ,30),(13 ,30),(14 ,30),(18 ,30),(19 ,30),(15 ,31),(16 ,31),(17 ,31),(18 ,31),(19 ,31)])
    '''

    # Creamos nuestro objeto LayoutGraph
    layout_gr = LayoutGraph(
        graph, 
        iters=args.iters,
        g = args.g,
        t = args.t,
        refresh=args.refresh,
        c1 = args.c1,
        c2 = args.c2,
        verbose=args.verbose
        )
    
    # Ejecutamos el layout
    layout_gr.layout()
    return


if __name__ == '__main__':
    main()
