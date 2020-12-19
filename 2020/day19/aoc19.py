import re


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read().split("\n\n")

        def parse_rules(lines):
            rules = dict()
            for line in lines:
                tmp = line.split(": ")
                i = int(tmp[0])
                m = re.fullmatch(r'"([a-z])"', tmp[1])
                if m:
                    rules[i] = m.group(1)
                else:
                    rules[i] = [[int(x) for x in l.split(' ')] for l in tmp[1].split(" | ")]
            return rules
        self.rules = parse_rules(data[0].splitlines())
        self.messages = data[1].splitlines()

    def is_valid(self, message, rules):
        if len(rules) > len(message):
            return False
        elif len(message) == 0 or len(rules) == 0:
            return len(message) == 0 and len(rules) == 0

        x = rules.pop(0)
        if type(x) == str:
            if message[0] == x:
                return self.is_valid(message[1:], rules.copy())
        else:
            for rule in self.rules[x]:
                if self.is_valid(message, list(rule) + rules):
                    return True
        return False

    def part1(self):
        num_valid_messages = 0
        for message in self.messages:
            if self.is_valid(message, self.rules[0][0].copy()):
                num_valid_messages += 1
        return num_valid_messages

    def part2(self):
        self.rules[8] = [[42], [42, 8]]
        self.rules[11] = [[42, 31], [42, 11, 31]]
        num_valid_messages = 0
        for message in self.messages:
            if self.is_valid(message, self.rules[0][0].copy()):
                num_valid_messages += 1
        return num_valid_messages


test1 = Puzzle('test1.txt')
assert test1.part1() == 2

test2 = Puzzle('test2.txt')
assert test2.part1() == 3
assert test2.part2() == 12

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
