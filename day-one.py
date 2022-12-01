def solve_p1():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-one.txt", "r")
    sum = 0
    list = []
    for line in input.readlines():
        if line == '\n':
            list.append(sum)
            sum = 0
        else:
            sum = sum + int(line)
    return max(list)

def solve_p2():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2022\\venv\\input-files\\input-day-one.txt", "r")
    cal = 0
    list = []
    for line in input.readlines():
        if line == '\n':
            list.append(cal)
            cal = 0
        else:
            cal = cal + int(line)
    list.append(cal)
    list.sort(reverse=True)
    return sum(list[:3])

print(solve_p2())