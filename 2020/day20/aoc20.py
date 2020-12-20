import numpy as np
import re


class Tile:
    def __init__(self, tile_no, image):
        self.no = tile_no
        self.x = None
        self.y = None
        self.image = image
        self.flipped = False
        self.rotation = 0
        self.neighbours = []
        edges = [
            image[0, :].tolist(),
            image[:, -1].tolist(),
            image[-1, :].tolist(),
            image[:, 0].tolist()]
        self.edges_cw = [
            tuple(edges[0]),
            tuple(edges[1]),
            tuple(reversed(edges[2])),
            tuple(reversed(edges[3]))]
        self.edges_ccw = [
            tuple(reversed(edges[0])),
            tuple(reversed(edges[1])),
            tuple(edges[2]),
            tuple(edges[3])]


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read().split("\n\n")
        header = re.compile(r'Tile (\d+):')
        self.tiles = dict()
        for tile in data:
            lines = tile.splitlines()
            if len(lines) == 0:
                continue
            m = header.fullmatch(lines[0])
            assert m
            tile_no = int(m.group(1))
            image = np.array([[int(x == '#') for x in line] for line in lines[1:]], dtype=int)
            self.tiles[tile_no] = Tile(tile_no, image)

    def has_common_edge(self, tile1, tile2):
        for edge1 in tile1.edges_cw:
            for edge2 in tile2.edges_cw:
                if edge1 == edge2:
                    return True
            for edge2 in tile2.edges_ccw:
                if edge1 == edge2:
                    return True
        return False

    def get_transform(self, tile1, tile2):
        for n1, edge1 in enumerate(tile1.edges_cw):
            for n2, edge2 in enumerate(tile2.edges_cw):
                if edge1 == edge2:
                    return (n1, n2, True)
            for n2, edge2 in enumerate(tile2.edges_ccw):
                if edge1 == edge2:
                    return (n1, n2, False)
        return None

    def find_neighbours(self):
        self.corner_tiles = set()
        self.border_tiles = set()
        self.inner_tiles = set()
        for no1, tile1 in self.tiles.items():
            neighbours = set()
            for no2, tile2 in self.tiles.items():
                if no1 == no2:
                    continue
                if self.has_common_edge(tile1, tile2):
                    neighbours.add(no2)
            tile1.neighbours = neighbours
            assert len(neighbours) in [2, 3, 4]
            if len(neighbours) == 2:
                self.corner_tiles.add(no1)
            elif len(neighbours) == 3:
                self.border_tiles.add(no1)
            elif len(neighbours) == 4:
                self.inner_tiles.add(no1)

    def arrange_tile(self, tile, ref):
        (n, m, flipped) = self.get_transform(tile, ref)
        if flipped:
            tile.edges_cw, tile.edges_ccw = tile.edges_ccw, tile.edges_cw
            tile.edges_cw[1], tile.edges_cw[3] = tile.edges_cw[3], tile.edges_cw[1]
            tile.edges_ccw[1], tile.edges_ccw[3] = tile.edges_ccw[3], tile.edges_ccw[1]
            if n in [1, 3]:
                n = (n + 2) % 4
        rotation = (n - m - 2) % 4
        tile.edges_cw = tile.edges_cw[rotation:] + tile.edges_cw[:rotation]
        tile.edges_ccw = tile.edges_ccw[rotation:] + tile.edges_ccw[:rotation]
        tile.flipped = flipped
        tile.rotation = rotation
        if m == 0:  # Tile above reference
            assert tile.edges_ccw[2] == ref.edges_cw[0]
            tile.x = ref.x
            tile.y = ref.y - 1
        elif m == 1:  # Tile on right side of reference
            assert tile.edges_ccw[3] == ref.edges_cw[1]
            tile.x = ref.x + 1
            tile.y = ref.y
        elif m == 2:  # Tile below reference
            assert tile.edges_ccw[0] == ref.edges_cw[2]
            tile.x = ref.x
            tile.y = ref.y + 1
        else:  # Tile on left side of reference
            assert tile.edges_ccw[1] == ref.edges_cw[3]
            tile.x = ref.x - 1
            tile.y = ref.y
        if tile.flipped:
            tile.image = np.fliplr(tile.image)
        if tile.rotation != 0:
            tile.image = np.rot90(tile.image, tile.rotation)
        assert tile.edges_cw[0] == tuple(tile.image[0, :].tolist())

    def arrange_tiles(self):
        corners = self.corner_tiles.copy()
        borders = self.border_tiles.copy()
        start_no = corners.pop()
        border = [start_no]
        next_no = next(iter(self.tiles[start_no].neighbours))
        border.append(next_no)
        borders.remove(next_no)
        while len(corners) + len(borders) > 0:
            neighbours = self.tiles[next_no].neighbours
            if len(neighbours.intersection(borders)) == 1:
                next_no = next(iter(neighbours.intersection(borders)))
                borders.remove(next_no)
            elif len(neighbours.intersection(corners)) == 1:
                next_no = next(iter(neighbours.intersection(corners)))
                corners.remove(next_no)
            else:
                raise RuntimeError()
            border.append(next_no)
        prev_tile = self.tiles[border[0]]
        prev_tile.x = 0
        prev_tile.y = 0
        for next_no in border[1:]:
            next_tile = self.tiles[next_no]
            self.arrange_tile(next_tile, prev_tile)
            prev_tile = next_tile
        border_tiles = self.border_tiles.copy()
        inner_tiles = self.inner_tiles.copy()
        while len(inner_tiles) > 0:
            outer_tiles = {tile_no for tile_no in inner_tiles if border_tiles.intersection(
                self.tiles[tile_no].neighbours)}
            for tile_no in outer_tiles:
                ref_no = next(iter(self.tiles[tile_no].neighbours.intersection(border_tiles)))
                self.arrange_tile(self.tiles[tile_no], self.tiles[ref_no])
                inner_tiles.remove(tile_no)
            border_tiles = outer_tiles

    def reset_origin(self):
        xmin = min([tile.x for tile in self.tiles.values()])
        ymin = min([tile.y for tile in self.tiles.values()])
        for tile in self.tiles.values():
            tile.x -= xmin
            tile.y -= ymin
            if tile.x == 0 and tile.y == 0:
                self.reference = tile

    def compose_image(self):
        self.reset_origin()
        tile_size = self.reference.image.shape
        assert tile_size[0] == tile_size[1]
        tile_size = tile_size[0] - 2
        size = int((1 + (len(self.border_tiles) + len(self.corner_tiles)) / 4) * tile_size)
        self.image = np.zeros([size, size], dtype=int)
        for tile in self.tiles.values():
            x = tile.x * tile_size
            y = tile.y * tile_size
            self.image[y:(y+tile_size), x:(x+tile_size)] = tile.image[1:-1, 1:-1]

    def load_monster(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        monster = np.array([[int(x == '#') for x in line] for line in lines], dtype=int)
        return monster

    def find_monsters(self, monster):
        image_size = self.image.shape
        monster_size = monster.shape
        monster_sum = np.sum(monster)
        for flip in [False, True]:
            for rotation in [0, 1, 2, 3]:
                image = self.image
                if flip:
                    image = np.fliplr(image)
                if rotation != 0:
                    image = np.rot90(image, rotation)
                num_monsters = 0
                for x in range(image_size[1] - monster_size[1]):
                    for y in range(image_size[0] - monster_size[0]):
                        product = np.multiply(
                            image[y: (y + monster_size[0]),
                                  x: (x + monster_size[1])],
                            monster)
                        if np.sum(product) == monster_sum:
                            num_monsters += 1
                if num_monsters > 0:
                    return num_monsters
        return 0

    def part1(self):
        self.find_neighbours()
        corners = list(self.corner_tiles)
        assert len(corners) == 4
        return np.prod(corners)

    def part2(self, filename):
        self.arrange_tiles()
        self.compose_image()
        monster = self.load_monster(filename)
        num_monsters = self.find_monsters(monster)
        return np.sum(self.image) - num_monsters * np.sum(monster)


test = Puzzle('test.txt')
assert test.part1() == 20899048083289
assert test.part2('monster.txt') == 273

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2('monster.txt'))
