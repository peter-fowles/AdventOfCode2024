
def part1(filename):
    left_nums = []
    right_nums = []

    with open(filename, 'r') as f:
        for line in f:
            left, right = line.strip().split('   ')
            left, right = int(left), int(right)
            left_nums.append(left)
            right_nums.append(right)

    left_sorted = sorted(left_nums)
    right_sorted = sorted(right_nums)

    total = sum([abs(left_sorted[i] - right_sorted[i]) for i in range(len(left_sorted))])

    return total

def part2(filename):
    left_nums = []
    right_nums = []

    with open(filename, 'r') as f:
        for line in f:
            left, right = line.strip().split('   ')
            left, right = int(left), int(right)
            left_nums.append(left)
            right_nums.append(right)

        score = sum([left_nums[i] * right_nums.count(left_nums[i]) for i in range(len(left_nums))])
        return score
    

if __name__ == '__main__':
    print(f'Solution to Part 1: {part1('day01.txt')}')
    print(f'Solution to Part 2: {part2('day01.txt')}')