#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._parse_data(raw_data)

    def _parse_rule(self, line):
        items = line.split(': ')
        field = items[0]
        ranges = items[1].split(' or ')
        values = []
        for range_str in ranges:
            rng = range_str.split('-')
            start = int(rng[0])
            end = int(rng[1]) + 1
            for i in range(start, end):
                values.append(i)
        self._rules[field] = {'position':-1, 'values':values}

    def _parse_ticket(self, line):
        items = line.split(',')
        return [int(item) for item in items]

    def _parse_data(self, raw_data):
        section = 0
        self._rules = {}
        self._nearby_tickets = []
        for line in raw_data:
            if len(line) == 0:
                section += 1
                continue
            if section == 0:
                self._parse_rule(line)
                continue
            if section == 1:
                if line[0:4] == 'your':
                    continue
                self._your_ticket = self._parse_ticket(line)
                continue
            if section == 2:
                if line[0:6] == 'nearby':
                    continue
                ticket = self._parse_ticket(line)
                self._nearby_tickets.append(ticket)

    def _is_valid_number(self, num):
        for field in self._rules.keys():
            values = self._rules[field]['values']
            if num in values:
                return True
        return False

    def do_part1(self):
        result = 0
        valid_tickets = []
        for i in range(0, len(self._nearby_tickets)):
            ticket = self._nearby_tickets[i]
            valid = True
            for n in ticket:
                if not self._is_valid_number(n):
                    result += n
                    valid = False
            if valid:
                valid_tickets.append(ticket)
        self._nearby_tickets = valid_tickets
        return result

    def _identify_fields(self):
        found_positions = []
        found_any = True
        while found_any:
            found_any = False
            for pos in range(0, len(self._your_ticket)):
                if pos in found_positions:
                    continue
                possible_fields = []
                for field in self._rules.keys():
                    if self._rules[field]['position'] < 0:
                        possible_fields.append(field)
                for ticket in self._nearby_tickets:
                    val = ticket[pos]
                    new_fields = []
                    for field in possible_fields:
                        values = self._rules[field]['values']
                        if val in values:
                            new_fields.append(field)
                    possible_fields = new_fields
                if len(possible_fields) == 1:
                    self._rules[possible_fields[0]]['position'] = pos
                    found_positions.append(pos)
                    found_any = True
        return len(found_positions) == len(self._your_ticket)

    def get_field_value(self, field):
        pos = self._rules[field]['position']
        return self._your_ticket[pos]

    def do_part2(self):
        result = 0
        if self._identify_fields():
            result = 1
            for field in self._rules.keys():
                if field[:9] == 'departure':
                    pos = self._rules[field]['position']
                    result *= self._your_ticket[pos]
        return result

    def execute(self):
        print('Part 1 result:', self.do_part1())
        print('Part 2 result:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
