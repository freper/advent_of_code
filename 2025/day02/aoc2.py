def is_invalid_1(id):
    id = str(id)
    length = len(id)
    if length % 2 != 0:
        return False
    n = int(length / 2)
    if id[0:n] * 2 == id:
        return True
    return False

def is_invalid_2(id):
    id = str(id)
    length = len(id)
    for i in range(1, int(length / 2) + 1):
        if length % i != 0:
            continue
        n = int(length / i)
        if id[0:i] * n == id:
            return True
    return False

def find_invalid_ids(sequence, check_invalid):
    invalid_ids = []
    for id in range(int(sequence[0]), sequence[1] + 1):
        if check_invalid(id):
            invalid_ids.append(id)
    return invalid_ids

class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        self.sequences = [[int(value) for value in sequence.split("-")] for sequence in file.read().split(",")]
        
    def part1(self):
        sum = 0
        for sequence in self.sequences:
            invalid_ids = find_invalid_ids(sequence, is_invalid_1)
            for id in invalid_ids:
                sum += id
        return sum

    def part2(self):
        sum = 0
        for sequence in self.sequences:
            invalid_ids = find_invalid_ids(sequence, is_invalid_2)
            for id in invalid_ids:
                sum += id
        return sum

test = Puzzle('test.txt')
assert test.part1() == 1227775554
assert test.part2() == 4174379265

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
