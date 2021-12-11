class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        self.input = data.splitlines()

    def part1(self):
        num_lines = len(self.input)
        num_bits = len(self.input[0])
        num_ones = [0] * num_bits
        for line in self.input:
            for i, value in enumerate(line):
                if value == '1':
                    num_ones[i] += 1
        gamma_rate = 0
        epsilon_rate = 0
        num_ones.reverse()
        for i in range(num_bits):
            if num_ones[i] > num_lines / 2:
                gamma_rate += 2**i
            else:
                epsilon_rate += 2**i
        return gamma_rate * epsilon_rate

    def part2(self):
        num_bits = len(self.input[0])
        oxygen_lines = self.input
        for i in range(num_bits):
            num_oxygen_ones = 0
            for line in oxygen_lines:
                if line[i] == '1':
                    num_oxygen_ones += 1
            num_oxygen_lines = len(oxygen_lines)
            if num_oxygen_ones >= num_oxygen_lines / 2:
                oxygen_value = '1'
            else:
                oxygen_value = '0'
            oxygen_lines = [line for line in oxygen_lines if line[i] == oxygen_value]
            if len(oxygen_lines) == 1:
                break
        co2_lines = self.input
        for i in range(num_bits):
            num_co2_ones = 0
            for line in co2_lines:
                if line[i] == '1':
                    num_co2_ones += 1
            num_co2_lines = len(co2_lines)
            if num_co2_ones < num_co2_lines / 2:
                co2_value = '1'
            else:
                co2_value = '0'
            co2_lines = [line for line in co2_lines if line[i] == co2_value]
            if len(co2_lines) == 1:
                break
        assert len(oxygen_lines) == 1
        assert len(co2_lines) == 1
        oxygen_rating = int(oxygen_lines[0], 2)
        co2_rating = int(co2_lines[0], 2)
        return oxygen_rating * co2_rating


test = Puzzle('test.txt')
assert test.part1() == 198
# assert test.part2() == 230
# print("Part 1:", test.part1())
print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
