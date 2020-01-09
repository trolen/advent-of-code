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
    global relative_base
    parm = data[pos]
    if mode == 1:
        return parm
    if mode == 2:
        parm += relative_base
    while parm >= len(data):
        data.append(0)
    return data[parm]


def put_data_value(data, pos, mode, value):
    global relative_base
    if mode == 2:
        pos += relative_base
    while pos >= len(data):
        data.append(0)
    data[pos] = value


def run_intcode(raw_data):
    global relative_base
    data = prepare_data(raw_data)
    relative_base = 0
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
            put_data_value(data, parmC, pModeC, valA + valB if opcode == 1 else valA * valB)
            incr = 4
        elif opcode == 3:
            parmA = data[pos + 1]
            put_data_value(data, parmA, pModeA, int(input('Input: ').strip()))
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
                result = 1
            else:
                result = 0
            put_data_value(data, parmC, pModeC, result)
            incr = 4
        elif opcode == 9:
            valA = get_data_value(data, pos + 1, pModeA)
            relative_base += valA
            incr = 2
        pos += incr


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    data = run_intcode(raw_data)
