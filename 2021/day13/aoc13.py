class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()

        def parse_dot_line(line):
            point = line.split(',')
            assert len(point) == 2
            return (int(point[0]), int(point[1]))

        def parse_fold_line(line):
            assert line.startswith("fold along ")
            line = line[len("fold along "):]
            fold = line.split('=')
            assert len(fold) == 2
            return (fold[0], int(fold[1]))

        groups = data.split('\n\n')
        dots = groups[0].splitlines()
        folds = groups[1].splitlines()

        self.points = {parse_dot_line(line) for line in dots}
        self.folds = [parse_fold_line(line) for line in folds]

    @staticmethod
    def fold_point(point, fold):
        if fold[0] == 'x' and point[0] > fold[1]:
            return (2 * fold[1] - point[0], point[1])
        elif fold[0] == 'y' and point[1] > fold[1]:
            return (point[0], 2 * fold[1] - point[1])
        return point

    @staticmethod
    def write_svg(points):
        scale = 10
        width = max([point[0] for point in points]) + 2
        height = max([point[1] for point in points]) + 2
        filename = "day13.svg"
        print('Writing frame to file:', filename)
        file = open(filename, 'w')
        file.write(
            f'<svg height="{height * scale}px" width="{width * scale}px" viewBox="{-1} {-1} {width} {height}" xmlns="http://www.w3.org/2000/svg">\n')
        for point in points:
            file.write(
                f'\t<circle cx="{point[0]}" cy="{point[1]}" r="0.5"/>\n')
        file.write('</svg>')
        file.close()

    def part1(self):
        points = set()
        for point in self.points:
            points.add(self.fold_point(point, self.folds[0]))
        return len(points)

    def part2(self):
        points = self.points
        for fold in self.folds:
            new_points = set()
            for point in points:
                new_points.add(self.fold_point(point, fold))
            (points, new_points) = (new_points, points)
        self.write_svg(points)


test = Puzzle('test.txt')
assert test.part1() == 17
# assert test.part2() == 2
print("Part 2:", test.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
