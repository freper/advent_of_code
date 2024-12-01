class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        def parse_line(line):
            data = line.split()
            return (data[0], data[1])
        list_data = [parse_line(line) for line in lines]
        self.list1 = [int(data[0]) for data in list_data]
        self.list2 = [int(data[1]) for data in list_data]
        
    
    def part1(self):
        sum = 0
        for data1, data2 in zip(sorted(self.list1), sorted(self.list2)):
            sum += abs(data1 - data2)
        return sum


    def part2(self):
        score = 0
        for data1 in self.list1:
            num = len([data2 for data2 in self.list2 if data2 == data1])
            score += data1 * num
        return score


test = Puzzle('test.txt')
assert test.part1() == 11
assert test.part2() == 31

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
