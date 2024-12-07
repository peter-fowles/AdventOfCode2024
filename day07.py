def is_solvable_1(line, answer, curr_solution=0):
    if curr_solution == answer and len(line) == 0:
        return True
    if len(line) == 0 or curr_solution > answer:
        return False
    return is_solvable_1(line[1:], answer, curr_solution + line[0]) or (curr_solution != 0 and is_solvable_1(line[1:], answer, curr_solution * line[0]))

def is_solvable_2(line, answer, curr_solution=0):
    if curr_solution == answer and len(line) == 0:
        return True
    if len(line) == 0 or curr_solution > answer:
        return False
    concat = int(str(curr_solution) + str(line[0]))
    return is_solvable_2(line[1:], answer, curr_solution + line[0]) or (curr_solution != 0 and is_solvable_2(line[1:], answer, curr_solution * line[0])) or \
        is_solvable_2(line[1:], answer, concat)

def part1(filename):
    lines = []
    result = 0
    with open(filename, 'r') as f:
        lines = [[int(i) for i in line.replace(':', '').split()] for line in f]
    for line in lines:
        if is_solvable_1(line[1:], line[0]):
            result += line[0]
    return result
        

def part2(filename):
    lines = []
    result = 0
    with open(filename, 'r') as f:
        lines = [[int(i) for i in line.replace(':', '').split()] for line in f]
    for line in lines:
        if is_solvable_2(line[1:], line[0]):
            result += line[0]
    return result

if __name__ == '__main__':
    print(f'Solution to Part 1: {part1('day07.txt')}')
    print(f'Solution to Part 2: {part2('day07.txt')}')