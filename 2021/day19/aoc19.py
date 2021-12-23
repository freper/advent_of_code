import numpy as np

nx = np.array([1, 0, 0], dtype=int)
ny = np.array([0, 1, 0], dtype=int)
nz = np.array([0, 0, 1], dtype=int)


def create_rotations():
    rotations = list()
    for rx in [nx, -nx, ny, -ny, nz, -nz]:
        for ry in [nx, -nx, ny, -ny, nz, -nz]:
            if (rx == ry).all() or (rx == -ry).all():
                continue
            rz = np.cross(rx, ry)
            rotation = np.stack((rx, ry, rz))
            rotations.append(rotation)
    return rotations


def compare_positions(list1, list2):
    occurences = {}
    for pos1 in list1:
        for pos2 in list2:
            diff = pos2 - pos1
            key = (diff[0], diff[1], diff[2])
            if key in occurences.keys():
                occurences[key] += 1
            else:
                occurences[key] = 1
    result = [(key, value) for key, value in occurences.items() if value > 2]
    return result[0] if result else None


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        groups = data.split('\n\n')
        reports = list()
        for group in groups:
            lines = group.splitlines()
            del lines[0]  # Remove first line
            report = list()
            for line in lines:
                report.append(np.array(line.split(','), dtype=int))
            reports.append(report)
        self.reports = reports

    def compare_reports(self, i, j):
        assert i < len(self.reports)
        assert j < len(self.reports)
        report_i = self.reports[i]
        for R in create_rotations():
            report_j = [np.dot(R, x) for x in self.reports[j]]
            result = compare_positions(report_i, report_j)
            if result:
                return result
        return None

    def part1(self):
        for i in range(len(self.reports) - 1):
            for j in range(i + 1, len(self.reports)):
                print(self.compare_reports(i, j))
        return 1

    def part2(self):
        return 2


test = Puzzle('test.txt')
# assert test.part1() == 1
# assert test.part2() == 2
print("Part 1:", test.part1())
print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
