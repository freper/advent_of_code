from copy import deepcopy
import math


class Number:
    def __init__(self, value):
        def flatten(pair, depth, output):
            if isinstance(pair[0], list):
                flatten(pair[0], depth + 1, output)
            else:
                assert isinstance(pair[0], int)
                output.append([pair[0], depth])
            if isinstance(pair[1], list):
                flatten(pair[1], depth + 1, output)
            else:
                assert isinstance(pair[1], int)
                output.append([pair[1], depth])

        flat_value = list()
        flatten(value, 0, flat_value)
        self.value = flat_value

    def explode(self):
        def impl(value):
            for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(value, value[1:])):
                if depth1 < 4 or depth1 != depth2:
                    continue
                if i > 0:
                    value[i - 1][0] += num1
                if i < len(value) - 2:
                    value[i + 2][0] += num2
                value = value[:i] + [[0, depth1 - 1]] + value[i + 2:]
                return True, value
            return False, value
        updated, self.value = impl(self.value)
        return updated

    def split(self):
        def impl(value):
            for i, (num, depth) in enumerate(value):
                if num < 10:
                    continue
                val1 = math.floor(num / 2)
                val2 = math.ceil(num / 2)
                value = value[:i] + [[val1, depth + 1]] + [[val2, depth + 1]] + value[i + 1:]
                return True, value
            return False, value
        updated, self.value = impl(self.value)
        return updated

    def add(self, number):
        self.value = [[num, depth + 1] for (num, depth) in self.value + number.value]
        updated = True
        while updated:
            updated = self.explode()
            if updated:
                continue
            updated = self.split()

    def magnitude(self):
        def impl(value):
            if len(value) > 1:
                for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(value, value[1:])):
                    if depth1 != depth2:
                        continue
                    value = value[:i] + [(3 * num1 + 2 * num2, depth1 - 1)] + value[i + 2:]
                    return impl(value)
            return value[0][0]
        return impl(self.value)


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        self.numbers = [Number(eval(line)) for line in data.splitlines()]

    def part1(self):
        value = deepcopy(self.numbers[0])
        for number in self.numbers[1:]:
            value.add(number)
        return value.magnitude()

    def part2(self):
        largest_magnitude = 0
        for i, num1 in enumerate(self.numbers):
            for j, num2 in enumerate(self.numbers):
                if i == j:
                    continue
                value = deepcopy(num1)
                value.add(num2)
                mag = value.magnitude()
                if mag > largest_magnitude:
                    largest_magnitude = mag
        return largest_magnitude


test = Puzzle('test.txt')
assert test.part1() == 4140
assert test.part2() == 3993

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
