#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


def generate_recipe_impl(recipes, elves):
    n = recipes[elves[0]] + recipes[elves[1]]
    s = ''
    if n > 9:
        recipes.append(1)
        s += str(recipes[-1])
    recipes.append(n % 10)
    s += str(recipes[-1])
    elves[0] = (elves[0] + recipes[elves[0]] + 1) % len(recipes)
    elves[1] = (elves[1] + recipes[elves[1]] + 1) % len(recipes)
    return(s)


def generate_recipes1(n_recipes):
    recipes = [3, 7]
    elves = [0, 1]
    while len(recipes) < n_recipes+10:
        generate_recipe_impl(recipes, elves)
    return ''.join(str(n) for n in recipes[n_recipes:n_recipes+10])


def generate_recipes2(search_str):
    len_search = len(search_str)
    recipes = [3, 7]
    elves = [0, 1]
    recipe_str = '37'
    idx = -1
    while idx < 0:
        recipe_str += generate_recipe_impl(recipes, elves)
        len_recipe = len(recipe_str)
        if len_recipe >= len_search + 2:
            start = len_recipe - len_search - 2
            idx = recipe_str[start:].find(search_str)
            if idx >= 0:
                idx += start
    return(idx)


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    s = generate_recipes1(int(raw_data))
    print('10 recipes after {0} recipes: {1}'.format(raw_data, s))
    n = generate_recipes2(raw_data)
    print('{0} first appears after {1} recipes'.format(raw_data, n))
