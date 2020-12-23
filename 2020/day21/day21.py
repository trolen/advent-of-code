#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._parse_data(raw_data)

    def _add_ingredients(self, ingredients):
        for ingredient in ingredients:
            n = 0 if ingredient not in self._ingredients else self._ingredients[ingredient]
            self._ingredients[ingredient] = n + 1

    def _add_alergens(self, ingredients, alergens):
        for alergen in alergens:
            arr = [] if alergen not in self._alergens else self._alergens[alergen]
            arr.append(ingredients)
            self._alergens[alergen] = arr

    def _parse_data(self, raw_data):
        self._ingredients = {}
        self._alergens = {}
        for line in raw_data:
            items = line.split(' (contains ')
            ingredients = items[0].split(' ')
            alergens = items[1][:-1].split(', ')
            self._add_ingredients(ingredients)
            self._add_alergens(ingredients, alergens)

    def _reduce_alergen(self, alergen):
        unique_ingredients = set()
        for row in self._alergens[alergen]:
            unique_ingredients.update(row)
        ingredients = []
        for i in unique_ingredients:
            found = True
            for row in self._alergens[alergen]:
                if i not in row:
                    found = False
                    break
            if found:
                ingredients.append(i)
        self._alergens[alergen] = ingredients

    def do_part1(self):
        for alergen in self._alergens:
            self._reduce_alergen(alergen)
        result = 0
        for ingredient in self._ingredients:
            found = False
            for alergen in self._alergens:
                if ingredient in self._alergens[alergen]:
                    found = True
                    break
            if not found:
                result += self._ingredients[ingredient]
        return result

    def do_part2(self):
        alergens = {}
        while len(self._alergens) > 0:
            found_alergen = None
            for alergen in self._alergens:
                if len(self._alergens[alergen]) == 1:
                    found_alergen = alergen
                    break
            if found_alergen is None:
                print('ERROR: Could not find alergen to remove')
                break
            ingredient = self._alergens[found_alergen][0]
            alergens[found_alergen] = ingredient
            del self._alergens[found_alergen]
            for alergen in self._alergens:
                if ingredient in self._alergens[alergen]:
                    self._alergens[alergen].remove(ingredient)
        return ','.join([alergens[key] for key in sorted(alergens.keys())])

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
