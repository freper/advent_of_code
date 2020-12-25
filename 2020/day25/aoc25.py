class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        self.card_pub_key = int(lines[0])
        self.door_pub_key = int(lines[1])

    def transform(self, subject_number, loop_size):
        value = 1
        for _ in range(loop_size):
            value *= subject_number
            value %= 20201227
        return value

    def find_loop_size(self, key):
        loop_size = 0
        subject_number = 7
        value = 1
        while not value == key:
            loop_size += 1
            value *= subject_number
            value %= 20201227

        return loop_size

    def part1(self):
        card_loop_size = self.find_loop_size(self.card_pub_key)
        door_loop_size = self.find_loop_size(self.door_pub_key)
        door_encryption_key = self.transform(self.card_pub_key, door_loop_size)
        card_encryption_key = self.transform(self.door_pub_key, card_loop_size)
        assert door_encryption_key == card_encryption_key
        return card_encryption_key


test = Puzzle('test.txt')
assert test.part1() == 14897079

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
