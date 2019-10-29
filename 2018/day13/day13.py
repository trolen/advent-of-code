#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.rstrip('\n') for line in file.readlines()]


def parse_data(data):
    grid = []
    carts = []
    y = 0
    for line in data:
        row = ''
        x = 0
        for ch in line:
            if ch in '<>^v':
                row += '-' if ch in '<>' else '|'
                carts.append((ch, x, y, 0))
            else: # ch in '-|'
                row += ch
            x += 1
        grid.append(row)
        y += 1
    return (grid, carts)


def move_cart(cart):
    (dir, x, y, cnt) = cart
    if dir == '>':
        x += 1
    elif dir == '<':
        x -= 1
    elif dir == 'v':
        y += 1
    else:  # dir == '^'
        y -= 1
    return (dir, x, y, cnt)


def perform_tick(grid, carts, remove_crashed_carts=False):
    n_carts = len(carts)
    idx = 0
    while idx < n_carts:
        (dir, x, y, cnt) = move_cart(carts[idx])
        cart_removed = False
        for idx1 in range(0, n_carts):
            (dir1, x1, y1, cnt1) = carts[idx1]
            if x1 == x and y1 == y:
                if not remove_crashed_carts:
                    return (x, y)
                del carts[idx1]
                if idx1 < idx:
                    idx -= 1
                del carts[idx]
                n_carts -= 2
                cart_removed = True
                break
        if cart_removed:
            continue
        carts[idx] = (dir, x, y, cnt)
        ch = grid[y][x]
        if ch in '-|':
            idx += 1
            continue
        if ch == '/':
            if dir in '<>':
                dir = 'v' if dir == '<' else '^'
            else:
                dir = '>' if dir == '^' else '<'
        elif ch == '\\':
            if dir in '<>':
                dir = 'v' if dir == '>' else '^'
            else:
                dir = '>' if dir == 'v' else '<'
        else:  # ch == '+'
            s = '<^>v'
            n = (cnt % 3) - 1
            i = s.find(dir) + n
            if i >= 4:
                i -= 4
            dir = s[i]
            cnt += 1
        carts[idx] = (dir, x, y, cnt)
        idx += 1
    return (None, None)


def show_grid(grid, carts):
    print('-------------------')
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            ch = grid[y][x]
            for cart in carts:
                (dir, x1, y1, cnt) = cart
                if x == x1 and y == y1:
                    ch = dir
                    break
            print(ch, end='')
        print()


def move_until_crash(data):
    (grid, carts) = parse_data(data)
    while True:
        (x, y) = perform_tick(grid, carts)
        if x is not None and y is not None:
            return (x, y)


def move_until_one_cart_left(data):
    (grid, carts) = parse_data(data)
    while len(carts) > 1:
        #show_grid(grid,carts)
        perform_tick(grid, carts, True)
    show_grid(grid, carts)
    (dir, x, y, cnt) = carts[0]
    return (x, y)


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    (x, y) = move_until_crash(raw_data)
    print('First Crash at: ({0},{1})'.format(x, y))
    (x, y) = move_until_one_cart_left(raw_data)
    print('Final cart at: ({0},{1})'.format(x, y))
