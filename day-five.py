def to_solve_p1():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-five.txt", "r")
    stacks = [[],[],[],[],[],[],[],[],[]]
    movements = False
    result = ''

    for line in input.readlines():
        line = line.rstrip()
        if not line:  # Empiezan los movimientos en la siguiente linea
            movements = True
            continue
        if line[1] == '1': # Se han acabado las cajas y hay que invertir las listas
            for stack in stacks:
                stack.reverse()
            continue
        if not movements: # Descripción de las pilas
            iteration_crates_map = parse_stack_line(line)
            update_crates_stacks_with_map(stacks, iteration_crates_map)
        else: # Descripción de los movimientos
            iteration_crates_list = parse_movement_line(line)
            update_crates_stacks_with_movement(stacks, iteration_crates_list)

    # Se forma una cadena con el último elemento de cada lista
    for stack in stacks:
        result = result + stack[len(stack)-1]

    return result

def to_solve_p2():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-five.txt", "r")
    stacks = [[],[],[],[],[],[],[],[],[]]
    movements = False
    result = ''

    for line in input.readlines():
        line = line.rstrip()
        if not line:  # Empiezan los movimientos en la siguiente linea
            movements = True
            continue
        if line[1] == '1': # Se han acabado las cajas y hay que invertir las listas
            for stack in stacks:
                stack.reverse()
            continue
        if not movements: # Descripción de las pilas
            iteration_crates_map = parse_stack_line(line)
            update_crates_stacks_with_map(stacks, iteration_crates_map)
        else: # Descripción de los movimientos
            iteration_crates_list = parse_movement_line(line)
            update_crates_stacks_with_movement_2(stacks, iteration_crates_list)

    # Se forma una cadena con el último elemento de cada lista
    for stack in stacks:
        result = result + stack[len(stack)-1]

    return result

# Devuelve un mapa del tipo {'A':1,'D':5} que significa que la caja A
# va en la pila 1 y la caja D va en la pila 5
def parse_stack_line(line):
    crates_map = []
    stack = 0
    pos = 0
    end_line = False
    while True:
        c = line[pos]
        if pos % 4 == 0 and not c.isspace():
            # Sí que hay caja así que se crea la entrada en el mapa del tipo {'A':1}
            crate_list = []
            crate_list.append(line[pos + 1])
            crate_list.append(stack)
            crates_map.append(crate_list)

        # Se actualiza la posición a la siguiente entrada donde se encuentre una caja
        stack = stack + 1
        pos = pos + 4
        # Condición de salida del bucle
        if pos >= len(line):
            break

    return crates_map

# Actualiza las pilas dado un mapa del tipo anterior
def update_crates_stacks_with_map(stacks, iteration_crates_map):
    for crate_list in iteration_crates_map:
        stacks[int(crate_list[1])].append(crate_list[0])

# Devuelve una lista del tipo [1,2,1] que significa que
# se coge 1 elemento de la pila 2 y se lleva a la pila 1
def parse_movement_line(line):
    iteration_crates_tuple = []

    line_list = line.split()
    line_list.pop(0)
    line_list.pop(1)
    line_list.pop(2)

    return line_list

# Actualiza las pilas con el movimiento anterior
def update_crates_stacks_with_movement(stacks, iteration_crates_list):
    for i in range(0,int(iteration_crates_list[0])):
        elem = stacks[int(iteration_crates_list[1])-1].pop()
        stacks[int(iteration_crates_list[2])-1].append(elem)

# Actualiza las pilas con el movimiento anterior
def update_crates_stacks_with_movement_2(stacks, iteration_crates_list):
    new_list = []
    for i in range(0,int(iteration_crates_list[0])):
        elem = stacks[int(iteration_crates_list[1])-1].pop()
        new_list.append(elem)

    new_list.reverse()
    stacks[int(iteration_crates_list[2])-1].extend(new_list)

print(to_solve_p2())