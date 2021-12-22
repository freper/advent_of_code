import numpy as np


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        groups = data.split('\n\n')
        self.table = [1 if x == '#' else 0 for x in groups[0].splitlines()[0]]

        lines = groups[1].splitlines()
        rows = len(lines)
        cols = len(lines[0])
        image = np.zeros((rows, cols), dtype=int)
        for i in range(rows):
            for j in range(cols):
                image[i, j] = 1 if lines[i][j] == '#' else 0
        self.image = image

    def enhance_image(self, image, pad):
        rows = image.shape[0] + 2
        cols = image.shape[1] + 2

        original_image = np.full((rows, cols), pad, dtype=int)
        original_image[1:(rows - 1), 1:(cols - 1)] = image
        enhanced_image = np.zeros((rows, cols), dtype=int)

        def value(image, i, j, pad):
            if i < 0 or j < 0 or i > image.shape[0] - 1 or j > image.shape[1] - 1:
                return str(pad)
            return str(image[i, j])

        for i in range(rows):
            for j in range(cols):
                val = ""
                val += value(original_image, i - 1, j - 1, pad)
                val += value(original_image, i - 1, j, pad)
                val += value(original_image, i - 1, j + 1, pad)
                val += value(original_image, i, j - 1, pad)
                val += value(original_image, i, j, pad)
                val += value(original_image, i, j + 1, pad)
                val += value(original_image, i + 1, j - 1, pad)
                val += value(original_image, i + 1, j, pad)
                val += value(original_image, i + 1, j + 1, pad)
                enhanced_image[i, j] = self.table[int(val, 2)]
        pad = self.table[pad]
        return enhanced_image, pad

    def part1(self):
        image = self.image
        pad = 0
        for _ in range(2):
            image, pad = self.enhance_image(image, pad)
        return np.sum(image)

    def part2(self):
        image = self.image
        pad = 0
        for _ in range(50):
            image, pad = self.enhance_image(image, pad)
        return np.sum(image)


test = Puzzle('test.txt')
assert test.part1() == 35
assert test.part2() == 3351

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
