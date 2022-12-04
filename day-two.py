def get_game_lib_p1():
    my_lib = {'A X':4,'A Y':8,'A Z':3,'B X':1,'B Y':5,'B Z':9,'C X':7,'C Y':2,'C Z':6}
    return my_lib

def solve_p1():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-two.txt", "r")
    total_score = 0
    my_lib = get_game_lib_p1()
    for line in input.readlines():
        total_score = total_score + my_lib[line.rstrip()]
    return total_score

def get_game_lib_p2():
    my_lib = {'A X':3,'A Y':4,'A Z':8,'B X':1,'B Y':5,'B Z':9,'C X':2,'C Y':6,'C Z':7}
    return my_lib

def solve_p2():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-two.txt", "r")
    total_score = 0
    my_lib = get_game_lib_p2()
    for line in input.readlines():
        total_score = total_score + my_lib[line.rstrip()]
    return total_score

print(solve_p2())