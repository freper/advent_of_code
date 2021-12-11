fieldstr_to_num = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4,
                   "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}


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
        decoded_sets = {}
        patterns_by_length = {}
        for pattern in patterns:
            length = len(pattern)
            if length in patterns_by_length.keys():
                patterns_by_length[length].append(set(pattern))
            else:
                patterns_by_length[length] = [set(pattern)]
        decoded_sets['a'] = patterns_by_length[3][0] - patterns_by_length[2][0]
        decoded_sets['d'] = set.intersection(*patterns_by_length[5]) & patterns_by_length[4][0]
        decoded_sets['f'] = set.intersection(*patterns_by_length[6]) & patterns_by_length[2][0]
        decoded_sets['g'] = set.intersection(
            *patterns_by_length[5]) - decoded_sets['a'] - decoded_sets['d']
        decoded_sets['b'] = set.intersection(
            *patterns_by_length[6]) - decoded_sets['a'] - decoded_sets['f'] - decoded_sets['g']
        decoded_sets['c'] = patterns_by_length[3][0] - decoded_sets['a'] - decoded_sets['f']
        decoded_sets['e'] = patterns_by_length[7][0] - set.intersection(
            *patterns_by_length[6]) - decoded_sets['c'] - decoded_sets['d']

        decoded_to_original_values = {}
        for original_value, decoded_set in decoded_sets.items():
            assert len(decoded_set) == 1
            decoded_value = next(iter(decoded_set))
            decoded_to_original_values[decoded_value] = original_value

        decoded_str = ""
        for digit in digits:
            original_fields = [decoded_to_original_values[value] for value in digit]
            original_str = "".join(sorted(original_fields))
            original_num = fieldstr_to_num[original_str]
            decoded_str += str(original_num)
        return int(decoded_str)

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
        return sum


test = Puzzle('test.txt')
assert test.part1() == 26
assert test.part2() == 61229

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
