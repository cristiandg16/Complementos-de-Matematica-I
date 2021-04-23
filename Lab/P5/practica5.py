#! /usr/bin/python

# 5ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

def prim(grafo):
    '''
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de Prim
    y retorna el MST correspondiente. 
    NOTA: El grafo de entrada se asume conexo.
    '''
    Aristas = grafo[1]
    SourceDest = []
    Vertex = grafo[0]
    for vert in Vertex:
        Ady = []
        for x in Aristas:
            if x[0] == vert:
                tupla = (x[1],x[2])
                Ady = Ady + tupla    
        tuplaAdy = (vert,Ady)
        SourceDest = SourceDest + tuplaAdy

    return SourceDest
            


def kruskal(grafo):
    '''
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
    Kruskal y retorna el MST correspondiente (o un bosque, en el caso de que 
    no sea conexo).
    '''
    Vertices = grafo[0]
    Aristas = grafo[1]

    return


def main():
    pass


if __name__ == "__main__":
    main()
