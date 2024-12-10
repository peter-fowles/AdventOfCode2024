
def part1(filename):
    fs = []
    line = []
    with open(filename, 'r') as f:
        line = [int(c) for c in f.readline().strip()]
    curr_label = 0
    is_open = False
    for c in line:
        for _ in range(c):
            if is_open:
                fs.append('.')
            else:
                fs.append(str(curr_label))
        if not is_open:
            curr_label += 1
        is_open = not is_open
    start = 0
    end = len(fs) - 1
    while end > start:
        if fs[start] != '.':
            start += 1
        if fs[end] == '.':
            end -= 1
        if fs[start] == '.' and fs[end] != '.':
            fs[start], fs[end] = fs[end], fs[start]
    
    checksum = 0
    for i in range(len(fs)):
        if fs[i] == '.':
            break
        checksum += i * int(fs[i])
    return checksum

def part2(filename):
    fs = []
    line = []
    with open(filename, 'r') as f:
        line = [int(c) for c in f.readline().strip()]
    curr_label = 0
    is_open = False
    for c in line:
        for _ in range(c):
            if is_open:
                fs.append('.')
            else:
                fs.append(str(curr_label))
        if not is_open:
            curr_label += 1
        is_open = not is_open
    start = 0
    curr_label -= 1
    while curr_label > 0:
        if 'sample' in filename:
            print(''.join(fs))
        print(f'curr_label: {curr_label}', end='\r')
        next_block_start = fs.index(str(curr_label))
        next_block_end = next_block_start + 1
        while next_block_end < len(fs) and fs[next_block_end] == str(curr_label):
            next_block_end += 1
        block_len = next_block_end - next_block_start
        moved = False
        start = 0
        for start in range(next_block_start - block_len + 1):
            if fs[start:start + block_len] == ['.' for _ in range(block_len)]:
                for i in range(start, start + block_len):
                    fs[i] = str(curr_label)
                    fs[next_block_start + (i - start)] = '.'
                    moved = True
            if moved: 
                break
        curr_label -= 1
    if 'sample' in filename:
        print(''.join(fs))
    checksum = 0 
    for i in range(len(fs)):
        if fs[i] == '.':
            continue
        checksum += i * int(fs[i])
    return checksum

if __name__ == '__main__':
    print(f'Solution to Part 1: {part1('day09.txt')}')
    print(f'Solution to Part 2: {part2('day09.txt')}')