def to_solve_p1():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-six.txt", "r")
    buffer = input.readline().rstrip()
    char_counter = 14
    while True:
        if find_marker(buffer[:14]):
            return char_counter
        else:
            buffer = buffer[1:]
            char_counter = char_counter + 1

def find_marker(buffer):
    buffer_list = list(buffer)
    for c in buffer_list:
        buffer_list_aux = list(buffer)
        buffer_list_aux.remove(c)
        if c in buffer_list_aux:
            return False
    return True

print(to_solve_p1())