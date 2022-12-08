import numpy as np

class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, "r")
        lines = file.read().splitlines()
        self.map = np.array([[int(value) for value in line] for line in lines], dtype=int)

    def part1(self):
        (rows, cols) = self.map.shape
        num_visible_trees = 2 * (rows + cols - 2)
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                height = self.map[r, c]
                if np.all(height > self.map[:r, c]) or np.all(height > self.map[(r+1):, c]) or np.all(height > self.map[r, :c]) or np.all(height > self.map[r, (c+1):]):
                    num_visible_trees += 1
        return num_visible_trees

    def part2(self):
        (rows, cols) = self.map.shape
        best_score = 0
        def count_visible_trees(current_height, tree_heights):
            num_visible_trees = 0
            for tree_height in tree_heights.flat:
                num_visible_trees += 1
                if tree_height >= current_height:
                    return num_visible_trees
            return num_visible_trees

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                height = self.map[r, c]
                num_trees_left = count_visible_trees(height, np.flip(self.map[r, :c]))
                num_trees_right = count_visible_trees(height, self.map[r, (c+1):])
                num_trees_up = count_visible_trees(height, np.flip(self.map[:r, c]))
                num_trees_down = count_visible_trees(height, self.map[(r+1):, c])
                score = num_trees_left * num_trees_right * num_trees_up * num_trees_down
                best_score = max(best_score, score)
        return best_score


test = Puzzle('test.txt')
assert test.part1() == 21
assert test.part2() == 8

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
