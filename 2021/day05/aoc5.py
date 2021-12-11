import numpy as np


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        lines = data.splitlines()
        line_segments = list()
        max_x = 0
        max_y = 0
        for line in lines:
            line_points = line.split(' -> ')

            start_point = line_points[0].split(',')
            start_point_x = int(start_point[0])
            start_point_y = int(start_point[1])

            end_point = line_points[1].split(',')
            end_point_x = int(end_point[0])
            end_point_y = int(end_point[1])

            max_x = max(max_x, start_point_x, end_point_x)
            max_y = max(max_y, start_point_y, end_point_y)

            line_segment = ((start_point_x, start_point_y), (end_point_x, end_point_y))
            line_segments.append(line_segment)
        self.line_map = np.zeros((max_x + 1, max_y + 1), dtype=int)
        self.lines = line_segments

    def part1(self):
        for line in self.lines:
            x1 = line[0][0]
            y1 = line[0][1]
            x2 = line[1][0]
            y2 = line[1][1]
            if x1 == x2:
                self.line_map[x1, min(y1, y2):(max(y1, y2) + 1)] += 1
            elif y1 == y2:
                self.line_map[min(x1, x2):(max(x1, x2) + 1), y1] += 1
        return (self.line_map > 1).sum()

    def part2(self):
        for line in self.lines:
            x1 = line[0][0]
            y1 = line[0][1]
            x2 = line[1][0]
            y2 = line[1][1]
            if not x1 == x2 and not y1 == y2:
                dx = x2 - x1
                dy = y2 - y1
                assert abs(dx) == abs(dy)
                nx = int(dx / abs(dx))
                ny = int(dy / abs(dy))
                for d in range(abs(dx) + 1):
                    self.line_map[x1 + d * nx, y1 + d * ny] += 1
        return (self.line_map > 1).sum()


test = Puzzle('test.txt')
# assert test.part1() == 5
# assert test.part2() == 12
print("Part 1:", test.part1())
print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
