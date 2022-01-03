from copy import deepcopy
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
        initial_state = np.zeros((rows, cols), dtype=int)
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == '>':
                    initial_state[i, j] = 1
                elif c == 'v':
                    initial_state[i, j] = 2
        self.rows = rows
        self.cols = cols
        self.initial_state = initial_state

    def init(self):
        self.state = self.initial_state

    def update(self):
        updated = False
        prev_state = deepcopy(self.state)
        for row in range(self.rows):
            for col in range(self.cols):
                next_col = (col + 1) % self.cols
                if prev_state[row, col] == 1 and prev_state[row, next_col] == 0:
                    self.state[row, col] = 0
                    self.state[row, next_col] = 1
                    updated = True
        prev_state = deepcopy(self.state)
        for row in range(self.rows):
            next_row = (row + 1) % self.rows
            for col in range(self.cols):
                if prev_state[row, col] == 2 and prev_state[next_row, col] == 0:
                    self.state[row, col] = 0
                    self.state[next_row, col] = 2
                    updated = True
        return updated

    def part1(self):
        self.init()
        updated = True
        step = 0
        while updated:
            updated = self.update()
            step += 1
        return step

    def part2(self):
        return 2


test = Puzzle('test.txt')
assert test.part1() == 58
# assert test.part2() == 2
# print("Part 1:", test.part1())
print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
# print("Part 2:", puzzle.part2())
