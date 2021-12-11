class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        values = file.read().split(',')
        self.input = [int(value) for value in values]

    def part1(self):
        fishes = self.input.copy()
        for _ in range(80):
            new_fishes = []
            for i, fish in enumerate(fishes):
                if fish == 0:
                    fishes[i] = 6
                    new_fishes.append(8)
                else:
                    fishes[i] -= 1
            fishes += new_fishes
        return len(fishes)

    def part2(self):
        num_fishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for value in self.input:
            num_fishes[value] += 1
        for _ in range(256):
            num_new_fishes = num_fishes[0]
            for i in range(1, 9):
                num_fishes[i - 1] = num_fishes[i]
            num_fishes[6] += num_new_fishes
            num_fishes[8] = num_new_fishes
        return sum(num_fishes.values())


test = Puzzle('test.txt')
assert test.part1() == 5934
assert test.part2() == 26984457539

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
