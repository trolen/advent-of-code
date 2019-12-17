#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


def prepare_data(raw_data):
    return [int(x) for x in raw_data.split(',')]


def calc_parameter_modes(data):
    opcode = data % 100
    pModeA = (data // 100) % 10
    pModeB = (data // 1000) % 10
    pModeC = (data // 10000) % 10
    return (opcode, pModeA, pModeB, pModeC)


def get_data_value(data, pos, mode):
    parm = data[pos]
    return data[parm] if mode == 0 else parm


def run_intcode(raw_data):
    data = prepare_data(raw_data)
    pos = 0
    while True:
        (opcode, pModeA, pModeB, pModeC) = calc_parameter_modes(data[pos])
        if opcode == 99:
            return data
        incr = 0
        if opcode in (1, 2):
            valA = get_data_value(data, pos + 1, pModeA)
            valB = get_data_value(data, pos + 2, pModeB)
            parmC = data[pos + 3]
            data[parmC] = valA + valB if opcode == 1 else valA * valB
            incr = 4
        elif opcode == 3:
            parmA = data[pos + 1]
            data[parmA] = int(input('Input: ').strip())
            incr = 2
        elif opcode == 4:
            valA = get_data_value(data, pos + 1, pModeA)
            print('Output: {0}'.format(valA))
            incr = 2
        elif opcode in (5, 6):
            valA = get_data_value(data, pos + 1, pModeA)
            valB = get_data_value(data, pos + 2, pModeB)
            if (opcode == 5 and not valA == 0) or (opcode == 6 and valA == 0):
                pos = valB
            else:
                incr = 3
        elif opcode in (7, 8):
            valA = get_data_value(data, pos + 1, pModeA)
            valB = get_data_value(data, pos + 2, pModeB)
            parmC = data[pos + 3]
            if (opcode == 7 and valA < valB) or (opcode == 8 and valA == valB):
                data[parmC] = 1
            else:
                data[parmC] = 0
            incr = 4
        pos += incr


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    data = run_intcode(raw_data)
