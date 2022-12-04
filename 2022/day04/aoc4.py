class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, "r")
        lines = file.read().splitlines()
        def parse_assignment(assignment):
            data = assignment.split("-")
            return set(range(int(data[0]), int(data[1]) + 1))
        def parse_pair(line):
            data = line.split(",")
            return (parse_assignment(data[0]), parse_assignment(data[1]))
        self.input = [parse_pair(line) for line in lines]

    def part1(self):
        def fully_contain(input):
            if input[0].issubset(input[1]) or input[1].issubset(input[0]):
                return 1
            return 0
        return sum([fully_contain(input) for input in self.input])

    def part2(self):
        def overlap(input):
            if set.intersection(*input):
                return 1
            return 0
        return sum([overlap(input) for input in self.input])


test = Puzzle('test.txt')
assert test.part1() == 2
assert test.part2() == 4

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
