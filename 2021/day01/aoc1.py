class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        self.input = data.splitlines()

    def part1(self):
        num_increases = 0
        for i in range(len(self.input) - 1):
            previous = int(self.input[i])
            current = int(self.input[i + 1])
            if current > previous:
                num_increases += 1
        return num_increases

    def part2(self):
        num_increases = 0
        for i in range(len(self.input) - 3):
            v0 = int(self.input[i])
            v1 = int(self.input[i + 1])
            v2 = int(self.input[i + 2])
            v3 = int(self.input[i + 3])
            previous = v0 + v1 + v2
            current = v1 + v2 + v3
            if current > previous:
                num_increases += 1
        return num_increases


test = Puzzle('test.txt')
assert test.part1() == 7
assert test.part2() == 5

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
