class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        lines = data.splitlines()

        map = dict()
        for row, line in enumerate(lines):
            for col, value in enumerate(line):
                map[(row, col)] = int(value)
        self.riskmap = map

        rows = len(lines)
        cols = len(lines[0])
        fullmap = dict()
        for rowtile in range(5):
            for coltile in range(5):
                for position, risk in map.items():
                    row = rowtile * rows + position[1]
                    col = coltile * cols + position[0]
                    fullrisk = risk + rowtile + coltile
                    fullrisk = ((fullrisk - 1) % 9) + 1
                    fullmap[(row, col)] = fullrisk
        self.fullriskmap = fullmap

    def part1(self):
        new_risks = {(0, 0): 0}
        updated = True
        while updated:
            risks = dict()
            risks, new_risks = new_risks, risks
            updated = False
            for position, risk in risks.items():
                for offset in [(0, 1), (1, 0)]:
                    new_position = (position[0] + offset[0], position[1] + offset[1])
                    if not new_position in self.riskmap.keys():
                        continue
                    new_risk = risk + self.riskmap[new_position]
                    if new_position not in new_risks.keys() or new_risk < new_risks[new_position]:
                        new_risks[new_position] = new_risk
                    updated = True
        assert len(risks.values()) == 1
        return next(iter(risks.values()))

    def part2(self):
        new_risks = {(0, 0): 0}
        updated = True
        while updated:
            risks = dict()
            risks, new_risks = new_risks, risks
            updated = False
            for position, risk in risks.items():
                for offset in [(0, 1), (1, 0)]:
                    new_position = (position[0] + offset[0], position[1] + offset[1])
                    if not new_position in self.fullriskmap.keys():
                        continue
                    new_risk = risk + self.fullriskmap[new_position]
                    if new_position not in new_risks.keys() or new_risk < new_risks[new_position]:
                        new_risks[new_position] = new_risk
                    updated = True
        assert len(risks.values()) == 1
        return next(iter(risks.values()))


test = Puzzle('test.txt')
assert test.part1() == 40
assert test.part2() == 315

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
