def all_increasing(report):
    if len(report) <= 1:
        return True
    return report[0] < report[1] and all_increasing(report[1:])

def all_decreasing(report):
    if len(report) <= 1:
        return True
    return report[0] > report[1] and all_decreasing(report[1:])

def levels_safe(report):
    if len(report) <= 1:
        return True
    return 1 <= abs(report[0] - report[1]) <= 3 and levels_safe(report[1:])

def safe(report):
    return levels_safe(report) and (all_increasing(report) or all_decreasing(report))

def part1(filename):
    reports = []

    with open(filename, 'r') as f:
        for line in f:
            reports.append([int(lv) for lv in line.split(' ')])

    return len([report for report in reports if safe(report)])

def part2(filename):
    safe_count = 0
    reports = []

    with open(filename, 'r') as f:
        for line in f:
            reports.append([int(lv) for lv in line.split(' ')])
    
    for report in reports:
        if not safe(report):
            for i in range(len(report)):
                if safe(report[:i] + report[i + 1:]):
                    safe_count += 1
                    break
        else:
            safe_count += 1

    return safe_count
        


if __name__ == '__main__':
    print(f'Solution to Part 1: {part1('day02.txt')}')
    print(f'Solution to Part 2: {part2('day02.txt')}')