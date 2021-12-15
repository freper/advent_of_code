from collections import deque


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        lines = data.splitlines()
        rows = len(lines)
        cols = len(lines[0])

        map = dict()
        for row, line in enumerate(lines):
            for col, value in enumerate(line):
                map[(row, col)] = int(value)
        self.riskmap = map
        self.target = (rows - 1, cols - 1)

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
        self.fulltarget = (5 * rows - 1, 5 * cols - 1)

    @staticmethod
    def find_minimum_risk(start, target, riskmap):
        risks = {start: 0}
        nodes = deque([start])
        while nodes:
            node = nodes.popleft()
            for offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_node = (node[0] + offset[0], node[1] + offset[1])
                if new_node not in riskmap.keys():
                    continue
                new_risk = risks[node] + riskmap[new_node]
                if new_node not in risks.keys() or new_risk < risks[new_node]:
                    risks[new_node] = new_risk
                    nodes.append(new_node)
        return risks[target]

    def part1(self):
        return self.find_minimum_risk((0, 0), self.target, self.riskmap)

    def part2(self):
        return self.find_minimum_risk((0, 0), self.fulltarget, self.fullriskmap)


test = Puzzle('test.txt')
assert test.part1() == 40
assert test.part2() == 315

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
