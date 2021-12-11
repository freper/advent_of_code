import numpy as np


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        lines = data.splitlines()
        rows = len(lines)
        cols = len(lines[0])
        values = np.zeros((rows, cols), dtype=int)
        for i, line in enumerate(lines):
            for j, value in enumerate(line):
                values[i, j] = int(value)
        self.rows = rows
        self.cols = cols
        self.input = values

    def energise_octopus(self, i, j):
        if i < 0 or i > self.rows - 1:
            return
        if j < 0 or j > self.cols - 1:
            return
        if self.energy[i, j] > 0:
            self.energy[i, j] += 1

    def energise_neighbours(self, i, j):
        self.energise_octopus(i - 1, j - 1)
        self.energise_octopus(i - 1, j)
        self.energise_octopus(i - 1, j + 1)
        self.energise_octopus(i, j - 1)
        self.energise_octopus(i, j + 1)
        self.energise_octopus(i + 1, j - 1)
        self.energise_octopus(i + 1, j)
        self.energise_octopus(i + 1, j + 1)

    def update_energy(self):
        num_flashes = 0
        self.energy += 1
        updated = True
        while updated:
            updated = False
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.energy[i, j] > 9:
                        self.energise_neighbours(i, j)
                        num_flashes += 1
                        self.energy[i, j] = 0
                        updated = True
        return num_flashes

    def part1(self):
        self.energy = self.input.copy()
        num_flashes = 0
        for n in range(100):
            num_flashes += self.update_energy()
        return num_flashes

    def part2(self):
        self.energy = self.input.copy()
        n = 0
        while True:
            n += 1
            num_flashes = self.update_energy()
            if num_flashes == self.rows * self.cols:
                return n


test = Puzzle('test.txt')
assert test.part1() == 1656
assert test.part2() == 195
# print("Part 1:", test.part1())
# print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
