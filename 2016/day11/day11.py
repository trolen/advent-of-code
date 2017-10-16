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
        self.min_floor = self._min_floor()

    def _min_floor(self):
        for idx in range(4):
            if len(self.floors[idx]) > 0:
                return idx
        return 4

    def copy(self):
        return GameState(self.steps, self.elevator, [[comp for comp in flr] for flr in self.floors])

    def move_component(self, from_floor, idx, to_floor):
        component = self.floors[from_floor][idx]
        del self.floors[from_floor][idx]
        self.floors[to_floor].append(component)

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
        words = line.split()
        for idx, word in enumerate(words):
            if word == 'nothing':
                return []
            if word[:9] == 'generator' or word[:9] == 'microchip':
                result.append(Component(words[idx - 1], word))
        return result

    def _set_min_steps(self, value):
        if value < self._min_steps:
            self._min_steps = value
            print('Min: {0}'.format(value))

    def _check_new_state(self, state):
        if state.is_game_won():
            self._set_min_steps(state.steps)
            return False
        if not state.is_good():
            return False
        return True

    def _try_moving_one(self, current_state, new_elevator):
        new_states = []
        for idx in range(len(current_state.floors[current_state.elevator])):
            new_state = current_state.copy()
            new_state.steps += 1
            new_state.elevator = new_elevator
            new_state.move_component(current_state.elevator, idx, new_elevator)
            if self._check_new_state(new_state):
                new_states.append(new_state)
        return new_states

    def _try_moving_two(self, current_state, new_elevator):
        new_states = []
        for idx1 in range(len(current_state.floors[current_state.elevator]) - 1):
            for idx2 in range(idx1 + 1, len(current_state.floors[current_state.elevator])):
                new_state = current_state.copy()
                new_state.steps += 1
                new_state.elevator = new_elevator
                new_state.move_component(current_state.elevator, idx2, new_elevator)
                new_state.move_component(current_state.elevator, idx1, new_elevator)
                if self._check_new_state(new_state):
                    new_states.append(new_state)
        return new_states

    def _play_round(self):
        new_states = []
        for current_state in self._game_states:
            if current_state.steps >= self._min_steps:
                continue
            for direction in range(-1, 2, 2):
                new_elevator = current_state.elevator + direction
                if new_elevator < current_state.min_floor or new_elevator > 3:
                    continue
                if direction < 0:
                    states = self._try_moving_one(current_state, new_elevator)
                else:
                    states = self._try_moving_two(current_state, new_elevator)
                if len(states) > 0:
                    new_states += states
                    continue
                if direction < 0:
                    states = self._try_moving_two(current_state, new_elevator)
                else:
                    states = self._try_moving_one(current_state, new_elevator)
                if len(states) > 0:
                    new_states += states
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
    min_spent = simulator.play_game()
    print('Part One: {0}'.format(min_spent))
