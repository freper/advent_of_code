def overlap(d, r):
    if d[0] <= r[1] and r[0] <= d[1]:
        return True
    return False

def update(disjoint, r):
    result = []
    overlaps = [r]
    for d in disjoint:
        if overlap(d, r):
            overlaps.append(d)
        else:
            result.append(d)
    d0 = min([d[0] for d in overlaps])
    d1 = max([d[1] for d in overlaps])
    result.append([d0, d1])
    return result

class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        groups = file.read().split("\n\n")
        self.fresh = [[int(id) for id in rn.split("-")] for rn in groups[0].split("\n")]
        self.available = [int(id) for id in groups[1].split("\n")]
        
    def is_fresh(self, id):
        for rn in self.fresh:
            if id >= rn[0] and id <= rn[1]:
                return True
        return False

    
    def overlap(self):
        min_id = 1e32
        max_id = 0
        for rn in self.fresh:
            if rn[0] < min_id:
                min_id = rn[0]
            if rn[1] > max_id:
                max_id = rn[1]
        return (min_id, max_id)
    
    def part1(self):
        num_fresh = 0
        for id in self.available:
            if self.is_fresh(id):
                num_fresh += 1
        return num_fresh

    def part2(self):
        disjoint = [self.fresh[0]]
        for r in self.fresh[1:]:
            disjoint = update(disjoint, r)
        sum = 0
        for d in disjoint:
            sum += d[1] - d[0] + 1
        return sum

test = Puzzle('test.txt')
assert test.part1() == 3
assert test.part2() == 14

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
