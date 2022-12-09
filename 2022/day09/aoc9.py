def update_head(head, direction):
    if direction == "R":
        return (head[0] + 1, head[1])
    if direction == "L":
        return (head[0] - 1, head[1])
    if direction == "U":
        return (head[0], head[1] + 1)
    if direction == "D":
        return (head[0], head[1] - 1)
    raise ValueError("Invalid direction.")

def is_adjacent(head, tail):
    if max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) <= 1:
        return True
    return False 


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, "r")
        lines = file.read().splitlines()
        def parse_line(line):
            data = line.split()
            return (data[0], int(data[1]))
        self.moves = [parse_line(line) for line in lines]

    def part1(self):
        head = (0 ,0)
        tail = (0, 0)
        visited = {tail}

        def update_tail(tail, head):
            if is_adjacent(head, tail):
                return tail
            temp = list(tail)
            for axis in [0, 1]:
                if head[axis] > tail[axis]:
                    temp[axis] +=1
                if head[axis] < tail[axis]:
                    temp[axis] -=1
            return tuple(temp)

        for (direction, num_steps) in self.moves:
            for _ in range(num_steps):
                head = update_head(head, direction)
                tail = update_tail(tail, head)
                visited.add(tail)

        return len(visited)

    def part2(self):
        head = (0 ,0)
        tail = [(0, 0) for _ in range(9)]
        visited = {tail[-1]}

        def update_tail(tail, head):
            for index, knot in enumerate(tail):
                prev = head if index == 0 else tail[index - 1]
                if is_adjacent(prev, knot):
                    continue
                temp = list(knot)
                for axis in [0, 1]:
                    if prev[axis] > knot[axis]:
                        temp[axis] +=1
                    if prev[axis] < knot[axis]:
                        temp[axis] -=1
                    tail[index] = tuple(temp)
            return tail

        for (direction, num_steps) in self.moves:
            for _ in range(num_steps):
                head = update_head(head, direction)
                tail = update_tail(tail, head)
                visited.add(tail[-1])

        return len(visited)


test1 = Puzzle('test1.txt')
assert test1.part1() == 13
assert test1.part2() == 1

test2 = Puzzle('test2.txt')
assert test2.part2() == 36

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
