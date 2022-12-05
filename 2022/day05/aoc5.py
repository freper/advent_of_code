from copy import deepcopy
import re

class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, "r")
        groups = file.read().split("\n\n")
        def update_stack(line, stack):
            for i, j in enumerate(range(1, len(line), 4)):
                if line[j] == " ":
                    continue
                if i + 1 in stack.keys():
                    stack[i + 1].insert(0, line[j])
                else:
                    stack[i + 1] = [line[j]]
        stack = dict()
        lines = groups[0].splitlines()
        for line in lines[:-1]:
            update_stack(line, stack)
        self.stack = stack

        def move(line):
            assert line.startswith("move ")
            return tuple([int(val) for val in re.split(" from | to ", line[5:])])
        lines = groups[1].splitlines()
        self.moves = [move(line) for line in lines]


    def part1(self):
        def update_stack(move, stack):
            num = move[0]
            src = move[1]
            dst = move[2]
            for _ in range(num):
                stack[dst].append(stack[src].pop())
        stack = deepcopy(self.stack)
        for move in self.moves:
            update_stack(move, stack)
        top = ""
        for key in sorted(stack.keys()):
            top += stack[key][-1]
        return top

    def part2(self):
        def update_stack(move, stack):
            num = move[0]
            src = move[1]
            dst = move[2]
            stack[dst].extend(stack[src][-num:])
            del stack[src][-num:]
        stack = deepcopy(self.stack)
        for move in self.moves:
            update_stack(move, stack)
        top = ""
        for key in sorted(stack.keys()):
            top += stack[key][-1]
        return top


test = Puzzle('test.txt')
assert test.part1() == "CMZ"
assert test.part2() == "MCD"

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
