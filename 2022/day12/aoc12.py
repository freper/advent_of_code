import numpy as np

class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        rows = len(lines)
        cols = len(lines[0])
        height = np.empty((rows, cols), dtype=int)
        start = None
        end = None
        valley = []
        for row, line in enumerate(lines):
            for col, val in enumerate(line):
                if val == "S":
                    start = (row, col)
                    height[row, col] = ord("a")
                elif val == "E":
                    end = (row, col)
                    height[row, col] = ord("z")
                else:
                    height[row, col] = ord(val)
                if height[row, col] == ord("a"):
                    valley.append((row, col))
        self.start = start
        self.end = end
        self.height = height
        self.valley = valley

    def shortest_path(self, start):
        end = self.end
        height = self.height
        visited = np.full(height.shape, np.Inf, dtype=int)
        def available_directions(height, position):
            result = []
            current = height[position[0], position[1]]
            for direction in [(0,-1), (0,1), (-1,0), (1,0)]:
                destination = (position[0] + direction[0], position[1] + direction[1])
                if destination[0] < 0 or destination[0] >= height.shape[0]:
                    continue
                if destination[1] < 0 or destination[1] >= height.shape[1]:
                    continue
                if height[destination[0], destination[1]] <= current + 1:
                    result.append(direction)
            return result
        visited = {start: 0}
        choices = {start: available_directions(height, start)}
        while choices:
            updated_choices = {}
            for position, directions in choices.items():
                current = visited[position]
                for direction in directions:
                    destination = (position[0] + direction[0], position[1] + direction[1])
                    if destination not in visited or visited[destination] > current + 1:
                        updated_choices[destination] = available_directions(height, destination)
                        visited[destination] = current + 1
            choices = updated_choices
        return visited[end] if end in visited.keys() else np.Inf

    def part1(self):
        start = self.start
        return self.shortest_path(start)

    def part2(self):
        shortest_pats = [self.shortest_path(start) for start in self.valley]
        return min(shortest_pats)


test = Puzzle('test.txt')
assert test.part1() == 31
assert test.part2() == 29

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
