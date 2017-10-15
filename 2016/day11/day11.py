#! /usr/bin/env python3

class Component:
    def __init__(self, element, type):
        self.element = element[:2].upper()
        self.type = type[0].upper()


class GameState:
    def __init__(self, steps, elevator, floors):
        self.steps = steps
        self.elevator = elevator
        self.floors = floors

    def copy(self):
        return GameState(self.steps, self.elevator, [[comp for comp in flr] for flr in self.floors])

    def iterate_microchips(self, floor):
        for component in floor:
            if component.type == 'M':
                yield component

    def iterate_generators(self, floor):
        for component in floor:
            if component.type == 'G':
                yield component

    def is_good(self):
        for floor in self.floors:
            for chip in self.iterate_microchips(floor):
                non_matching_generator = False
                matching_generator = False
                for generator in self.iterate_generators(floor):
                    if chip.element == generator.element:
                        matching_generator = True
                        break
                    else:
                        non_matching_generator = True
                if non_matching_generator and not matching_generator:
                    return False
        return True

    def is_game_won(self):
        for i in range(3):
            if len(self.floors[i]) > 0:
                return False
        return True


class Simulator:
    def __init__(self, data):
        self._game_states = [GameState(0, 0, self._parse_data(data))]
        self._min_steps = 999999

    def _parse_data(self, data):
        floors = []
        for line in data:
            floors.append(self._parse_line(line))
        return floors

    def _parse_line(self, line):
        result = []
        prev_word = ''
        for word in line.split():
            if word == 'nothing':
                return []
            if word.startswith('gen') or word.startswith('mic'):
                result.append(Component(prev_word, word))
            prev_word = word
        return result

    def _set_min_steps(self, value):
        if value < self._min_steps:
            self._min_steps = value
            print('Min: {0}'.format(value))

    def _play_round(self):
        new_states = []
        for current_state in self._game_states:
            if current_state.steps >= self._min_steps:
                continue
            for direction in range(-1, 2, 2):
                new_elevator = current_state.elevator + direction
                if new_elevator < 0 or new_elevator > 3:
                    continue
                for idx in range(len(current_state.floors[current_state.elevator])):
                    new_state = current_state.copy()
                    new_state.steps += 1
                    new_state.elevator = new_elevator
                    component = new_state.floors[current_state.elevator][idx]
                    del new_state.floors[current_state.elevator][idx]
                    new_state.floors[new_elevator].append(component)
                    if new_state.is_game_won():
                        self._set_min_steps(new_state.steps)
                    elif new_state.is_good():
                        new_states.append(new_state)
                for idx1 in range(len(current_state.floors[current_state.elevator]) - 1):
                    for idx2 in range(idx1 + 1, len(current_state.floors[current_state.elevator])):
                        new_state = current_state.copy()
                        new_state.steps += 1
                        new_state.elevator = new_elevator
                        comp2 = new_state.floors[current_state.elevator][idx2]
                        comp1 = new_state.floors[current_state.elevator][idx1]
                        del new_state.floors[current_state.elevator][idx2]
                        del new_state.floors[current_state.elevator][idx1]
                        new_state.floors[new_elevator].append(comp2)
                        new_state.floors[new_elevator].append(comp1)
                        if new_state.is_game_won():
                            self._set_min_steps(new_state.steps)
                        elif new_state.is_good():
                            new_states.append(new_state)
        self._game_states = new_states

    def play_game(self):
        while len(self._game_states) > 0:
            self._play_round()
        return self._min_steps


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    simulator = Simulator(data)
    simulator.play_game()
