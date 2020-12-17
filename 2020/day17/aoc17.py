import numpy as np


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        lines = data.splitlines()

        num_cycles = 6
        size1 = len(lines[0])
        size2 = size1 + 2 * (num_cycles + 1)
        offset1 = (size1 - 1) // 2
        offset2 = (size2 - 1) // 2
        grid1 = np.zeros([size2, size2, size2], dtype=int)
        grid2 = np.zeros([size2, size2, size2, size2], dtype=int)
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '#':
                    grid1[x - offset1 + offset2, y - offset1 + offset2, offset2] = 1
                    grid2[x - offset1 + offset2, y - offset1 + offset2, offset2, offset2] = 1
        self.grid1 = grid1
        self.grid2 = grid2
        self.size = size2

    def update_state1(self):
        updated_grid = self.grid1.copy()
        for x in range(1, self.size - 1):
            for y in range(1, self.size - 1):
                for z in range(1, self.size - 1):
                    active = (self.grid1[x, y, z] == 1)
                    num_active_neigbours = np.sum(
                        self.grid1[(x-1):(x+2), (y-1):(y+2), (z-1):(z+2)]) - self.grid1[x, y, z]
                    if active and (num_active_neigbours not in [2, 3]):
                        updated_grid[x, y, z] = 0
                    elif not active and num_active_neigbours == 3:
                        updated_grid[x, y, z] = 1
                    else:
                        updated_grid[x, y, z] = self.grid1[x, y, z]
        self.grid1 = updated_grid

    def update_state2(self):
        updated_grid = self.grid2.copy()
        for x in range(1, self.size - 1):
            for y in range(1, self.size - 1):
                for z in range(1, self.size - 1):
                    for w in range(1, self.size - 1):
                        active = (self.grid2[x, y, z, w] == 1)
                        num_active_neigbours = np.sum(
                            self.grid2[(x-1):(x+2), (y-1):(y+2), (z-1):(z+2), (w-1):(w+2)]) - self.grid2[x, y, z, w]
                        if active and (num_active_neigbours not in [2, 3]):
                            updated_grid[x, y, z, w] = 0
                        elif not active and num_active_neigbours == 3:
                            updated_grid[x, y, z, w] = 1
                        else:
                            updated_grid[x, y, z, w] = self.grid2[x, y, z, w]
        self.grid2 = updated_grid

    def part1(self):
        for _ in range(6):
            self.update_state1()
        return np.sum(self.grid1)

    def part2(self):
        for _ in range(6):
            self.update_state2()
        return np.sum(self.grid2)


test = Puzzle('test.txt')
assert test.part1() == 112
assert test.part2() == 848

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
