class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        groups = data.split('\n\n')
        self.template = groups[0].splitlines()[0]
        lines = groups[1].splitlines()
        self.rules = dict()
        for line in lines:
            data = line.split(' -> ')
            self.rules[data[0]] = data[1]

    def init(self):
        elements = {self.template[0]: 1}
        pairs = dict()

        polymer = self.template
        for i in range(1, len(polymer)):
            element = polymer[i]
            if element in elements.keys():
                elements[element] += 1
            else:
                elements[element] = 1

            pair = polymer[i - 1] + polymer[i]
            if pair in pairs.keys():
                pairs[pair] += 1
            else:
                pairs[pair] = 1
        self.elements = elements
        self.pairs = pairs

    def update(self):
        new_pairs = dict()
        for pair, count in self.pairs.items():
            if pair in self.rules.keys():
                element = self.rules[pair]
                if element in self.elements.keys():
                    self.elements[element] += count
                else:
                    self.elements[element] = count

                for new_pair in [pair[0] + element, element + pair[1]]:
                    if new_pair in new_pairs.keys():
                        new_pairs[new_pair] += count
                    else:
                        new_pairs[new_pair] = count
                self.pairs[pair] = 0
        for pair, count in new_pairs.items():
            if pair in self.pairs.keys():
                self.pairs[pair] += count
            else:
                self.pairs[pair] = count

    def part1(self):
        self.init()
        for _ in range(10):
            self.update()
        max_value = max(self.elements.values())
        min_value = min(self.elements.values())
        return max_value - min_value

    def part2(self):
        self.init()
        for _ in range(40):
            self.update()
        max_value = max(self.elements.values())
        min_value = min(self.elements.values())
        return max_value - min_value


test = Puzzle('test.txt')
assert test.part1() == 1588
assert test.part2() == 2188189693529

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
