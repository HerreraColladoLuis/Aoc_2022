import copy
NUMEROS = ['0','1','2','3','4','5','6','7','8','9']

def resuelve_problema():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-thirteen.txt", "r")
    indice_parejas = 1
    primer_elemento = True
    suma_total = 0
    for linea in input.readlines():
        if linea == '\n':
            indice_parejas += 1
            primer_elemento = True
            continue
        if primer_elemento:
            elem_1 = procesa(linea.rstrip(),1)[0]
            print(elem_1)
            primer_elemento = False
        else:
            elem_2 = procesa(linea.rstrip(),1)[0]
            print(elem_2,end='')
            print('\n')
            if haz_comparacion(elem_1,elem_2) == 1:
                suma_total += indice_parejas

    return suma_total

def resuelve_parte_2():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-thirteen.txt", "r")
    clasificacion = []
    for linea in input.readlines():
        if linea == '\n':
            continue
        else:
            lista = eval(linea)
            clasifica(lista, clasificacion)
            #print(clasificacion)

    lista_indice_1 = eval('[[2]]')
    lista_indice_2 = eval('[[6]]')
    i_1 = clasifica(lista_indice_1, clasificacion)
    i_2 = clasifica(lista_indice_2, clasificacion)
    for li in clasificacion:
        print(li)
    return (i_1+1)*(i_2+1)

def clasifica(lista, clasificacion): # DIVIDE Y VENCERÁS
    inicio = 0
    final = len(clasificacion)
    while inicio != final:
        l = ((final - inicio) // 2) + inicio
        lista_aux_1 = copy.deepcopy(lista)
        lista_aux_2 = copy.deepcopy(clasificacion[l])
        if haz_comparacion(lista_aux_2,lista_aux_1) == 1:
            inicio = l+1
        else:
            final = l

    clasificacion.insert(inicio, lista)
    return inicio

def haz_comparacion(lista_1,lista_2):
    while len(lista_1) > 0:
        if len(lista_2) == 0:
            return -1
        e1 = lista_1.pop(0)
        e2 = lista_2.pop(0)
        comparacion = compara(e1,e2)
        if comparacion == 1:
            return 1
        elif comparacion == -1:
            return -1
        else:
            return haz_comparacion(lista_1,lista_2)
    if len(lista_2) == 0:
        return 0
    else:
        return 1

def compara(e_1,e_2):
    if type(e_1) is int and type(e_2) is int:
        if e_1 < e_2:
            return 1
        elif e_1 > e_2:
            return -1
        else:
            return 0
    elif type(e_1) is list and type(e_2) is list:
        return haz_comparacion(e_1, e_2)
    elif type(e_1) is int and type(e_2) is list:
        a = []
        b = e_2
        a.append(e_1)
        return haz_comparacion(a,b)
    elif type(e_1) is list and type(e_2) is int:
        a = e_1
        b = []
        b.append(e_2)
        return haz_comparacion(a,b)

def procesa(linea,p):
    lista = []
    while p < len(linea):
        if linea[p] == ']':
            return (lista,p)
        elif linea[p] in NUMEROS:
            if linea[p+1] in NUMEROS:
                numero = int(linea[p]+linea[p+1])
                p += 1
            else:
                numero = int(linea[p])
            lista.append(numero)
        elif linea[p] == '[':
            resultado = procesa(linea,p+1)
            lista.append(resultado[0])
            p = resultado[1]
        p += 1

#print(resuelve_problema())

linea = '[1,2,[2,[3,5]],3]'
lista = eval(linea)
print(resuelve_parte_2())
#linea = '[10,[2,[3,[4,[5,6,7]]]],8,9]'
#print(procesa(linea,1)[0])
#parsea_linea('[1,2,[2,[3,5]],3]',1,ELEM,[])
#print(ELEM)