import numpy as np


class Puzzle:
    def __init__(self, line):
        self.input = [int(x) for x in line]

    def move_cups(self, cups):
        current = cups.pop(0)
        removed = cups[0:3]
        cups = cups[3:]

        # Find destination cup
        destination = current - 1
        while True:
            if destination in cups:
                break
            elif destination < min(cups):
                destination = max(cups)
                break
            destination -= 1
        cups.append(current)
        i = cups.index(destination)
        cups = cups[i:] + cups[:i]
        cups = [cups[0]] + removed + cups[1:]
        i = cups.index(current)
        cups = cups[i:] + cups[:i]
        cups = cups[1:] + cups[:1]
        return cups

    def part1(self, num_moves=100):
        cups = self.input.copy()
        for i in range(num_moves):
            cups = self.move_cups(cups)
        i = cups.index(1)
        cups = cups[i:] + cups[:i]
        return "".join([str(x) for x in cups[1:]])

    def part2(self, num_moves=10000000, num_cups=1000000):
        cups = self.input.copy()
        num_cups = max(len(cups), num_cups)
        next_index = [i for i in range(1, num_cups + 1)]
        for i, x in enumerate(cups):
            next_index[x - 1] = cups[i + 1] - 1 if i + 1 < len(cups) else max(cups)
        next_index[-1] = cups[0] - 1

        current = cups[0] - 1
        for _ in range(num_moves):
            a = next_index[current]
            b = next_index[a]
            c = next_index[b]
            x = next_index[c]
            d = (current - 1) % num_cups
            while d in [a, b, c]:
                d = (d - 1) % num_cups
            e = next_index[d]
            next_index[d] = a
            next_index[c] = e
            next_index[current] = x
            current = next_index[current]

        v1 = next_index[0]
        v2 = next_index[v1]
        return (v1 + 1) * (v2 + 1)


test = Puzzle("389125467")
assert test.part1(10) == "92658374"
assert test.part1() == "67384529"
assert test.part2() == 149245887792

puzzle = Puzzle("418976235")
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
