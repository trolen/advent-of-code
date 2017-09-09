#! /usr/bin/env python3

# THIS PROGRAM RUNS FASTER AT THE COMMAND PROMPT (NOT IN THE IDE)
# THE MD5 HAS ROUTINE IS SLOW

from hashlib import md5

SPINNER = '|/-\\'


def compute_hash(s):
    return md5(s.encode('ascii')).hexdigest()


def find_interesting_hash(s_id):
    idx = 0
    while True:
        s_hash = '-----'
        while s_hash[:5] != '00000':
            print('\r{0}'.format(SPINNER[idx % 4]), flush=True, end='')
            s_in = s_id + str(idx)
            s_hash = compute_hash(s_in)
            idx += 1
        yield s_hash


def get_password1(s_id):
    result = ''
    idx = 0
    for s_hash in find_interesting_hash(s_id):
        result += s_hash[5]
        idx += 1
        print('\r{0}'.format(result))
        if len(result) >= 8:
            break
    return result


def get_password2(s_id):
    result = '________'
    for s_hash in find_interesting_hash(s_id):
        ch = s_hash[5]
        if ch in '01234567':
            idx = int(ch)
            if result[idx] == '_':
                result = '{0}{1}{2}'.format(result[:idx], s_hash[6], result[idx + 1:])
                print('\r{0}'.format(result))
        if '_' not in result:
            break
    return result


if __name__ == '__main__':
    door_id = 'cxdnnyjw'
    pw = get_password1(door_id)
    print('Part One: {0}'.format(pw))
    pw = get_password2(door_id)
    print('Part Two: {0}'.format(pw))
