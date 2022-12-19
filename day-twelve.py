ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','E']

def crea_mapa():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-twelve.txt", "r")
    mapa = []
    for linea in input.readlines():
        fila = list(linea.rstrip())
        mapa.append(fila)
    return mapa

def dibuja_mapa(mapa):
    for fila in mapa:
        print(fila)

def dame_posicion_inicial(mapa):
    for i_f in range(len(mapa)):
        for i_c in range(len(mapa[0])):
            if mapa[i_f][i_c] == 'S':
                return [i_f,i_c]

def dame_posicion_final(mapa):
    for i_f in range(len(mapa)):
        for i_c in range(len(mapa[0])):
            if mapa[i_f][i_c] == 'E':
                return [i_f,i_c]

def dame_posiciones_adjacentes_posibles(mapa, p_ant, p_act):
    fila = p_act[0]
    columna = p_act[1]
    posiciones_adjacentes = []
    for f in range(fila-1,fila+2):
        if f > len(mapa)-1:
            continue
        p_adj = []
        p_adj.append(f)
        p_adj.append(columna)
        if p_adj == p_ant or p_adj == p_act or p_adj[0] < 0 or p_adj[1] < 0:
            continue

        letra_actual = mapa[p_act[0]][p_act[1]]
        if letra_actual == 'S':
            letra_actual = 'a'
        indice_letra_actual = ABC.index(letra_actual)
        letra_siguiente = ABC[indice_letra_actual+1]
        letra_adjacente = mapa[p_adj[0]][p_adj[1]]

        if letra_adjacente == letra_actual or letra_adjacente == letra_siguiente:
            posiciones_adjacentes.append(p_adj)

    for c in range(columna-1,columna+2):
        if c > len(mapa[0])-1:
            continue
        p_adj = []
        p_adj.append(fila)
        p_adj.append(c)
        if p_adj == p_ant or p_adj == p_act or p_adj[0] < 0 or p_adj[1] < 0:
            continue

        letra_actual = mapa[p_act[0]][p_act[1]]
        if letra_actual == 'S':
            letra_actual = 'a'
        indice_letra_actual = ABC.index(letra_actual)
        letra_siguiente = ABC[indice_letra_actual + 1]
        letra_adjacente = mapa[p_adj[0]][p_adj[1]]

        if letra_adjacente == letra_actual or letra_adjacente == letra_siguiente:
            posiciones_adjacentes.append(p_adj)

    return posiciones_adjacentes

def mejor_camino(mapa, p_ant, p_act, p_fin, pasos):

    if p_act == p_fin:
        print(pasos)
        return 0
    else:
        for p_adj_posible in dame_posiciones_adjacentes_posibles(mapa,p_ant,p_act):
            print(p_adj_posible)
            mejor_camino(mapa, p_act, p_adj_posible, p_fin, pasos+1)
    pasos -= 1
    #mejor_camino(mapa,p_ant,p_act,p_fin,pasos-1)

mapa = crea_mapa()
dibuja_mapa(mapa)
p_ini = dame_posicion_inicial(mapa)
p_fin = dame_posicion_final(mapa)
print(dame_posiciones_adjacentes_posibles(mapa,p_ini, p_ini))
print(mejor_camino(mapa, p_ini, p_ini, p_fin, 0))
