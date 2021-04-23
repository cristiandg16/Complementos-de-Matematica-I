def make_set(lista):
    '''
    Inicializa un conjunto (Lista) de modo de que todos sus elementos pasen 
    a ser conjuntos unitarios. 
    Retorna un disjointSet
    '''
    dS = {}
    
    for i in range (0,len(lista)):
        dS[lista[i]] = i
    return dS	

    

def find(elem, disjoint_set):
    '''
    Obtiene la clave correspondiente al conjunto al que pertenece 
    el elemento 'elem'
    '''
    
    for key in disjoint_set:
        if(disjoint_set[key] == elem):
            return key

    

def union(id_1, id_2, disjoint_set):
    '''
    Une los conjuntos con identificadores id_1, id_2.
    Retorna la estructura actualizada
    '''

    disjoint_set[id_2] = [get(id_1)+get(id_2)]
    
    return disjoint_set


