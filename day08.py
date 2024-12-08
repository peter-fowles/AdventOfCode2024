
def part1(filename):
    antennae = {}
    grid = []
    with open(filename, 'r') as f:
        y = 0
        for line in f:
            grid.append(list(line.strip()))
            for x in range(len(grid[y])):
                curr_cell = grid[y][x]
                if curr_cell != '.':
                    if curr_cell not in antennae:
                        antennae[curr_cell] = []
                    antennae[curr_cell].append((x, y))
            y += 1
    for antenna, positions in antennae.items():
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                a, b = positions[i], positions[j]
                antinode_1 = (a[0] + (a[0] - b[0]), a[1] + (a[1] - b[1]))
                antinode_2 = (b[0] + (b[0] - a[0]), b[1] + (b[1] - a[1]))
                if 0 <= antinode_1[0] < len(grid[0]) and 0 <= antinode_1[1] < len(grid):
                    grid[antinode_1[1]][antinode_1[0]] = '#'
                if 0 <= antinode_2[0] < len(grid[0]) and 0 <= antinode_2[1] < len(grid):
                    grid[antinode_2[1]][antinode_2[0]] = '#'
    return sum([len([c for c in line if c == '#']) for line in grid])

def part2(filename):
    antennae = {}
    grid = []
    with open(filename, 'r') as f:
        y = 0
        for line in f:
            grid.append(list(line.strip()))
            for x in range(len(grid[y])):
                curr_cell = grid[y][x]
                if curr_cell != '.':
                    if curr_cell not in antennae:
                        antennae[curr_cell] = []
                    antennae[curr_cell].append((x, y))
            y += 1
    for antenna, positions in antennae.items():
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                a, b = positions[i], positions[j]
                antinode_1 = (a[0] + (a[0] - b[0]), a[1] + (a[1] - b[1]))
                antinode_2 = (b[0] + (b[0] - a[0]), b[1] + (b[1] - a[1]))
                while 0 <= antinode_1[0] < len(grid[0]) and 0 <= antinode_1[1] < len(grid):
                    grid[antinode_1[1]][antinode_1[0]] = '#'
                    antinode_1 = (antinode_1[0] + (a[0] - b[0]), antinode_1[1] + (a[1] - b[1]))
                while 0 <= antinode_2[0] < len(grid[0]) and 0 <= antinode_2[1] < len(grid):
                    grid[antinode_2[1]][antinode_2[0]] = '#'
                    antinode_2 = (antinode_2[0] + (b[0] - a[0]), antinode_2[1] + (b[1] - a[1]))
    return sum([len([c for c in line if c != '.']) for line in grid])

if __name__ == '__main__':
    print(f'Solution to Part 1: {part1('day08.txt')}')
    print(f'Solution to Part 2: {part2('day08.txt')}')