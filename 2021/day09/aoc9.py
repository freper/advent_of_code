import numpy as np


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        heightmap = np.zeros((len(lines), len(lines[0])), dtype=int)
        for i, line in enumerate(lines):
            for j, character in enumerate(line):
                heightmap[i][j] = int(character)
        self.heightmap = heightmap

    def is_low_point(self, i, j):
        height = self.heightmap[i, j]
        rows = self.heightmap.shape[0]
        cols = self.heightmap.shape[1]
        if i > 0 and self.heightmap[i - 1, j] <= height:
            return False
        if i < rows - 1 and self.heightmap[i + 1, j] <= height:
            return False
        if j > 0 and self.heightmap[i, j - 1] <= height:
            return False
        if j < cols - 1 and self.heightmap[i, j + 1] <= height:
            return False
        return True

    def find_low_points(self):
        low_points = list()
        for i in range(self.heightmap.shape[0]):
            for j in range(self.heightmap.shape[1]):
                if self.is_low_point(i, j):
                    low_points.append((i, j))
        return low_points

    def get_neighbours(self, point):
        i, j = point
        rows = self.heightmap.shape[0]
        cols = self.heightmap.shape[1]
        neighbours = set()
        if i > 0 and self.heightmap[i - 1, j] < 9:
            neighbours.add((i - 1, j))
        if i < rows - 1 and self.heightmap[i + 1, j] < 9:
            neighbours.add((i + 1, j))
        if j > 0 and self.heightmap[i, j - 1] < 9:
            neighbours.add((i, j - 1))
        if j < cols - 1 and self.heightmap[i, j + 1] < 9:
            neighbours.add((i, j + 1))
        return neighbours

    def find_basin(self, low_point):
        basin = {low_point}
        old_points = {low_point}
        while len(old_points) > 0:
            new_points = set()
            for point in old_points:
                neighbours = self.get_neighbours(point)
                new_points.update(neighbours - basin)
            basin.update(new_points)
            old_points = new_points
        return basin

    def part1(self):
        risk = 0
        for i, j in self.find_low_points():
            risk += 1 + self.heightmap[i, j]
        return risk

    def part2(self):
        low_points = self.find_low_points()
        basins = dict()
        for point in low_points:
            basins[point] = self.find_basin(point)
        sizes = [len(points) for points in basins.values()]
        sizes.sort(reverse=True)
        return sizes[0] * sizes[1] * sizes[2]


test = Puzzle('test.txt')
assert test.part1() == 15
assert test.part2() == 1134

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
