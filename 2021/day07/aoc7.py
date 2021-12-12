class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        values = file.read().split(',')
        self.input = [int(value) for value in values]

    def cost_table(self, incremental_cost=False):
        cost_table = {0: 0}
        for i in range(1, max(self.input) - min(self.input) + 1):
            if incremental_cost:
                cost_table[i] = cost_table[i - 1] + i
            else:
                cost_table[i] = cost_table[i - 1] + 1
        return cost_table

    def calculate_cost(self, target, cost_table):
        cost = 0
        for crab in self.input:
            cost += cost_table[abs(crab - target)]
        return cost

    def calculate_minimum_cost(self, incremental_cost=False):
        cost_table = self.cost_table(incremental_cost)
        min_cost = ((max(self.input) - min(self.input))**2) * len(self.input)
        for target in range(min(self.input), max(self.input) + 1):
            cost = self.calculate_cost(target, cost_table)
            if cost < min_cost:
                min_cost = cost
        return min_cost

    def part1(self):
        return self.calculate_minimum_cost()

    def part2(self):
        return self.calculate_minimum_cost(incremental_cost=True)


test = Puzzle('test.txt')
assert test.part1() == 37
assert test.part2() == 168

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
