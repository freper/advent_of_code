class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        lines = data.splitlines()
        self.start_pos = [int(lines[0].split(':')[1]), int(lines[1].split(':')[1])]
        self.dice_values = list(range(1, 101))

    def init(self):
        self.current_pos = self.start_pos.copy()
        self.score = [0, 0]
        self.dice_counter = 0
        self.dice_index = 0

    def roll_dice(self):
        dice_value = self.dice_values[self.dice_index]
        self.dice_index = (self.dice_index + 1) % 100
        self.dice_counter += 1
        return dice_value

    def play_round(self, player_index):
        shift = self.roll_dice() + self.roll_dice() + self.roll_dice()
        self.current_pos[player_index] = ((self.current_pos[player_index] + shift - 1) % 10) + 1
        self.score[player_index] += self.current_pos[player_index]

    def shift_player(self, player_index):
        return (player_index + 1) % 2

    def part1(self):
        self.init()
        player_index = 0
        while True:
            self.play_round(player_index)
            other_player = self.shift_player(player_index)
            if self.score[player_index] >= 1000:
                return self.score[other_player] * self.dice_counter
            player_index = other_player

    def part2(self):
        return 2


test = Puzzle('test.txt')
assert test.part1() == 739785
# assert test.part2() == 2
print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
