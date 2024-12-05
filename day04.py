

def part1(filename):
    key = 'XMAS'
    count = 0
    rows = []
    with open(filename, 'r') as f:
        rows = [list(line.strip()) for line in f]
    for row in range(len(rows)):
        for start in range(len(rows[row])):
            horizontal = None if start + 4 > len(rows[row]) else ''.join(rows[row][start:start + 4])
            vertical = None if row + 4 > len(rows) else ''.join([rows[i][start] for i in range(row, row + 4)])
            down_right = None if horizontal is None or vertical is None else ''.join([rows[i][start + (i - row)] for i in range(row, row + 4)])
            down_left = None if (start - 3 < 0 or vertical is None) else ''.join([rows[i][start - (i - row)] for i in range(row, row + 4)])
            if horizontal is not None and (horizontal == key or horizontal[::-1] == key):
                count += 1
            if vertical is not None and (vertical == key or vertical[::-1] == key):
                count += 1
            if down_right is not None and (down_right == key or down_right[::-1] == key):
                count += 1
            if down_left is not None and (down_left == key or down_left[::-1] == key):
                count += 1
    return count

def part2(filename):
    key = 'MAS'
    count = 0
    rows = []
    with open(filename, 'r') as f:
        rows = [list(line.strip()) for line in f]
    for row in range(0, len(rows) - 2):
        for start in range(0, len(rows[row]) - 2):
            down_right = ''.join([rows[row + i][start + i] for i in range(3)])
            down_left = ''.join([rows[row + i][start + 2 - i] for i in range(3)])
            if (down_right == key or down_right[::-1] == key) and (down_left == key or down_left[::-1] == key):
                count += 1
    return count

if __name__ == '__main__':
    print(f'Solution to Part 1: {part1('day04.txt')}')
    print(f'Solution to Part 2: {part2('day04.txt')}')