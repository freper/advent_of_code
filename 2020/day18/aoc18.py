class Puzzle:
    def __init__(self, filename=None):
        if filename:
            self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        self.input = data.splitlines()

    def get_value(self, expression):
        if expression.startswith('('):
            i = 1
            n = 0
            while True:
                if expression[i] == ')':
                    if n == 0:
                        break
                    else:
                        n -= 1
                elif expression[i] == '(':
                    n += 1
                i += 1
            if i < len(expression) - 1:
                return (self.evaluate1(expression[1:i]), expression[(i+2):])
            else:
                return (self.evaluate1(expression[1:i]), "")
        else:
            tmp = expression.split(' ')
            if tmp:
                if len(tmp) > 1:
                    return (int(tmp[0]), ' '.join(tmp[1:]))
                else:
                    return (int(tmp[0]), "")
            else:
                return None

    def evaluate1(self, line):
        (lhs, line) = self.get_value(line)
        while len(line) > 0:
            op = line[0]
            (rhs, line) = self.get_value(line[2:])
            if op == '+':
                lhs += rhs
            elif op == '*':
                lhs *= rhs
            else:
                raise ValueError()
        return lhs

    def evaluate2(self, line):
        (lhs, line) = self.get_value(line)
        while len(line) > 0:
            op = line[0]
            (rhs, line) = self.get_value(line[2:])
            if op == '+':
                lhs += rhs
            elif op == '*':
                lhs *= rhs
            else:
                raise ValueError()
        return lhs

    def part1(self):
        sum = 0
        for line in self.input:
            sum += self.evaluate1(line)
        return sum

    def part2(self):
        return 2


test = Puzzle()
assert test.evaluate1("1 + 2 * 3 + 4 * 5 + 6") == 71
assert test.evaluate1("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert test.evaluate1("2 * 3 + (4 * 5)") == 26
assert test.evaluate1("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
assert test.evaluate1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
assert test.evaluate1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632

print(test.evaluate2("1 + (2 * 3) + (4 * (5 + 6))"))  # == 51.
print(test.evaluate2("2 * 3 + (4 * 5)"))  # == 46.
print(test.evaluate2("5 + (8 * 3 + 9 + 3 * 4 * 3)"))  # == 1445.
print(test.evaluate2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))  # == 669060.
print(test.evaluate2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))  # == 23340.

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
# print("Part 2:", puzzle.part2())
