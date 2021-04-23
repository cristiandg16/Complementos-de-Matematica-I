#! /usr/bin/python

# 2da Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

# Un disjointSet lo representaremos como un diccionario. 
# Ejemplo: {'A':1, 'B':2, 'C':1} (Nodos A y C pertenecen al conjunto 
# identificado con 1, B al identificado on 2)

def make_set(lista):
    '''
    Inicializa un conjunto (Lista) de modo de que todos sus elementos pasen 
    a ser conjuntos unitarios. 
    Retorna un disjointSet
    '''

	for i in lista:
	    dS = {'i': lista[i]} + dS
	print(dS)	

    pass


def find(elem, disjoint_set):
    '''
    Obtiene el identificador correspondiente al conjunto al que pertenece 
    el elemento 'elem'
    '''
    pass


def union(id_1, id_2, disjoint_set):
    '''
    Une los conjuntos con identificadores id_1, id_2.
    Retorna la estructura actualizada
    '''
    pass


def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo formato salida: 
        [['a, 'b'], ['c'], ['d']]
    '''
    pass



def main():
    pass

if __name__ == '__main__':
    main()
