def crea_matriz():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-eigth.txt", "r")
    matriz = []
    for linea in input.readlines():
        fila = list(linea.rstrip())
        print(fila)
        matriz.append(fila)
    return matriz

def arboles_visibles_en_extremos(matriz):
    arboles_visibles = len(matriz)*2 + (len(matriz[0])*2 - 4)
    return arboles_visibles

def arboles_visibles_en_medio(matriz):
    arboles_visibles = 0
    for i_f in range(len(matriz)):
        for i_c in range(len(matriz[0])):
            if i_f == 0 or i_f == len(matriz)-1:
                continue
            if i_c == 0 or i_c == len(matriz[0])-1:
                continue
            fila = matriz[i_f]
            columna = dame_columna_por_indice(matriz, i_c)

            if es_visible(fila, i_c):
                arboles_visibles += 1
            elif es_visible(columna, i_f):
                arboles_visibles += 1

    return arboles_visibles

def arboles_visibles_para_montar_casa(matriz):
    arboles_visibles = 0
    for i_f in range(len(matriz)):
        for i_c in range(len(matriz[0])):
            fila = matriz[i_f]
            columna = dame_columna_por_indice(matriz, i_c)

            max_arboles = dame_arboles_visibles(fila, i_c, columna, i_f)
            if max_arboles > arboles_visibles:
                arboles_visibles = max_arboles

    return arboles_visibles

def dame_arboles_visibles(fila, i_c, columna, i_f):
    arboles_visibles_izq = 0
    arboles_visibles_der = 0
    arboles_visibles_arr = 0
    arboles_visibles_aba = 0
    x = i_c - 1
    while x > -1: # SE SACAN LOS ÁRBOLES HACIA LA IZQUIERDA
        if int(fila[x]) >= int(fila[i_c]):
            arboles_visibles_izq += 1
            break
        x -= 1
        arboles_visibles_izq += 1

    x = i_c + 1
    while x < len(fila): # SE SACAN LOS ÁRBOLES HACIA LA DERECHA
        if int(fila[x]) >= int(fila[i_c]):
            arboles_visibles_der += 1
            break
        x += 1
        arboles_visibles_der += 1

    x = i_f - 1
    while x > -1: # SE SACAN LOS ARBOLES HACIA ARRIBA
        if int(columna[x]) >= int(columna[i_f]):
            arboles_visibles_arr += 1
            break
        x -= 1
        arboles_visibles_arr += 1

    x = i_f + 1
    while x < len(columna): # SE SACAN LOS ÁRBOLES HACIA ABAJO
        if int(columna[x]) >= int(columna[i_f]):
            arboles_visibles_aba += 1
            break
        x += 1
        arboles_visibles_aba += 1

    return arboles_visibles_izq*arboles_visibles_der*arboles_visibles_arr*arboles_visibles_aba

def es_visible(lista, indice):
    izq = True
    der = True
    x = indice-1
    while x > -1: # SE COMPRUEBA SI SE VE DESDE LA IZQUIERDA
        if int(lista[x]) >= int(lista[indice]):
            izq = False
            break
        x -= 1

    if izq:
        return izq

    x = indice+1
    while x < len(lista): # SE COMPRUEBA SI SE VE DESDE LA DERECHA
        if int(lista[x]) >= int(lista[indice]):
            der = False
            break
        x += 1
    return der

def dame_columna_por_indice(matriz, i_c):
    columna = []
    for i_f in range(len(matriz)):
        columna.append(matriz[i_f][i_c])
    return columna

matriz = crea_matriz()
extremos = arboles_visibles_en_extremos(matriz)
medio = arboles_visibles_en_medio(matriz)
maximo_arboles_visibles = arboles_visibles_para_montar_casa(matriz)

print(extremos)
print(medio)
print(medio+extremos) # RESULTADO PARTE 1
print(maximo_arboles_visibles) # RESULTADO PARTE 2
