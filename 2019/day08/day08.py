#! /usr/bin/env python3

import sys

def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


def parse_layers(raw_data, width, height):
    result = []
    layer_size = height * width
    n_layers = len(raw_data) // layer_size
    for n in range(0, n_layers):
        start = n *  layer_size
        end = start + layer_size
        s = raw_data[start:end]
        result.append(s)
    return result


def calc_crc(layers):
    n_layers = len(layers)
    min_0 = sys.maxsize
    result = None
    for n in range(0, n_layers):
        layer = layers[n]
        n0 = layer.count('0')
        n1 = layer.count('1')
        n2 = layer.count('2')
        if n0 < min_0:
            min_0 = n0
            result = n1 * n2
    return result


def decode_image(layers):
    layer_size = len(layers[0])
    result = '2' * layer_size
    for layer in layers:
        for i in range(0, layer_size):
            if result[i] == '2':
                s = result[:i] + layer[i] + result[i+1:]
                result = s
    return result


def show_image(image, width, height):
    image = image.replace('0', ' ')
    image = image.replace('1', '#')
    for r in range(0, height):
        start = r * width
        end = start + width
        print(image[start:end])


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    layers = parse_layers(raw_data, width=25, height=6)
    crc = calc_crc(layers)
    print('Part 1 result: {0}'.format(crc))
    image = decode_image(layers)
    show_image(image, width=25, height=6)
