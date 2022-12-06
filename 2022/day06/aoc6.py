class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        self.input = lines[0]

    def find_marker(self, length):
        for start in range(0, len(self.input) - length):
            end = start + length
            if len(set(self.input[start:end])) == length:
                return end
    
    def part1(self):
        return self.find_marker(4)

    def part2(self):
        return self.find_marker(14)


test = Puzzle('test.txt')
assert test.part1() == 7
assert test.part2() == 19

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
