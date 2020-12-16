class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read().split("\n\n")
        rules = data[0].splitlines()
        self.parse_rules(rules)

        def parse_ticket(line):
            return [int(x) for x in line.split(',')]

        self.your_ticket = parse_ticket(data[1].splitlines()[1])
        self.nearby_tickets = [parse_ticket(ticket)
                               for ticket in data[2].splitlines()[1:]]

    def parse_rules(self, rules):
        valid_ranges = []
        for line in rules:
            data = line.split(": ")
            name = data[0]
            ranges = data[1].split(" or ")
            for r in ranges:
                x = r.split("-")
                valid_ranges.append((int(x[0]), int(x[1])))
        self.valid_ranges = valid_ranges

    def is_value_valid(self, value):
        for x in self.valid_ranges:
            if value >= x[0] and value <= x[1]:
                return True
        return False

    def part1(self):
        invalid_values = []
        for ticket in self.nearby_tickets:
            for value in ticket:
                if not self.is_value_valid(int(value)):
                    invalid_values.append(value)
        return sum(invalid_values)

    def part2(self):
        return 2


test = Puzzle('test.txt')
assert test.part1() == 71
assert test.part2() == 2

puzzle = Puzzle('input.txt')
print(puzzle.part1())
print(puzzle.part2())
