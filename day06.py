import re

def part1(filename):
    rows = []
    guard_states = ['<', '^', '>', 'v']
    guard_pos = [0, 0]
    guard_state = ''
    with open(filename, 'r') as f:
        y = 0
        for line in f:
            row = []
            x = 0
            for c in line.strip():
                row.append(c)
                if c in guard_states:
                    guard_pos = [x, y]
                    guard_state = c
                x += 1
            y += 1
            rows.append(row)
    count = 0
    while 0 <= guard_pos[0] < len(rows[0]) and 0 <= guard_pos[1] < len(rows):
        next_pos = [guard_pos[0], guard_pos[1]]
        if guard_state == '<':
            next_pos[0] -= 1
        elif guard_state == '^':
            next_pos[1] -= 1
        elif guard_state == '>':
            next_pos[0] += 1
        elif guard_state == 'v':
            next_pos[1] += 1
        if 0 <= next_pos[0] < len(rows[0]) and 0 <= next_pos[1] < len(rows) and rows[next_pos[1]][next_pos[0]] == '#':
            guard_state = guard_states[0] if guard_states.index(guard_state) + 1 >= len(guard_states) else guard_states[guard_states.index(guard_state) + 1]
        else:
            rows[guard_pos[1]][guard_pos[0]] = 'X'
            guard_pos = [next_pos[0], next_pos[1]]
    for row in rows:
        count += len([item for item in row if item == 'X'])
    return count

def part2(filename):
    rows = []
    guard_states = ['<', '^', '>', 'v']
    guard_pos = [0, 0]
    guard_state = ''
    with open(filename, 'r') as f:
        y = 0
        for line in f:
            row = []
            x = 0
            for c in line.strip():
                row.append(c)
                if c in guard_states:
                    guard_pos = [x, y]
                    guard_state = c
                x += 1
            y += 1
            rows.append(row)
    count = 0
    original_guard_pos = [i for i in guard_pos]
    original_guard_state = guard_state
    original_rows = [[x for x in y] for y in rows]
    for y in range(len(original_rows)):
        for x in range(len(original_rows[y])):
            if rows[y][x] == '#' or (guard_pos[0] == x and guard_pos[1] == y):
                continue
            rows[y][x] = '#'
            seen_states = set()
            while 0 <= guard_pos[0] < len(rows[0]) and 0 <= guard_pos[1] < len(rows):
                seen_states.add((guard_state, guard_pos[0], guard_pos[1]))
                next_pos = [guard_pos[0], guard_pos[1]]
                if guard_state == '<':
                    next_pos[0] -= 1
                elif guard_state == '^':
                    next_pos[1] -= 1
                elif guard_state == '>':
                    next_pos[0] += 1
                elif guard_state == 'v':
                    next_pos[1] += 1
                if 0 <= next_pos[0] < len(rows[0]) and 0 <= next_pos[1] < len(rows) and rows[next_pos[1]][next_pos[0]] == '#':
                    guard_state = guard_states[0] if guard_states.index(guard_state) + 1 >= len(guard_states) else guard_states[guard_states.index(guard_state) + 1]
                else:
                    rows[guard_pos[1]][guard_pos[0]] = 'X'
                    guard_pos = [next_pos[0], next_pos[1]]
                if (guard_state, guard_pos[0], guard_pos[1]) in seen_states:
                    count += 1
                    break
            rows = [[col for col in row] for row in original_rows]
            guard_pos = [original_guard_pos[0], original_guard_pos[1]]
            guard_state = original_guard_state
    return count

if __name__ == '__main__':
    print(f'Solution to Part 1: {part1('day06.txt')}')
    print(f'Solution to Part 2: {part2('day06.txt')}')