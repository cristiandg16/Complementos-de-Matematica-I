#! /usr/bin/python
# -*- coding: utf-8 -*-

# 3ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos
 
'''
Recordatorio: 
- Un camino/ciclo es Euleriano si contiene exactamente 1 vez
a cada arista del grafo
- Un camino/ciclo es Hamiltoniano si contiene exactamente 1 vez
a cada vértice del grafo
'''

def esCaminoEuleriano(grafo, camino):
    '''Comprueba si una lista de aristas constituye un camino euleriano
	en un grafo.

	Argumentos:
		grafo: Grafo en formato de listas. 
			   Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

		camino: Lista de aristas. Posible camino.
				Ej: [('a', 'b'), ('b', 'c')]

        Retorno:
        boolean: camino es camino euleriano en grafo

    '''

    AristaInicial = list(camino[0])
    VerticeInicial = AristaInicial[0]
	
    for i in range(0,len(camino)-1):
    	VertExtremo = camino[i][1]
    	if((VertExtremo != camino[i+1][0]) or (VerticeInicial == camino[i+1][1])):
    	    return False
		

	
    for aristas in camino:	#recorremos las aristas del camino pasado como argumento.
        if(camino.count(aristas)>1):	#si se repite alguna ya no es un camino de euler
            return False

    return True



def esCicloEuleriano(grafo, ciclo):
    '''Comprueba si una lista de aristas constituye un ciclo euleriano
	en un grafo.

	Argumentos:
		grafo: Grafo en formato de listas. 
			   Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

		camino: Lista de aristas. Posible ciclo.
				Ej: [('a', 'b), ('b', 'c')]

    Retorno:
        boolean: ciclo es ciclo euleriano en grafo

    '''
    Longitud = len(grafo[0])

    VerticeInit = grafo[0][0]
    VerticeFinal = grafo[0][Longitud-1]

    camino = ciclo[0:Longitud-1]

    if(((VerticeFinal,VerticeInit) in ciclo) and esCaminoEuleriano(grafo,camino)):
        if((VerticeFinal,VerticeInit) in grafo[1]):
            return True

    return False
    
    
def esCaminoHamiltoniano(grafo, camino):
    '''Comprueba si una lista de aristas constituye un camino hamiltoniano
	en un grafo.

	Argumentos:
		grafo: Grafo en formato de listas. 
			   Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

		camino: Lista de aristas. Posible camino.
				Ej: [('a', 'b'), ('b', 'c')]

    Retorno:
        boolean: camino es camino hamiltoniano en grafo

    '''
    CantAristas = len(camino)
    
    VerticeIni = camino[0][0]
    VerticeEnd = camino[CantAristas-1][1]
    #print(VerticeEnd)
    if(VerticeEnd == VerticeIni):
        '''Corroboramos que no haya un ciclo'''
        return False

    ListaVerticesCamino = []
    for Aristx in camino:
        ListaVerticesCamino = ListaVerticesCamino + list(Aristx)
        if not(Aristx in grafo[1]):
            return False
    #print(ListaVerticesCamino)
    
    for Vertex in ListaVerticesCamino:
        if(ListaVerticesCamino.count(Vertex) > 2 or (Vertex not in grafo[0])):
            return False
    
    return True

def esCicloHamiltoniano(grafo, ciclo):
    '''Comprueba si una lista de aristas constituye un ciclo hamiltoniano
	en un grafo.

	Argumentos:
		grafo: Grafo en formato de listas. 
			   Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

		camino: Lista de aristas. Posible ciclo.
				Ej: [('a', 'b), ('b', 'c')]

    Retorno:
        boolean: ciclo es ciclo hamiltoniano en grafo

    '''
    VertexInit = ciclo[0][0]
    VertexEnd  = ciclo[len(ciclo)-1][1]

    camino = ciclo[0:len(ciclo)-1]
    
    if((esCaminoHamiltoniano(grafo,camino) == True) and (VertexInit == VertexEnd)):
        return True

    return False

def tieneCaminoEuleriano(grafo):
    '''Comprueba si un grafo no dirigido tiene un camino euleriano.

	Argumentos:
		grafo: Grafo en formato de listas. 
			   Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

	Retorno:
		boolean: grafo tiene un camino euleriano

    '''
    listAristas = grafo[1]
    VertexInit = listAristas[0][0]

    for i in range(0,len(listAristas)-1):
    	VertExtremo = listAristas[i][1]
    	if((VertExtremo != listAristas[i+1][0]) or (VertexInit == listAristas[i+1][1])):
    	    return False
		

	
    for aristas in listAristas:	
        if(listAristas.count(aristas)>1):	
            return False

    return True


def cicloEuleriano(grafo):
    '''Obtiene un ciclo euleriano en un grafo no dirigido, si es posible

    Argumentos:
        grafo: Grafo en formato de listas. 
                Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Retorno:
        lista de aristas: ciclo euleriano, si existe
        None: si no existe un camino euleriano
    '''

    # Sugerencia: Usar el Algoritmo de Fleury
    # Recursos:
    # http://caminoseuler.blogspot.com.ar/p/algoritmo-leury.html
    # http://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/
    pass


def main():
    pass

if __name__ == '__main__':
    main()
