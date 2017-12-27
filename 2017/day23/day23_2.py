#! /usr/bin/env python3

def main():
    a = 0
    b,c,d,e,f,g,h = (107900,124900,0,0,0,0,0)
    # b = 107900 = b * 100 + 100000
    # c = 124900 = b + 17000

    for n in range(b, c + 1, 17):
        for x in range(2, n):
            if n % x == 0:
                h += 1
                break
    return h


if __name__ == '__main__':
    print('Part Two: {0}'.format(main()))
