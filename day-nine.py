FILAS = 1000
COLUMNAS = 1000
LONGITUD_CUERDA = 9

def crea_tablero_vacio():
    tablero = []
    for f in range(FILAS):
        fila = []
        for c in range(COLUMNAS):
            fila.append('.')
        tablero.append(fila)
    return tablero

def dibuja_tablero(tablero):
    for f in range(len(tablero)):
        for c in range(len(tablero[0])):
            print(tablero[f][c],end="")
        print()
    print()

def crea_posicion_inicial(tablero, posicion):
    tablero[posicion[0]][posicion[1]] = 's'

def mueve_cuerda(tablero, movimiento, posicion_cabeza, posicion_cola):
    posiciones_visitadas = []

    for i in range(int(movimiento[1])):
        # SE ACTUALIZA LA POSICIÓN DE LA CABEZA
        if movimiento[0] == 'R':
            nueva_posicion_cabeza = [posicion_cabeza[0], int(posicion_cabeza[1]) + 1]
        elif movimiento[0] == 'L':
            nueva_posicion_cabeza = [posicion_cabeza[0], int(posicion_cabeza[1]) - 1]
        elif movimiento[0] == 'U':
            nueva_posicion_cabeza = [int(posicion_cabeza[0] - 1), posicion_cabeza[1]]
        elif movimiento[0] == 'D':
            nueva_posicion_cabeza = [int(posicion_cabeza[0] + 1), posicion_cabeza[1]]

        # SE ACTUALIZA LA POSICIÓN NUEVA DE LA COLA DEPENDIENDO DE DÓNDE ESTÉ SITUADA EN TORNO A LA CABEZA
        if (posicion_cola == posicion_cabeza):
            # ...
            # .H.
            if movimiento[0] == 'R':
                # ...    ...
                # .H. -> .TH
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'L':
                # ...    ...
                # .H. -> HT.
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'U':
                # ...    .H.
                # .H. -> .T.
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'D':
                # .H.    .T.
                # ... -> .H.
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR

        elif ((posicion_cabeza[0] == posicion_cola[0]) and (posicion_cabeza[1] == int(posicion_cola[1]) + 1)):
            # ....
            # .TH.
            # s...
            if movimiento[0] == 'R':
                # ....    .....
                # .TH. -> ..TH.
                # s...    s....
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA
            elif movimiento[0] == 'L':
                # ....    .....
                # .TH. -> ..H..
                # s...    s....
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'U':
                # ....    ..H.
                # .TH. -> .T..
                # s...    s...
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'D':
                # ....    ....
                # .TH. -> .T..
                # s...    s.H.
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR

        elif ((posicion_cabeza[0] == posicion_cola[0]) and (posicion_cabeza[1] == int(posicion_cola[1]) - 1)):
            # ....
            # .HT.
            # s...
            if movimiento[0] == 'R':
                # ....    .....
                # .HT. -> ...H.
                # s...    s....
                nueva_posicion_cola = posicion_cola # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'L':
                # ....    .....
                # .HT. -> HT...
                # s...    s....
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA
            elif movimiento[0] == 'U':
                # ....    .H..
                # .HT. -> ..T.
                # s...    s...
                nueva_posicion_cola = posicion_cola # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'D':
                # ....    ....
                # .HT. -> ..T.
                # s...    sH..
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR

        elif ((posicion_cabeza[0] == int(posicion_cola[0]) - 1) and (posicion_cabeza[1] == posicion_cola[1])):
            # ...
            # .H.
            # .T.
            # s..
            if movimiento[0] == 'R':
                # ...    ....
                # .H. -> ..H.
                # .T.    .T..
                # s..    s...
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'L':
                # ...    ....
                # .H. -> H...
                # .T.    .T..
                # s..    s...
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'U':
                # ...    .H.
                # .H. -> .T.
                # .T.    ...
                # s..    s..
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA
            elif movimiento[0] == 'D':
                # ...    ...
                # .H. -> ...
                # .T.    .H.
                # s..    s..
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR

        elif ((posicion_cabeza[0] == int(posicion_cola[0]) + 1) and (posicion_cabeza[1] == posicion_cola[1])):
            # ...
            # .T.
            # .H.
            # s..
            if movimiento[0] == 'R':
                # ...    ....
                # .T.    .T..
                # .H. -> ..H.
                # s..    s...
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'L':
                # ...    ....
                # .T.    .T..
                # .H. -> H...
                # s..    s...
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'U':
                # ...    ...
                # .T.    .H.
                # .H. -> ...
                # s..    s..
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'D':
                # ...    ...
                # .T.    ...
                # .H. -> .T.
                # s..    sH.
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA

        elif ((posicion_cabeza[0] == int(posicion_cola[0]) + 1) and (posicion_cabeza[1] == int(posicion_cola[1]) + 1)):
            # ....
            # .T..
            # ..H.
            # s...
            if movimiento[0] == 'R':
                # ....    .....
                # .T..    .....
                # ..H. -> ..TH.
                # s...    s....
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA
            elif movimiento[0] == 'L':
                # ....    .....
                # .T..    .T...
                # ..H. -> .H...
                # s...    s....
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'U':
                # ....    ....
                # .T..    .TH.
                # ..H. -> ....
                # s...    s...
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'D':
                # ....    ....
                # .T..    ....
                # ..H. -> ..T.
                # s...    s.H.
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA

        elif ((posicion_cabeza[0] == int(posicion_cola[0]) - 1) and (posicion_cabeza[1] == int(posicion_cola[1]) + 1)):
            # ....
            # ....
            # ..H.
            # sT..
            if movimiento[0] == 'R':
                # ....    .....
                # ....    .....
                # ..H. -> ..TH.
                # sT..    s....
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA
            elif movimiento[0] == 'L':
                # ....    .....
                # ....    .....
                # ..H. -> .H...
                # sT..    sT...
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'U':
                # ....    ....
                # ....    ..H.
                # ..H. -> ..T.
                # sT..    s...
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA
            elif movimiento[0] == 'D':
                # ....    ....
                # ....    ....
                # ..H. -> ....
                # sT..    sTH.
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR

        elif ((posicion_cabeza[0] == int(posicion_cola[0] + 1)) and (posicion_cabeza[1] == int(posicion_cola[1]) - 1)):
            # ....
            # ..T.
            # .H..
            # s...
            if movimiento[0] == 'R':
                # ....    ....
                # ..T.    ..T.
                # .H.. -> ..H.
                # s...    s...
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'L':
                # ....    ...
                # ..T.    ...
                # .H.. -> HT.
                # s...    s..
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA
            elif movimiento[0] == 'U':
                # ....    ....
                # ..T.    .HT.
                # .H.. -> ....
                # s...    s...
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'D':
                # ....    ....
                # ..T.    ....
                # .H.. -> .T..
                # s...    sH..
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA

        elif ((posicion_cabeza[0] == int(posicion_cola[0] - 1)) and (posicion_cabeza[1] == int(posicion_cola[1]) - 1)):
            # ....
            # ....
            # .H..
            # s.T.
            if movimiento[0] == 'R':
                # ....    ....
                # ....    ....
                # .H.. -> ..H.
                # s.T.    s.T.
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR
            elif movimiento[0] == 'L':
                # ....    ...
                # ....    ...
                # .H.. -> HT.
                # s.T.    s..
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA
            elif movimiento[0] == 'U':
                # ....    ....
                # ....    .H..
                # .H.. -> .T..
                # s.T.    s...
                nueva_posicion_cola = posicion_cabeza  # SE ACTUALIZA A LA POSICIÓN ANTERIOR DE LA CABEZA
            elif movimiento[0] == 'D':
                # ....    ....
                # ....    ....
                # .H.. -> ....
                # s.T.    sHT.
                nueva_posicion_cola = posicion_cola  # SE MANTIENE LA POSICIÓN ANTERIOR

        # ACTUALIZAMOS EL TABLERO CON LAS NUEVAS POSICIONES
        tablero[posicion_cabeza[0]][posicion_cabeza[1]] = '.'
        tablero[nueva_posicion_cola[0]][nueva_posicion_cola[1]] = 'T' # SE ACTUALIZA LA COLA
        tablero[nueva_posicion_cabeza[0]][nueva_posicion_cabeza[1]] = 'H' # SE ACTUALIZA LA CABEZA

        # SE ACTUALIZA LA POSICIÓN VISITADA POR LA COLA
        if posicion_cola[0] == FILAS-1 and posicion_cola[1] == 0: # SI LA ANTERIOR ERA LA INICIAL, SE PONE UNA 's'
            tablero[FILAS-1][0] = 's'
        elif nueva_posicion_cola != posicion_cola: # SI NO ERA LA INICIAL Y TAMPOCO LA ANTERIOR, SE PONE UN '#'
            tablero[posicion_cola[0]][posicion_cola[1]] = '#'

        # SE ACTUALIZAN LAS NUEVAS POSICIONES
        posicion_cabeza = nueva_posicion_cabeza
        posicion_cola = nueva_posicion_cola

        # SE CREA LA POSICIÓN VISITADA Y SE AÑADE A LA LISTA
        posicion_visitada = nueva_posicion_cola
        if posicion_visitada not in posiciones_visitadas:
            posiciones_visitadas.append(posicion_visitada)

        # SE DIBUJA EL TABLERO
        #dibuja_tablero(tablero)

    return [posiciones_visitadas, posicion_cabeza, posicion_cola]

