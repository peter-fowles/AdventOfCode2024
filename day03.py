import re

def part1(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    mul_instructions = re.findall(r'mul\((\d*),(\d*)\)', text)
    return sum([int(ins[0]) * int(ins[1]) for ins in mul_instructions])

def part2(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    mul_instructions = re.findall(r"(don\'t|do|mul\((\d*),(\d*)\))", text)
    total = 0
    use_line = True
    for ins in mul_instructions:
        if ins[0] == 'don\'t':
            use_line = False
        elif ins[0] == 'do':
            use_line = True
        elif use_line:
            total += int(ins[1]) * int(ins[2])
    return total

if __name__ == '__main__':
    print(f'Solution to Part 1: {part1('day03.txt')}')
    print(f'Solution to Part 2: {part2('day03.txt')}')