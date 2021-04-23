#! /usr/bin/python

# 1ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

import sys

def lee_grafo_archivo(file_path):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    ruta =  '/home/cristiann_16/Escritorio/grafito.txt'
    archivo = open(ruta,'r')
    lista = []
    lista_tuplera = []
    #for linea in archivo.readlines():
    #   lista += linea.rstrip('\n')

    for i in range(0,6):
        if(i<3):
            lista += archivo.readline().rstrip('\n')
        else:
            lista_tuplera += (archivo.readline().rstrip('\n'),)

    lista += lista_tuplera
    
    print(lista)
    
    pass


def lee_grafo_stdin():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    longitud = input("Ingrese la cantidad de vertices:\n")

    Vertices = []
    for i in range(0,int(longitud)):
        vertice = raw_input("Ingrese el vertice Nº %d :\n" % (i+1))        
        Vertices += vertice

    Aristas = []
    for j in range(0,2**int(longitud)-1):
        v1 = raw_input("Ingrese el vertice origen de la arista:\n")
        v2 = raw_input("Ingrese el vertice destino de la arista:\n")
        if(v1 == '\n' or v2 == '\n'):
            break
        Aristas.append((v1,v2))
        

    #print((Vertices,Aristas))
    return (Vertices,Aristas)


def lee_entrada_1():
    count = 0
    for line in sys.stdin:
        count = count + 1
        print('Linea: [{0}]').format(line)
    print('leidas {0} lineas').format(count)
    

def imprime_grafo_lista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    print(grafo)
    
def lista_a_adyacencia(grafo_lista):
    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de adyacencia.
    '''
    Matriz = [] 
    TuplaA = (grafo_lista[0],Matriz)
    
    inde = 0
    for i in grafo_lista[0]:
        Matriz.append([])
        for j in grafo_lista[0]:
            if(((i,j) in grafo_lista[1]) or (j,i) in grafo_lista[1]):
                Matriz[inde].append(1)
            else:
                Matriz[inde].append(0)
        inde = inde + 1
        
    print(TuplaA)
    return(TuplaA)

def lista_a_incidencia(grafo_lista):
    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de incidencia.
    '''
    Matrix = []
    Tupla = (grafo_lista[0],Matrix)
    
    index = 0
    for i in grafo_lista[0]:
        Matrix.append([])
        for j in grafo_lista[0]:
            if(((i,j) in grafo_lista[1]) and ((j,i) in grafo_lista[1])):
                Matrix[index].append(1)
            else:
                Matrix[index].append(0)
        index = index + 1
        

    return(Tupla)


def incidencia_a_lista(grafo_incidencia):
    '''
    Transforma un grafo representado una matriz de incidencia a su 
    representacion por listas.
    '''
    ListVertices = grafo_incidencia[0]
    
    Aristas = []
    for vertex in ListVertices:
        for i in grafo_incidencia[1]:
            for j in len(ListVertices):
                if(i.index(vertex)==1 and i.index(j)==1):
                    Aristas.append((vertex,ListVertices[j]))

     Ret = (grafo_incidencia[0],Aristas)
     return Ret
    


def imprime_grafo_incidencia(grafo_incidencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de incidencia.
    '''
    for i in range(0,len(grafo_incidencia[1])):
        print(grafo_incidencia[1][i])
        print("\n")


def adyacencia_a_lista(grafo_adyacencia):
    '''
    Transforma un grafo representado una matriz de adyacencia a su 
    representacion por listas.
    '''
    Vertices = grafo_adyacencia[0]
    Filas = grafo_adyacencia[1]
    Aristas = []
    
    for vertex in Vertices:
        index = 0
        for j in len(Vertices):
            if(Filas[index][j] == 1):
                Aristas.append((vertex,Vertices[j]))
        index = index + 1 

    
    return (Vertices,Aristas) 

def imprime_grafo_adyacencia(grafo_adyacencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de adyacencia.
    '''
    print(adyacencia_a_lista(grafo_adyacencia))
