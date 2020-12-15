class Puzzle:
    def __init__(self, input=None):
        if input:
            self.input = input
        else:
            self.input = []

    @staticmethod
    def determine_spoken_number(values, num_turns):
        assert num_turns > len(values)
        history = {}
        turn = 1
        for value in values:
            history[value] = (turn, None)
            prev = value
            turn += 1
        while turn <= num_turns:
            if prev not in history.keys():
                current = 0
            else:
                if history[prev][1]:
                    current = history[prev][0] - history[prev][1]
                else:
                    current = 0
            if current in history.keys():
                history[current] = (turn, history[current][0])
            else:
                history[current] = (turn, None)
            prev = current
            turn += 1
        return prev

    def part1(self, values=None):
        if not values:
            values = self.input
        return Puzzle.determine_spoken_number(values, 2020)

    def part2(self, values=None):
        if not values:
            values = self.input
        return Puzzle.determine_spoken_number(values, 30000000)


test = Puzzle()
assert test.part1([0, 3, 6]) == 436
assert test.part1([1, 3, 2]) == 1
assert test.part1([2, 1, 3]) == 10
assert test.part1([1, 2, 3]) == 27
assert test.part1([2, 3, 1]) == 78
assert test.part1([3, 2, 1]) == 438
assert test.part1([3, 1, 2]) == 1836

puzzle = Puzzle([15, 5, 1, 4, 7, 0])
print("Print 1:", puzzle.part1())
print("Print 2:", puzzle.part2())
