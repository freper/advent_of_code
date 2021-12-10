
score_table1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_table2 = {")": 1, "]": 2, "}": 3, ">": 4}

open_brackets = {"(", "[", "{", "<"}
close_brackets = {")", "]", "}", ">"}
close_to_open_bracket = {")": "(", "]": "[", "}": "{", ">": "<"}
open_to_close_bracket = {"(": ")", "[": "]", "{": "}", "<": ">"}


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        self.input = data.splitlines()

    def part1(self):
        score = 0
        for line in self.input:
            stack = []
            for i, bracket in enumerate(line):
                if bracket in open_brackets:
                    stack.append(bracket)
                elif bracket in close_brackets:
                    open_bracket = close_to_open_bracket[bracket]
                    if len(stack) == 0 or not stack[-1] == open_bracket:
                        score += score_table1[bracket]
                        break
                    stack.pop()
        return score

    def part2(self):
        scores = []
        for line in self.input:
            stack = []
            corrupt = False
            for i, bracket in enumerate(line):
                if bracket in open_brackets:
                    stack.append(bracket)
                elif bracket in close_brackets:
                    open_bracket = close_to_open_bracket[bracket]
                    if len(stack) == 0 or not stack[-1] == open_bracket:
                        corrupt = True
                        break  # Ignore corrupt lines
                    stack.pop()
            if not corrupt and len(stack) > 0:  # Incomplete line
                score = 0
                stack.reverse()
                for bracket in stack:
                    close_bracket = open_to_close_bracket[bracket]
                    score = score * 5 + score_table2[close_bracket]
                scores.append(score)
        assert scores and len(scores) % 2 == 1
        scores.sort()
        return scores[int((len(scores) - 1) / 2)]


test = Puzzle('test.txt')
assert test.part1() == 26397
assert test.part2() == 288957
# print("Part 1:", test.part1())
# print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
