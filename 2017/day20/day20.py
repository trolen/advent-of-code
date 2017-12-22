#! /usr/bin/env python3

class Particle:
    def __init__(self, position, velocity, accel):
        self._position = position
        self._velocity = velocity
        self._accel = accel

    def distance(self):
        return sum([abs(n) for n in self._position])

    def total_accel(self):
        return sum([abs(n) for n in self._accel])

    def tick(self):
        self._velocity = (
            self._velocity[0] + self._accel[0],
            self._velocity[1] + self._accel[1],
            self._velocity[2] + self._accel[2]
        )
        self._position = (
            self._position[0] + self._velocity[0],
            self._position[1] + self._velocity[1],
            self._position[2] + self._velocity[2]
        )

    def position(self):
        return self._position

    def compare_position(self, position):
        return (self._position[0] == position[0]) and \
               (self._position[1] == position[1]) and \
               (self._position[2] == position[2])


class Particles:
    def __init__(self, data):
        self._particles = self._parse_data(data)

    def _parse_triple(self, line, search):
        n1 = line.index(search)
        n2 = line[n1:].index('>')
        x,y,z = line[n1+3:n1+n2].split(',')
        return (int(x), int(y), int(z))

    def _parse_data(self, data):
        result = []
        for line in data:
            pos = self._parse_triple(line, 'p=<')
            vel = self._parse_triple(line, 'v=<')
            accel = self._parse_triple(line, 'a=<')
            result.append(Particle(pos, vel, accel))
        return result

    def find_min_accel(self):
        result = 0
        min_accel = 999999
        for i,p in enumerate(self._particles):
            a = p.total_accel()
            if a < min_accel:
                min_accel = a
                result = i
        return result

    def _collisions(self):
        new_particles = []
        collisions = []
        for i,p1 in enumerate(self._particles):
            if i in collisions:
                continue
            found = False
            for j,p2 in enumerate(self._particles[i+1:]):
                if p1.compare_position(p2.position()):
                    if not found:
                        collisions.append(i)
                        found = True
                    collisions.append(i+j+1)
            if not found:
                new_particles.append(p1)
        self._particles = new_particles


    def _tick(self):
        for p in self._particles:
            p.tick()

    def run(self):
        for _ in range(50):
            self._collisions()
            self._tick()
        return len(self._particles)


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    particles = Particles(data)
    print('Part One: {0}'.format(particles.find_min_accel()))
    print('Part Two: {0}'.format(particles.run()))
