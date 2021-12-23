import math


class Number:
    def __init__(self, value):
        self.value = value

    def explode(self):
        left = self.value[0]
        right = self.value[1]
        stack = [(left, right)]
        while isinstance(left, list) or isinstance(right, list):
            if isinstance(left, list):
                assert not isinstance(right, list)
                if len(left) > 1:
                    right = left[1]
                left = left[0]
            if isinstance(right, list):
                assert not isinstance(left, list)
                if len(right) > 1:
                right = right[0]
        print(left, right)
        return left

    def split(self, value):
        assert isinstance(value, int)
        return [math.floor(value / 2), math.ceil(value / 2)]

    def reduce(self):
        return None

    def add(self, value):
        return [self.value, value]

    def magnitude(self):
        if isinstance(self.value[0], list):
            left = Number(self.value[0]).magnitude()
        else:
            left = self.value[0]
        if isinstance(self.value[1], list):
            right = Number(self.value[1]).magnitude()
        else:
            right = self.value[1]
        assert isinstance(left, int)
        assert isinstance(right, int)
        return 3 * left + 2 * right


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        self.numbers = [Number(eval(line)) for line in data.splitlines()]

    def part1(self):
        return 1

    def part2(self):
        return 2


print(Number([[[[[9, 8], 1], 2], 3], 4]).explode(), [[[[0, 9], 2], 3], 4])

# test = Puzzle('test.txt')
# assert test.part1() == 1
# assert test.part2() == 2
# print("Part 1:", test.part1())
# print("Part 2:", test.part2())

# puzzle = Puzzle('input.txt')
# print("Part 1:", puzzle.part1())
# print("Part 2:", puzzle.part2())
