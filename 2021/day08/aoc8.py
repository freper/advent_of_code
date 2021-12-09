class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()

        self.patterns = list()
        self.digits = list()
        for line in lines:
            patterns = line.split(' | ')[0].split(' ')
            digits = line.split(' | ')[1].split(' ')
            self.patterns.append(patterns)
            self.digits.append(digits)

    @staticmethod
    def decode(patterns, digits):
        decoded = dict()
        undecoded = list()
        table = dict()
        for pattern in patterns:
            if len(pattern) == 2:
                decoded[1] = set(pattern)
            elif len(pattern) == 3:
                decoded[7] = set(pattern)
            elif len(pattern) == 4:
                decoded[4] = set(pattern)
            elif len(pattern) == 7:
                decoded[8] = set(pattern)
            else:
                undecoded.append(set(pattern))
        table['a'] = decoded[7] - decoded[1]
        print(table)
        return 1

    def part1(self):
        num_instances = 0
        for values in self.digits:
            for value in values:
                if len(value) in [2, 3, 4, 7]:
                    num_instances += 1
        return num_instances

    def part2(self):
        sum = 0
        for patterns, digits in zip(self.patterns, self.digits):
            sum += self.decode(patterns, digits)
        return 2


test = Puzzle('test.txt')
assert test.part1() == 26
# assert test.part2() == 61229
print("Part 1:", test.part1())
print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
