def get_game_lib_p1():
    my_lib = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9
              ,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17
                 ,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,
              'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36
        ,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47
        ,'V':48,'W':49,'X':50,'Y':51,'Z':52}
    return my_lib

def to_solve_p1():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-three.txt", "r")
    total_priority = 0
    my_lib = get_game_lib_p1()
    for line in input.readlines():
        backpack = list(line.rstrip())
        capacity = int(len(backpack)/2)
        compartment_1 = backpack[:capacity]
        compartment_2 = backpack[capacity:]
        elements = compare(compartment_1,compartment_2)
        for ele in elements:
            total_priority = total_priority + my_lib[ele]

    return total_priority

def to_solve_p2():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-three.txt", "r")
    total_priority = 0
    loop_var = 0
    group = []
    for line in input.readlines():
        if loop_var == 2:
            group.append(list(line.rstrip()))
            total_priority = total_priority + solve_group(group)
            group = []
            loop_var = 0
        else:
            group.append(list(line.rstrip()))
            loop_var = loop_var + 1

    return total_priority

def solve_group(group_list):
    my_lib = get_game_lib_p1()
    value = 0
    aux_list = compare(group_list[0],group_list[1])
    elements = compare(aux_list,group_list[2])
    for ele in elements:
        value = value + my_lib[ele]

    return value

def compare(list_1, list_2):
    elements = []
    for elem_1 in list_1:
        for elem_2 in list_2:
            if elem_1 == elem_2:
                if elem_1 not in elements:
                    elements.append(elem_1)

    return elements

print(to_solve_p2())