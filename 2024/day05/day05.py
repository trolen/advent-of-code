import re

def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]
    

def split_line(line, separator = ','):
    return [int(x) for x in line.split(separator)]


class Application:
    def __init__(self, raw_input):
        rules_loaded = False
        self.rules = []
        self.updates = []
        for i in range(len(raw_input)):
            line = raw_input[i]
            if line == '':
                rules_loaded = True
                continue
            if not rules_loaded:
                self.rules.append(split_line(line, '|'))
                continue
            self.updates.append(split_line(line))

    def isUpdateCorrect(self, update):
        for i in range(len(update) - 1):
            p1 = update[i]
            for j in range(i + 1, len(update)):
                p2 = update[j]
                for k in range(len(self.rules)):
                    rule = self.rules[k]
                    if rule[0] == p1 and rule[1] == p2:
                        break
                    if rule[0] == p2 and rule[1] == p1:
                        fixedUpdate = [x for x in update]
                        fixedUpdate[j] = p1
                        fixedUpdate[i] = p2
                        return [False, fixedUpdate]
        return [True, update]
    
    def findMid(self, update):
        return update[(len(update) - 1) // 2]
    
    def do_part1(self):
        result = 0
        for i in range(len(self.updates)):
            update = self.updates[i]
            [flag, fixedUpdate] = self.isUpdateCorrect(update)
            if (flag):
                result += self.findMid(update)
        return result

    def do_part2(self):
        result = 0
        for i in range(len(self.updates)):
            update = self.updates[i]
            [flag, fixedUpdate] = self.isUpdateCorrect(update)
            if (not flag):
                while not flag:
                    [flag, fixedUpdate] = self.isUpdateCorrect(fixedUpdate)
                result += self.findMid(fixedUpdate)
        return result


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
