import numpy as np


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def init(self):
        board_status = [None] * len(self.boards)
        for n, board in enumerate(self.boards):
            assert board.shape == (self.board_shape)
            board_status[n] = np.zeros(self.board_shape, dtype=int)
        self.board_status = board_status
        self.previous_winners = set()

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        groups = data.split('\n\n')
        self.numbers = [int(value) for value in groups[0].split(',')]

        num_boards = len(groups) - 1
        boards = [None] * num_boards
        for n in range(num_boards):
            rows = groups[n + 1].splitlines()
            size = len(rows)
            boards[n] = np.zeros((size, size), dtype=int)
            for i, row in enumerate(rows):
                values = row.split()
                for j, value in enumerate(values):
                    boards[n][i, j] = value
        self.boards = boards
        self.board_shape = (size, size)
        self.init()

    def update_board_status(self, number):
        for n, board in enumerate(self.boards):
            if not number in board:
                continue
            for i in range(self.board_shape[0]):
                for j in range(self.board_shape[1]):
                    if board[i, j] == number:
                        self.board_status[n][i, j] = 1

    def check_board_status(self):
        winners = set()
        for n, status in enumerate(self.board_status):
            if n in self.previous_winners:
                continue
            for row in range(self.board_shape[0]):
                if np.all(status[row, :] == 1):
                    winners.add(n)
            for col in range(self.board_shape[1]):
                if np.all(status[:, col] == 1):
                    winners.add(n)
        self.previous_winners.update(winners)
        return winners

    def calculate_unmarked_sum(self, board_index):
        board = self.boards[board_index]
        status = self.board_status[board_index]
        sum = 0
        for i in range(self.board_shape[0]):
            for j in range(self.board_shape[1]):
                if status[i, j] == 0:
                    sum += board[i, j]
        return sum

    def part1(self):
        self.init()
        for number in self.numbers:
            self.update_board_status(number)
            if winners := self.check_board_status():
                assert len(winners) == 1
                return number * self.calculate_unmarked_sum(winners.pop())
        return None

    def part2(self):
        self.init()
        last_winner_score = None
        for number in self.numbers:
            self.update_board_status(number)
            if winners := self.check_board_status():
                if len(winners) > 1:
                    continue  # We are only interested in unique winners
                score = number * self.calculate_unmarked_sum(winners.pop())
                last_winner_score = score
        return last_winner_score


test = Puzzle('test.txt')
assert test.part1() == 4512
assert test.part2() == 1924
# print("Part 1:", test.part1())
# print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
