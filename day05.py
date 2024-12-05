from random import shuffle

def is_ordered(update, ordering):
    visited = set()
    for page in update:
        for pred in ordering.get(page, []):
            if pred in visited:
                return False
        visited.add(page)
    return True

def sort_update(update, ordering):
    # implements a bubble sorting algorithm
    for i in range(len(update)):
        swapped = False
        for j in range(0, len(update) - i - 1):
            if update[j] in ordering.get(update[j + 1], []):
                update[j], update[j + 1] = update[j + 1], update[j]
        swapped = True
        if not swapped:
            break
    assert is_ordered(update, ordering)


def part1(filename):
    ordering = dict()
    updates = []
    with open(filename) as f:
        line = f.readline().strip()
        while line:
            page, before = line.split('|')
            if page not in ordering:
                ordering[page] = []
            ordering[page].append(before)
            line = f.readline().strip()
        for line in f:
            updates.append(line.strip().split(','))

    return sum(int(update[len(update) // 2]) for update in updates if is_ordered(update, ordering))

def part2(filename):
    ordering = dict()
    updates = []
    total = 0
    with open(filename) as f:
        line = f.readline().strip()
        while line:
            page, before = line.split('|')
            if page not in ordering:
                ordering[page] = []
            ordering[page].append(before)
            line = f.readline().strip()
        for line in f:
            updates.append(line.strip().split(','))
    for update in updates:
        if not is_ordered(update, ordering):
            sort_update(update, ordering)
            total += int(update[len(update) // 2])
    return total

if __name__ == '__main__':
    print(f'Solution to Part 1: {part1('day05.txt')}')
    print(f'Solution to Part 2: {part2('day05_sample.txt')}')