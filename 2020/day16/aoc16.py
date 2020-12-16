class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read().split("\n\n")

        self.all_valid_ranges = []
        self.rule_valid_ranges = {}
        for line in data[0].splitlines():
            tmp = line.split(": ")
            name = tmp[0]
            ranges = tmp[1].split(" or ")
            self.rule_valid_ranges[name] = []
            for r in ranges:
                x = r.split("-")
                self.all_valid_ranges.append((int(x[0]), int(x[1])))
                self.rule_valid_ranges[name].append((int(x[0]), int(x[1])))

        def parse_ticket(line):
            return [int(x) for x in line.split(',')]

        self.your_ticket = parse_ticket(data[1].splitlines()[1])
        self.num_ticket_values = len(self.your_ticket)
        self.nearby_tickets = [parse_ticket(ticket)
                               for ticket in data[2].splitlines()[1:]]

    def identify_ticket_fields(self):
        self.offset = {}
        valid_offsets = {}
        for name in self.rule_valid_ranges.keys():
            valid_offsets[name] = set()
        for offset in range(self.num_ticket_values):
            values = [ticket[offset] for ticket in self.nearby_tickets]
            for name, valid_ranges in self.rule_valid_ranges.items():
                if all([self.is_value_valid(value, valid_ranges) for value in values]):
                    valid_offsets[name].add(offset)

        # Purge valid offsets
        finished = False
        while not finished:
            finished = True
            invalid_offsets = set()
            for name, offsets in valid_offsets.items():
                if len(offsets) == 1:
                    offset = next(iter(offsets))
                    self.offset[name] = offset
                    invalid_offsets.add(offset)
            if invalid_offsets:
                for name in valid_offsets.keys():
                    valid_offsets[name] -= invalid_offsets
                    finished = False

    def is_value_valid(self, value, valid_ranges):
        for x in valid_ranges:
            if value >= x[0] and value <= x[1]:
                return True
        return False

    def is_ticket_valid(self, ticket):
        return all([self.is_value_valid(value, self.all_valid_ranges) for value in ticket])

    def remove_invalid_tickets(self):
        self.nearby_tickets = [
            ticket for ticket in self.nearby_tickets if self.is_ticket_valid(ticket)]

    def part1(self):
        invalid_values = []
        for ticket in self.nearby_tickets:
            invalid_values += [value for value in ticket if not self.is_value_valid(
                value, self.all_valid_ranges)]
        return sum(invalid_values)

    def part2(self):
        self.remove_invalid_tickets()
        self.identify_ticket_fields()
        product = 1
        num_fields = 0
        for name, offset in self.offset.items():
            if name.startswith("departure"):
                product *= self.your_ticket[offset]
                num_fields += 1
        assert num_fields == 6
        return product


test1 = Puzzle('test1.txt')
assert test1.part1() == 71
test2 = Puzzle('test2.txt')
test2.remove_invalid_tickets()
test2.identify_ticket_fields()
assert test2.offset["class"] == 1
assert test2.offset["row"] == 0
assert test2.offset["seat"] == 2

puzzle = Puzzle('input.txt')
print(puzzle.part1())
print(puzzle.part2())
