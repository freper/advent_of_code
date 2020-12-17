import numpy as np


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        lines = data.splitlines()

        assert len(lines) == len(lines[0])
        size = len(lines)
        grid1 = np.zeros([size, size, 1], dtype=int)
        grid2 = np.zeros([size, size, 1, 1], dtype=int)
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '#':
                    grid1[x, y, 0] = 1
                    grid2[x, y, 0, 0] = 1
        self.grid1 = grid1
        self.grid2 = grid2

    def prepare_grid1(self):
        idx = np.nonzero(self.grid1)
        xmin = np.min(idx[0])
        xmax = np.max(idx[0])
        ymin = np.min(idx[1])
        ymax = np.max(idx[1])
        zmin = np.min(idx[2])
        zmax = np.max(idx[2])
        dx = xmax - xmin + 1
        dy = ymax - ymin + 1
        dz = zmax - zmin + 1
        grid = np.zeros([dx + 4, dy + 4, dz + 4], dtype=int)
        grid[2: (dx + 2),
             2: (dy + 2),
             2: (dz + 2)] = self.grid1[xmin: (xmax + 1),
                                       ymin: (ymax + 1),
                                       zmin: (zmax + 1)]
        self.grid1 = grid

    def prepare_grid2(self):
        idx = np.nonzero(self.grid2)
        xmin = np.min(idx[0])
        xmax = np.max(idx[0])
        ymin = np.min(idx[1])
        ymax = np.max(idx[1])
        zmin = np.min(idx[2])
        zmax = np.max(idx[2])
        wmin = np.min(idx[3])
        wmax = np.max(idx[3])
        dx = xmax - xmin + 1
        dy = ymax - ymin + 1
        dz = zmax - zmin + 1
        dw = wmax - wmin + 1
        grid = np.zeros([dx + 4, dy + 4, dz + 4, dz + 4], dtype=int)
        grid[2: (dx + 2),
             2: (dy + 2),
             2: (dz + 2),
             2: (dw + 2)] = self.grid2[xmin: (xmax + 1),
                                       ymin: (ymax + 1),
                                       zmin: (zmax + 1),
                                       wmin: (wmax + 1)]
        self.grid2 = grid

    def update_grid1(self):
        self.prepare_grid1()
        updated_grid = self.grid1.copy()
        (nx, ny, nz) = updated_grid.shape
        for x in range(1, nx - 1):
            for y in range(1, ny - 1):
                for z in range(1, nz - 1):
                    active = (self.grid1[x, y, z] == 1)
                    num_active_neigbours = np.sum(
                        self.grid1[(x - 1):(x + 2), (y - 1):(y + 2), (z - 1):(z + 2)]) - self.grid1[x, y, z]
                    if active and (num_active_neigbours not in [2, 3]):
                        updated_grid[x, y, z] = 0
                    elif not active and num_active_neigbours == 3:
                        updated_grid[x, y, z] = 1
                    else:
                        updated_grid[x, y, z] = self.grid1[x, y, z]
        self.grid1 = updated_grid

    def update_grid2(self):
        self.prepare_grid2()
        updated_grid = self.grid2.copy()
        (nx, ny, nz, nw) = updated_grid.shape
        for x in range(1, nx - 1):
            for y in range(1, ny - 1):
                for z in range(1, nz - 1):
                    for w in range(1, nw - 1):
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
            self.update_grid1()
        return np.sum(self.grid1)

    def part2(self):
        for _ in range(6):
            self.update_grid2()
        return np.sum(self.grid2)


test = Puzzle('test.txt')
assert test.part1() == 112
assert test.part2() == 848

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