def haz_movimientos(tablero):
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-nine.txt", "r")
    posiciones_totales = [] # LISTA CON LAS POSICIONES VISITADAS POR LA COLA. PEJ: ['2,3', '5,7',...]
    posicion_cola = [499,499]
    posicion_cabeza = [499,499]
    #posicion_cola = [FILAS-1,0]
    #posicion_cabeza = [FILAS-1,0]
    crea_posicion_inicial(tablero,posicion_cabeza)
    #dibuja_tablero(tablero)
    for linea in input.readlines():
        movimiento = linea.rstrip().split(' ') # SE COGE EL MOVIMIENTO DE LA LISTA DE MOVIMIENTOS
        resultado_movimiento = mueve_cuerda(tablero, movimiento, posicion_cabeza, posicion_cola) # SE HACE EL MOVIMIENTO Y SE COGE LA POSICIÓN VISITADA
        posiciones_visitadas = resultado_movimiento[0]
        posicion_cabeza = resultado_movimiento[1]
        posicion_cola = resultado_movimiento[2]
        for posicion_visitada in posiciones_visitadas:
            if posicion_visitada not in posiciones_totales: # SI LA POSICIÓN VISITADA NO ESTÁ MARCADA, SE AÑADE A LA LISTA DE MARCADAS
                posiciones_totales.append(posicion_visitada)

    return len(posiciones_totales) # SE DEVUELVE EL TOTAL DE LAS POSICIONES VISITADAS

