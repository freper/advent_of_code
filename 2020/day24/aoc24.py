from math import sqrt


class Tile:
    def __init__(self, coord=(0, 0)):
        self.x = coord[0]
        self.y = coord[1]

    def offset(self, direction):
        if direction == 'e':
            self.x += 1
        elif direction == 'w':
            self.x -= 1
        elif direction == 'se':
            self.y += 1
        elif direction == 'nw':
            self.y -= 1
        elif direction == 'ne':
            self.x += 1
            self.y -= 1
        elif direction == 'sw':
            self.x -= 1
            self.y += 1
        else:
            raise ValueError("Invalid direction")
        return self.coord()

    def coord(self):
        return (self.x, self.y)


class Puzzle:
    def __init__(self, filename, write_frames=False):
        self.write_frames = write_frames
        self.day = 0
        self.frame_counter = 0
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()

        def parse_line(line):
            l = [c for c in line]
            tile = Tile()
            while len(l) > 0:
                d = l.pop(0)
                if d not in ['e', 'w']:
                    d += l.pop(0)
                tile.offset(d)
            return tile.coord()

        self.black_tiles = set()
        if self.write_frames:
            self.write_svg()
        for line in lines:
            coord = parse_line(line)
            if coord in self.black_tiles:
                self.black_tiles.remove(coord)
            else:
                self.black_tiles.add(coord)
            if self.write_frames:
                self.write_svg()
        if self.write_frames:
            self.write_svg()

    def write_svg(self):
        width = 128
        height = 128
        scale = 12

        xaxis = (1, 0)
        yaxis = (1/2, sqrt(3)/2)

        def tile_corners(center):
            corners = [(0, 1.0 / sqrt(3)),
                       (0.5, 0.5 / sqrt(3)),
                       (0.5, -0.5 / sqrt(3)),
                       (0, -1.0 / sqrt(3)),
                       (-0.5, -0.5 / sqrt(3)),
                       (-0.5, 0.5 / sqrt(3))]
            return " ".join([f'{center[0] + corner[0]},{center[1] + corner[1]}'
                             for corner in corners])

        filename = f'frame_{self.day:03}_{self.frame_counter:03}.svg'
        print('Writing frame to file:', filename)
        file = open(filename, 'w')
        file.write(
            f'<svg height="{height * scale}px" width="{width * scale}px" viewBox="{-width/2} {-height/2} {width} {height}" xmlns="http://www.w3.org/2000/svg">\n')
        for y in range(int(-height / sqrt(3)), int(height / sqrt(3)) + 1):
            for x in range(int(-3 * width / 4 - height / sqrt(12)),
                           int(3 * width / 4 + height / sqrt(12)) + 1):
                center = (x * xaxis[0] + y * yaxis[0],
                          x * xaxis[1] + y * yaxis[1])
                if center[0] < -width / 2 or center[0] > width / 2 or center[1] < -height / 2 or center[1] > height / 2:
                    continue
                points = tile_corners(center)
                if (x, y) in self.black_tiles:
                    file.write(
                        f'\t<polygon points="{points}" style="fill:black;stroke:black;stroke-width:0.05"/>\n')
                else:
                    file.write(
                        f'\t<polygon points="{points}" style="fill:white;stroke:black;stroke-width:0.05"/>\n')
        file.write('</svg>')
        file.close()
        self.frame_counter += 1

    def check_neighbours(self):
        self.black_tiles_with_black_neighbours = dict()
        self.white_tiles_with_black_neighbours = dict()
        for coord in self.black_tiles:
            self.black_tiles_with_black_neighbours[coord] = 0
            for d in ['e', 'w', 'se', 'nw', 'ne', 'sw']:
                neighbour = Tile(coord).offset(d)
                if neighbour in self.black_tiles:
                    self.black_tiles_with_black_neighbours[coord] += 1
                elif neighbour in self.white_tiles_with_black_neighbours.keys():
                    self.white_tiles_with_black_neighbours[neighbour] += 1
                else:
                    self.white_tiles_with_black_neighbours[neighbour] = 1

    def flip_tiles(self):
        for coord, n in self.black_tiles_with_black_neighbours.items():
            if n not in [1, 2]:
                self.black_tiles.remove(coord)
        for coord, n in self.white_tiles_with_black_neighbours.items():
            if n == 2:
                self.black_tiles.add(coord)
        self.day += 1

    def part1(self):
        return len(self.black_tiles)

    def part2(self, num_days=100):
        while self.day < num_days:
            self.check_neighbours()
            self.flip_tiles()
            if self.write_frames:
                self.write_svg()
        return len(self.black_tiles)


test = Puzzle('test.txt')
assert test.part1() == 10
assert test.part2(1) == 15
assert test.part2(10) == 37
assert test.part2() == 2208

puzzle = Puzzle('input.txt', True)
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
