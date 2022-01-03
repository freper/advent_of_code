import math
from os import stat_result
from typing_extensions import IntVar

index_map = {'w': 0, 'x': 1, 'y': 2, 'z': 3}


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        groups = data.split('inp w\n')

        def parse_line(line):
            data = line.split(' ')
            return (data[0], data[1], data[2])

        instructions = list()
        for group in groups:
            if not group:
                continue
            lines = group.splitlines()
            instructions.append([parse_line(line) for line in lines])
        self.instructions = instructions

    @staticmethod
    def apply(instruction, state):
        i = index_map[instruction[1]]
        var = instruction[2]
        if var in index_map.keys():
            var = state[index_map[var]]
        else:
            var = int(var)
        if instruction[0] == "add":
            state[i] += var
        elif instruction[0] == "mul":
            state[i] *= var
        elif instruction[0] == "div":
            state[i] = int(state[i] / var)
        elif instruction[0] == "mod":
            state[i] = state[i] % var
        elif instruction[0] == "eql":
            state[i] = 1 if state[i] == var else 0
        return state

    def check(self, index, input):
        output = input
        for instruction in self.instructions[index]:
            output = self.apply(instruction, output)
        output[0] = 0
        output[1] = 0
        output[2] = 0
        # output[0] = output[0] % 26
        # output[1] = output[1] % 26
        # output[2] = output[2] % 26
        # output[3] = output[3] % 26
        return output

    def part1(self):
        states = {(0, 0, 0, 0)}
        for digit in range(0, 14):
            output_states = set()
            for value in range(1, 10):
                for input_state in states:
                    state = list(input_state)
                    state[0] = value
                    self.check(digit, state)
                    output_states.add(tuple(state))
            states.update(output_states)
            print(len(states))
        valid_states = {state for state in states if state[3] == 0}
        number = [0] * 14
        for digit in reversed(range(0, 14)):
            for value in reversed(range(1, 10)):
                assert valid_states
                valid_input_states = set()
                for input_state in states:
                    state = list(input_state)
                    state[0] = value
                    self.check(digit, state)
                    state = tuple(state)
                    if state in valid_states:
                        print(digit, value)
                        valid_input_states.add(input_state)
                valid_states, valid_input_states = valid_input_states, valid_states
        return number

    def part2(self):
        return 2


# test = Puzzle('test.txt')
# assert test.part1() == 1(
# assert test.part2() == 2)
# print("Part 1:", test.part1())
# print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
