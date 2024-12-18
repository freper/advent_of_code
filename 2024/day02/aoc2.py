def is_safe(report) -> bool:
        if report[0] == report[1]:
            return False
        increase = report[1] > report[0]
        decrease = report[1] < report[0]
        previous = report[0]
        for value in report[1:]:
            if value == previous:
                return False
            if abs(value - previous) > 3:
                return False
            if increase and (value < previous):
                return False
            if decrease and (value > previous):
                return False
            previous = value
        return True


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        def parse_line(line):
            return [int(value) for value in line.split()]
        self.reports = [parse_line(line) for line in lines]

    def part1(self):
        sum = 0
        for report in self.reports:
            if is_safe(report):
                sum += 1
        return sum

    def part2(self):
        sum = 0
        for report in self.reports:
            if any([is_safe(report[:i] + report[i+1:]) for i in range(len(report))]):
                sum += 1
        return sum


test = Puzzle('test.txt')
assert test.part1() == 2
assert test.part2() == 4

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
