import re


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
                return (self.evaluate(expression[1:i]), expression[(i+2):])
            else:
                return (self.evaluate(expression[1:i]), "")
        else:
            tmp = expression.split(' ')
            if tmp:
                if len(tmp) > 1:
                    return (int(tmp[0]), ' '.join(tmp[1:]))
                else:
                    return (int(tmp[0]), "")
            else:
                return None

    def evaluate(self, line):
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

    def simplify(self, line):
        re1 = re.compile(r"\d+ \+ \d+")
        re2 = re.compile(r"\(\d+\)")
        re3 = re.compile(r"\([\d \*]+\)")
        finished = False
        while not finished:
            finished = True
            m = re1.search(line)
            if m:
                result = str(eval(m.group(0)))
                line = re1.sub(result, line, count=1)
                finished = False
            m = re2.search(line)
            if m:
                result = str(eval(m.group(0)))
                line = re2.sub(result, line, count=1)
                finished = False
            m = re3.search(line)
            if m:
                result = str(eval(m.group(0)))
                line = re3.sub(result, line, count=1)
                finished = False
        return line

    def part1(self):
        sum = 0
        for line in self.input:
            sum += self.evaluate(line)
        return sum

    def part2(self):
        sum = 0
        for line in self.input:
            line = self.simplify(line)
            sum += self.evaluate(line)
        return sum


test = Puzzle()
assert test.evaluate("1 + 2 * 3 + 4 * 5 + 6") == 71
assert test.evaluate("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert test.evaluate("2 * 3 + (4 * 5)") == 26
assert test.evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
assert test.evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
assert test.evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
assert test.evaluate(test.simplify("1 + (2 * 3) + (4 * (5 + 6))")) == 51
assert test.evaluate(test.simplify("2 * 3 + (4 * 5)")) == 46
assert test.evaluate(test.simplify("5 + (8 * 3 + 9 + 3 * 4 * 3)")) == 1445
assert test.evaluate(test.simplify("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")) == 669060
assert test.evaluate(test.simplify("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")) == 23340

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
