#! /usr/bin/python

import sys # sys.sarasa

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
    cant_vertices = int(input("Ingrese cantidad de nodos."))
    nodos = []
    aristas = []
    for i in range(cant_vertices):
        nodos.append(input("Ingrese el nombre del {0} nodo".format(i+1)))

    try:
        while True:
            s = (input("Ingrese aristas: "))
            aristas.append( tuple(s.split(" ")))
            
    except EOFError:
        pass
    return (nodos, aristas)

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
    with open(file_path, 'r')as file:
        cant_vertices = int(file.readline())
        nodos = []
        aristas = []
        for i  in range(cant_vertices):
            nodos.append(file.readline()[:-1])
        for line in file:
            aristas.append(tuple(line[:-1].split(" ")))
    return (nodos, aristas)

def main():
    if(len(sys.argv) >= 2):
        grafito = sys.argv[1]
    grafo = lee_grafo_archivo(grafito)
    print(grafo)

if __name__ == "__main__":
    main()

        
    
