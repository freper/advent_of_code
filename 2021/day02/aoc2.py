class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        self.input = data.splitlines()

    def part1(self):
        horizontal = 0
        depth = 0
        for line in self.input:
            data = line.split(' ')
            assert len(data) == 2
            if data[0] == "forward":
                horizontal += int(data[1])
            elif data[0] == "down":
                depth += int(data[1])
            elif data[0] == "up":
                depth -= int(data[1])
            else:
                print("Invalid movement direction.")
        return horizontal * depth

    def part2(self):
        horizontal = 0
        depth = 0
        aim = 0
        for line in self.input:
            data = line.split(' ')
            assert len(data) == 2
            if data[0] == "forward":
                horizontal += int(data[1])
                depth += aim * int(data[1])
            elif data[0] == "down":
                aim += int(data[1])
            elif data[0] == "up":
                aim -= int(data[1])
            else:
                print("Invalid movement direction.")
        return horizontal * depth


test = Puzzle('test.txt')
assert test.part1() == 150
assert test.part2() == 900
# print("Part 1:", test.part1())
# print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
