def to_solve_p1():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-four.txt", "r")
    pairs = 0
    for line in input.readlines():
        pair = line.rstrip().split(',')
        elf_1 = pair[0].split('-') # p ej: ['2','4']
        elf_2 = pair[1].split('-') # p ej: ['6','8']
        if fully_contains(elf_1,elf_2) or fully_contains(elf_2,elf_1):
            pairs = pairs + 1

    return pairs

def fully_contains(list_1, list_2):
    return ((int(list_1[0]) <= int(list_2[0])) and (int(list_1[1]) >= int(list_2[1])))

def partial_contains(list_1, list_2):
    return ((int(list_1[1]) >= int(list_2[0])) and (int(list_2[1]) >= int(list_1[0])))

def to_solve_p2():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-four.txt", "r")
    pairs = 0
    for line in input.readlines():
        pair = line.rstrip().split(',')
        elf_1 = pair[0].split('-')  # p ej: ['2','4']
        elf_2 = pair[1].split('-')  # p ej: ['6','8']
        if fully_contains(elf_1, elf_2) or fully_contains(elf_2, elf_1) \
                or partial_contains(elf_1,elf_2) or partial_contains(elf_2,elf_1):
            pairs = pairs + 1

    return pairs

print(to_solve_p2())