def haz_movimientos_parte_2(tablero):
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-nine.txt", "r")
    posiciones_totales = [] # LISTA CON LAS POSICIONES VISITADAS POR LA COLA. PEJ: ['2,3', '5,7',...]
    pila_posiciones_totales = []
    posicion_cola = [499,499]
    posicion_cabeza = [499,499]
    #posicion_cola = [FILAS-1,0]
    #posicion_cabeza = [FILAS-1,0]
    crea_posicion_inicial(tablero,posicion_cabeza)
    #dibuja_tablero(tablero)
    for linea in input.readlines():
        movimiento = linea.rstrip().split(' ') # SE COGE EL MOVIMIENTO DE LA LISTA DE MOVIMIENTOS
        resultado_movimiento = mueve_cuerda(tablero, movimiento, posicion_cabeza, posicion_cola) # SE HACE EL MOVIMIENTO Y SE COGE LA POSICIÓN VISITADA
        posiciones_visitadas = resultado_movimiento[0]
        posicion_cabeza = resultado_movimiento[1]
        posicion_cola = resultado_movimiento[2]
        for posicion_visitada in posiciones_visitadas:
            if posicion_visitada not in posiciones_totales: # SI LA POSICIÓN VISITADA NO ESTÁ MARCADA, SE AÑADE A LA LISTA DE MARCADAS
                posiciones_totales.append(posicion_visitada)

    return len(posiciones_totales) # SE DEVUELVE EL TOTAL DE LAS POSICIONES VISITADAS

tablero = crea_tablero_vacio()
print(haz_movimientos_parte_2(tablero))