CL = [20,60,100,140,180,220,260,300,340,380,420,460,500]

def ejecuta_programa():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-ten.txt", "r")
    salida = 1
    ciclos = 0
    suma_total = 0
    for linea in input.readlines():
        if linea.rstrip()[:4] == 'noop':
            ciclos += 1
            if ciclos in CL:
                suma_total += salida * ciclos
                print(salida * ciclos)
        elif linea.rstrip()[:4] == 'addx':
            ciclos += 1
            if ciclos in CL:
                suma_total += salida * ciclos
                print(salida * ciclos)
            ciclos += 1
            if ciclos in CL:
                suma_total += salida * ciclos
                print(salida * ciclos)
            salida += int(linea.rstrip().split(' ')[1])

    return suma_total

def procesa_fin_ciclo(ciclos, SPRITE):
    if ciclos in SPRITE:
        print('#',end='')
    else:
        print('.',end='')

    ciclos += 1
    if ciclos == 40:
        ciclos = 0
        print()
    return ciclos

def dibuja_imagen():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-ten.txt", "r")
    x = 1
    ciclos = 0
    SPRITE = [0, 1, 2]
    for linea in input.readlines():
        if linea.rstrip()[:4] == 'noop':
            ciclos = procesa_fin_ciclo(ciclos, SPRITE)

        elif linea.rstrip()[:4] == 'addx':
            ciclos = procesa_fin_ciclo(ciclos, SPRITE)
            ciclos = procesa_fin_ciclo(ciclos, SPRITE)
            x += int(linea.rstrip().split(' ')[1])
            SPRITE = [x-1,x,x+1]


print(ejecuta_programa()) # PARTE 1
dibuja_imagen() # PARTE 2