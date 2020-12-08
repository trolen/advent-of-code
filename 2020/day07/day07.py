#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]

def parse_bag_data(str):
    items = str.split(' ')
    if items[0] == 'no':
        return (None, None)
    n = int(items[0])
    color = items[1] + ' ' + items[2]
    return (n, color)

def parse_rule_line(line):
    items = line.split(', ')
    bag_contents = {}
    for i in range(1, len(items)):
        (n, color) = parse_bag_data(items[i])
        bag_contents[color] = n
    items2 = items[0].split(' contain ')
    bag_definition = items2[0].split(' ')
    bag_color = bag_definition[0] + ' ' + bag_definition[1]
    (n, color) = parse_bag_data(items2[1])
    if color is not None:
        bag_contents[color] = n
    return (bag_color, bag_contents)

def parse_data(raw_data):
    result = {}
    for line in raw_data:
        (bag_color, bag_contents) = parse_rule_line(line)
        result[bag_color] = bag_contents
    return result

def find_bags_containing(rules, search_for_color):
    bags_found = []
    for bag_color in rules:
        bag_contents = rules[bag_color]
        if search_for_color in bag_contents:
            bags_found.append(bag_color)
    for bag_color in bags_found:
        new_bags = find_bags_containing(rules, bag_color)
        for new_color in new_bags:
            if new_color not in bags_found:
                bags_found.append(new_color)
    return bags_found

def do_part1(rules):
    bags_found = find_bags_containing(rules, 'shiny gold')
    return len(bags_found)

def number_of_bags_contained(rules, search_for_color):
    result = 0
    bag_contents = rules[search_for_color]
    for bag_color in bag_contents:
        n = bag_contents[bag_color]
        result += n + n * number_of_bags_contained(rules, bag_color)
    return result

def do_part2(rules):
    return number_of_bags_contained(rules, 'shiny gold')

def execute():
    raw_data = read_data('input.txt')
    rules = parse_data(raw_data)
    print('Part 1 result:', do_part1(rules))
    print('Part 2 result:', do_part2(rules))

if __name__ == '__main__':
    execute()