def read_input(filename):
    with open(filename) as file:
        return file.readline().strip('\n')


def find_marker(raw_input, marker_length):
    i = 0
    n = len(raw_input)
    while i < n - marker_length:
        s = raw_input[i: i + marker_length]
        cnt = 0
        for ch in s:
            cnt += s.count(ch)
        if cnt == marker_length:
            return i + marker_length
        i += 1
    return 0


def do_part1(raw_input):
    return find_marker(raw_input, 4)


def do_part2(raw_input):
    return find_marker(raw_input, 14)


def main():
    raw_input = read_input('input.txt')
    print('Part 1:', do_part1(raw_input))
    print('Part 2:', do_part2(raw_input))


if __name__ == '__main__':
    main()
