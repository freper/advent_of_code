from copy import deepcopy
import re


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read().split("\n\n")

        def parse_rules(lines):
            index = dict()
            rules = dict()
            for line in lines:
                tmp = line.split(": ")
                i = int(tmp[0])
                m = re.fullmatch(r'"([a-z])"', tmp[1])
                if m:
                    rules[i] = m.group(1)
                    index[m.group(1)] = i
                else:
                    rules[i] = [tuple([int(x) for x in l.split(' ')]) for l in tmp[1].split(" | ")]
            return rules, index
        self.rules, self.index = parse_rules(data[0].splitlines())
        self.messages = data[1].splitlines()

    def expand_rule(self, x):
        options = set(self.rules[x])

        index = 0
        update_index = False
        while index < max([len(x) for x in options]):
            update_index = True
            updated_options = set()
            for option in options:
                if index >= len(option):
                    updated_options.add(option)
                    continue
                if option[index] in self.index.values():
                    updated_options.add(option)
                    continue
                update_index = False
                rules = self.rules[option[index]]
                for rule in rules:
                    l = list(deepcopy(option))
                    l = l[:index] + list(rule) + l[(index + 1):]
                    updated_options.add(tuple(deepcopy(l)))
            options = updated_options
            if update_index:
                index += 1
        return options

    def valid_messages(self, x):
        options = self.expand_rule(x)
        messages = set()
        for option in options:
            message = [self.rules[x] for x in option]
            messages.add("".join(message))
        return messages

    def part1(self):
        valid_messages = self.valid_messages(0)
        sum = 0
        for message in self.messages:
            if message in valid_messages:
                sum += 1
        return sum


test = Puzzle('test.txt')
assert test.part1() == 2

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
