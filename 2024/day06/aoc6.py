class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        
    def part1(self):
        return

    def part2(self):
        return

test = Puzzle('test.txt')
print("Part 1:", test.part1())
print("Part 2:", test.part2())
# assert test.part1() == 2
# assert test.part2() == 4

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
