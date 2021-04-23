def esCaminoEuleriano(grafo, camino):
    '''Comprueba si una lista de aristas constituye un camino euleriano
	en un grafo.

	Argumentos:
		grafo: Grafo en formato de listas. 
			   Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

		camino: Lista de aristas. Posible camino.
				Ej: [('a', 'b), ('b', 'c')]

        Retorno:
        boolean: camino es camino euleriano en grafo

    '''
    AristaInicial = list(camino[0])
	VerticeInicial = AristaInicial[0]
	#for aristas in camino:
    print(VerticeInicial)

	#for aristas in camino:	#recorremos las aristas del camino pasado como argumento.
        #        if(camino.count(arista)>1):	#si se repite alguna ya no es un camino de euler
        #               return False

    return True
