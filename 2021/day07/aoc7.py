class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        values = file.read().split(',')
        self.input = [int(value) for value in values]

    def calculate_cost(self, target, cost_table):
        cost = 0
        for crab in self.input:
            cost += cost_table[abs(crab - target)]
        return cost

    def calculate_cost_table1(self):
        cost_table = {0: 0}
        for i in range(1, max(self.input) - min(self.input) + 1):
            cost_table[i] = cost_table[i - 1] + 1
        return cost_table

    def calculate_cost_table2(self):
        cost_table = {0: 0}
        for i in range(1, max(self.input) - min(self.input) + 1):
            cost_table[i] = cost_table[i - 1] + i
        return cost_table

    def part1(self):
        cost_table = self.calculate_cost_table1()
        min_cost = (max(self.input) - min(self.input)) * len(self.input)
        for target in range(min(self.input), max(self.input) + 1):
            cost = self.calculate_cost(target, cost_table)
            if cost < min_cost:
                min_cost = cost
        return min_cost

    def part2(self):
        cost_table = self.calculate_cost_table2()
        min_cost = ((max(self.input) - min(self.input)) ** 2) * len(self.input)
        for target in range(min(self.input), max(self.input) + 1):
            cost = self.calculate_cost(target, cost_table)
            if cost < min_cost:
                min_cost = cost
        return min_cost


test = Puzzle('test.txt')
assert test.part1() == 37
assert test.part2() == 168

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
