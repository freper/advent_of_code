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
    def __init__(self, filename):
        self.read_input(filename)
        self.day = 0

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
        for line in lines:
            coord = parse_line(line)
            if coord in self.black_tiles:
                self.black_tiles.remove(coord)
            else:
                self.black_tiles.add(coord)

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
        return len(self.black_tiles)


test = Puzzle('test.txt')
assert test.part1() == 10
assert test.part2(1) == 15
assert test.part2(10) == 37
assert test.part2() == 2208

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
