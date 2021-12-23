import math
import re

p = re.compile(r"target area: x=(?P<xmin>\d+)\.\.(?P<xmax>\d+), y=-(?P<ymin>\d+)..-(?P<ymax>\d+)")


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        lines = data.splitlines()
        m = p.fullmatch(lines[0])
        assert m
        self.xmin = int(m["xmin"])
        self.xmax = int(m["xmax"])
        self.ymin = -int(m["ymin"])
        self.ymax = -int(m["ymax"])

    def step(self):
        self.x += self.vx
        self.y += self.vy
        if self.vx > 0:
            self.vx -= 1
        elif self.vx < 0:
            self.vx += 1
        self.vy -= 1

    def inside_target(self):
        if self.x < self.xmin:
            return False
        if self.x > self.xmax:
            return False
        if self.y < self.ymin:
            return False
        if self.y > self.ymax:
            return False
        return True

    def find_highest_position(self):
        target_ymax = 0
        num_hits = 0
        for vx in range(int(math.sqrt(2 * self.xmin)), self.xmax + 1):
            for vy in range(self.ymin, abs(self.ymin)):
                self.x = 0
                self.y = 0
                self.vx = vx
                self.vy = vy
                ymax = 0
                while self.x < self.xmax and self.y > self.ymin and not self.inside_target():
                    self.step()
                    if self.y > ymax:
                        ymax = self.y
                if self.inside_target():
                    num_hits += 1
                    if ymax > target_ymax:
                        target_ymax = ymax
        return target_ymax, num_hits

    def part1(self):
        return self.find_highest_position()[0]

    def part2(self):
        return self.find_highest_position()[1]


test = Puzzle('test.txt')
assert test.part1() == 45
assert test.part2() == 112

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
