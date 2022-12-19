class my_tree(object):
    def __init__(self):
        self.nombre = None
        self.padre = None
        self.hijos = None
        self.dim = None

def crea_arbol():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-seven.txt", "r")
    nodo_actual = None
    for linea in input.readlines():
        if linea.rstrip()[:4] == '$ cd': # SE MUEVE UN DIRECTORIO

            if linea.rstrip()[5:] == '..': # Se vuelve al directorio anterior
                nodo_actual = nodo_actual.padre # Apuntamos al nodo padre del actual
            else: # Se va a un directorio hijo
                siguiente_nodo = crea_nodo(linea.rstrip()[5:], nodo_actual, [], 0)
                agrega_hijo(nodo_actual, siguiente_nodo)
                nodo_actual = siguiente_nodo # Apuntamos al siguiente nodo que vamos a entrar
            continue

        if linea.rstrip()[:1] != '$': # EL DIRECTORIO CONTIENE UN ARCHIVO O UN DIRECTORIO
            if linea.rstrip().split(' ')[0] != 'dir': # SE TRATA DE UN ARCHIVO
                actualiza_dimension(nodo_actual, int(linea.rstrip().split(' ')[0])) # Actualizamos la dimension del nodo y de sus padres
            continue

    return busca_raiz(nodo_actual) # Devolvemos la raíz del árbol creado

def crea_nodo(nombre, padre, hijos, dim):
    nodo = my_tree()
    nodo.nombre = nombre
    nodo.padre = padre
    nodo.hijos = hijos
    nodo.dim = dim
    return nodo

def agrega_hijo(nodo_padre, nodo_hijo):
    if nodo_padre is not None:
        nodo_padre.hijos.append(nodo_hijo)

def actualiza_dimension(nodo, dimension):
    nodo.dim = nodo.dim + dimension
    if nodo.padre is not None:
        actualiza_dimension(nodo.padre, dimension)

def busca_raiz(nodo):
    if nodo.nombre == '/':
        return nodo
    else:
        return busca_raiz(nodo.padre)

def recorre_arbol(nodo):
    if nodo is None:
        return 0
    print(nodo.nombre, nodo.dim)
    for hijo in nodo.hijos:
        recorre_arbol(hijo)

def suma_dimensiones_nodos(nodo):
    if nodo is None:
        return 0
    if nodo.dim <= 100000:
        print(nodo.dim)
    for hijo in nodo.hijos:
        suma_dimensiones_nodos(hijo)

def busca_directorio_para_borrar(nodo):
    if nodo is None:
        return 0
    if nodo.dim + 21955498 >= 30000000:
        print(nodo.dim)
    for hijo in nodo.hijos:
        busca_directorio_para_borrar(hijo)

suma_dimensiones_nodos(crea_arbol()) # Resuelve parte uno (coger la suma de todos los valores de la salida en consola)
busca_directorio_para_borrar(crea_arbol()) # Resuelve parte dos (coger el valor más pequeño de la salida en consola)