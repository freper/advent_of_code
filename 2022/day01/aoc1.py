class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        groups = data.split('\n\n')
        self.calories = list()
        for group in groups:
            self.calories.append([int(value) for value in group.splitlines()])
        self.sum_calories = [sum(calories) for calories in self.calories]
        

    def part1(self):
        return max(self.sum_calories)

    def part2(self):
        sorted_calories = sorted(self.sum_calories)
        return sorted_calories[-1] + sorted_calories[-2] + sorted_calories[-3]


test = Puzzle('test.txt')
assert test.part1() == 24000
assert test.part2() == 45000
# print("Part 1:", test.part1())
# print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
