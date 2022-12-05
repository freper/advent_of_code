def priority(item):
    value = ord(item)
    if value >= 97 and value <= 122:
        return value - 97 + 1
    if value >= 65 and value <= 90:
        return value - 65 + 27

def shared_item(rucksack):
    shared_items = rucksack[0].intersection(rucksack[1])
    return list(shared_items)[0]

def shared_item_group(rucksacks):
    combined_rucksacks = [(rucksack[0] | rucksack[1]) for rucksack in rucksacks]
    shared_items = set.intersection(*combined_rucksacks)
    return list(shared_items)[0]

class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        def rucksack(line):
            num_elements = len(line)
            return (set(line[:int(num_elements/2)]), set(line[int(num_elements/2):]))
        self.rucksacks = [rucksack(line) for line in lines]

    def part1(self):
        priorities = [priority(shared_item(rucksack)) for rucksack in self.rucksacks]
        return sum(priorities)

    def part2(self):
        priorities = [priority(shared_item_group(self.rucksacks[i:(i + 3)])) for i in range(0, len(self.rucksacks), 3)]
        return sum(priorities)


test = Puzzle('test.txt')
assert test.part1() == 157
assert test.part2() == 70

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
