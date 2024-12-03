import re

class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        self.memory = lines
        
    def part1(self):
        pattern = re.compile(r"mul\((\d+)\,(\d+)\)")
        sum = 0
        for section in self.memory:
            for match in pattern.finditer(section):
                sum += int(match.group(1)) * int(match.group(2))
        return sum

    def part2(self):
        pattern = re.compile(r"mul\((\d+)\,(\d+)\)|do\(\)|don't\(\)")
        sum = 0
        do = True
        for section in self.memory:
            for match in pattern.finditer(section):
                if match.group(0) == "do()":
                    do = True
                elif match.group(0) == "don't()":
                    do = False
                elif do:
                    sum += int(match.group(1)) * int(match.group(2))
        return sum

test1 = Puzzle('test1.txt')
test2 = Puzzle('test2.txt')
assert test1.part1() == 161
assert test2.part2() == 48

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
