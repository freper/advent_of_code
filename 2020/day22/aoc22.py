class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)
        self.history = set()

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read().split("\n\n")
        self.player1 = [int(x) for x in data[0].splitlines()[1:]]
        self.player2 = [int(x) for x in data[1].splitlines()[1:]]

    def play_game(self, cards1, cards2):
        while not len(cards1) == 0 and not len(cards2) == 0:
            card1 = cards1.pop(0)
            card2 = cards2.pop(0)

            if card1 > card2:
                cards1 += [card1, card2]
            else:
                cards2 += [card2, card1]

        if len(cards1) == 0:
            return self.calculate_score(cards2)
        else:
            return self.calculate_score(cards1)

    def play_recursive_game(self, cards1, cards2, game_no=1):
        # print("\n=== Game {} ===".format(game_no))
        previous = list()
        round_no = 1
        while not len(cards1) == 0 and not len(cards2) == 0:
            card1 = cards1.pop(0)
            card2 = cards2.pop(0)
            cards = tuple(cards1 + cards2)
            if cards in previous:
                return 1
            else:
                previous.append(cards)
            # print("\n-- Round {} (Game {}) --".format(round_no, game_no))
            # print("Player 1's deck:", cards1)
            # print("Player 2's deck:", cards2)
            # card1 = cards1.pop(0)
            # card2 = cards2.pop(0)
            # print("Player 1 plays:", card1)
            # print("Player 2 plays:", card2)
            if len(cards1) >= card1 and len(cards2) >= card2:
                # print("Playing a sub-game to determine the winner...")
                result = self.play_recursive_game(
                    cards1[:card1],
                    cards2[:card2],
                    game_no + 1)
                if result == 1:
                    # print("Player 1 wins round {} of game {}!".format(round_no, game_no))
                    cards1 += [card1, card2]
                else:
                    # print("Player 2 wins round {} of game {}!".format(round_no, game_no))
                    cards2 += [card2, card1]
            elif card1 > card2:
                # print("Player 1 wins round {} of game {}!".format(round_no, game_no))
                cards1 += [card1, card2]
            else:
                # print("Player 2 wins round {} of game {}!".format(round_no, game_no))
                cards2 += [card2, card1]
            round_no += 1
        if len(cards1) == 0:
            # print("The winner of game {} is player 2!".format(game_no))
            if game_no == 1:
                return self.calculate_score(cards2)
            else:
                return 2
        else:
            # print("The winner of game {} is player 1!".format(game_no))
            if game_no == 1:
                return self.calculate_score(cards1)
            else:
                return 1

    def calculate_score(self, cards):
        score = 0
        for n, card in enumerate(reversed(cards)):
            score += (n + 1) * card
        return score

    def part1(self):
        winning_score = self.play_game(self.player1.copy(), self.player2.copy())
        return winning_score

    def part2(self):
        winning_score = self.play_recursive_game(self.player1.copy(), self.player2.copy())
        return winning_score


test = Puzzle('test.txt')
assert test.part1() == 306
assert test.part2() == 291

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
