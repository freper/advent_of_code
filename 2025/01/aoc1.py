class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        self.input = [(line[0], int(line[1:])) for line in lines]
        
    def part1(self):
        position = 50
        num_zeros = 0
        for direction, offset in self.input:
            if direction == "L":
                position -= offset
            elif direction == "R":
                position += offset
            else:
                raise RuntimeError("Unexpected direction")
            position %= 100
            if position == 0:
                num_zeros += 1
        return num_zeros

    def part2(self):
        position = 50
        num_zeros = 0
        prev_zero = False
        for direction, offset in self.input:
            num_complete_turns = int(offset / 100)
            offset -= num_complete_turns * 100
            if direction == "L":
                position -= offset
            elif direction == "R":
                position += offset
            else:
                raise RuntimeError("Unexpected direction")
            if (position < 0 or position > 100) and not prev_zero:
                num_zeros += 1
            position %= 100
            if position == 0:
                num_zeros += 1
                prev_zero = True
            else:
                prev_zero = False
            num_zeros += num_complete_turns
        return num_zeros

test = Puzzle('test.txt')
assert test.part1() == 3
assert test.part2() == 6

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
