def result(round):
    translation = {"X": "A", "Y": "B", "Z": "C"}
    if round[0] == translation[round[1]]:
        return 3
    if (round[0] == "A" and round[1] == "Y") or (round[0] == "B" and round[1] == "Z") or (round[0] == "C" and round[1] == "X"):
        return 6
    return 0

def score(round):
    table = {"X": 1, "Y": 2, "Z": 3}
    return result(round) + table[round[1]]

def update(round):
    translation = {"A": "X", "B": "Y", "C": "Z"}
    if round[1] == "X":  # Loose
        if round[0] == "A":
            play = "Z"
        elif round[0] == "B":
            play = "X"
        else:
            assert round[0] == "C"
            play = "Y"
    elif round[1] == "Y":  # Draw
        play = translation[round[0]]
    else:  # Win
        assert round[1] == "Z"
        if round[0] == "A":
            play = "Y"
        elif round[0] == "B":
            play = "Z"
        else:
            assert round[0] == "C"
            play = "X"
    return (round[0], play)

class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        def strategy(line):
            data = line.split()
            return (data[0], data[1])
        self.rounds = [strategy(line) for line in lines]

    def part1(self):
        scores = [score(round) for round in self.rounds]
        return sum(scores)

    def part2(self):
        scores = [score(update(round)) for round in self.rounds]
        return sum(scores)


test = Puzzle('test.txt')
assert test.part1() == 15
assert test.part2() == 12

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
