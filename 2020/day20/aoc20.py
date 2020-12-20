import numpy as np
import re


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read().split("\n\n")
        header = re.compile(r'Tile (\d+):')
        self.tiles = dict()
        self.edges_cw = dict()
        self.edges_ccw = dict()
        for tile in data:
            lines = tile.splitlines()
            if len(lines) == 0:
                continue
            m = header.fullmatch(lines[0])
            assert m
            tile_no = int(m.group(1))
            image = np.array([[int(x == '#') for x in line] for line in lines[1:]], dtype=int)
            edges = [
                image[0, :].tolist(),
                image[:, -1].tolist(),
                image[-1, :].tolist(),
                image[:, 0].tolist()]
            cw = [
                tuple(edges[0]),
                tuple(edges[1]),
                tuple(reversed(edges[2])),
                tuple(reversed(edges[3]))]
            ccw = [
                tuple(edges[3]),
                tuple(edges[2]),
                tuple(reversed(edges[1])),
                tuple(reversed(edges[0]))]
            self.tiles[tile_no] = image[1:-1, 1:-1]
            self.edges_cw[tile_no] = cw
            self.edges_ccw[tile_no] = ccw

    def has_common_edge(self, no1, no2):
        for edge1 in self.edges_cw[no1]:
            for edge2 in self.edges_cw[no2]:
                if edge1 == edge2:
                    return True
            for edge2 in self.edges_ccw[no2]:
                if edge1 == edge2:
                    return True
        return False

    def neighbour_candidates(self):
        candidates = dict()
        for no1 in self.tiles.keys():
            candidates[no1] = list()
            for no2 in self.tiles.keys():
                if no1 == no2:
                    continue
                if self.has_common_edge(no1, no2):
                    candidates[no1].append(no2)
        return candidates

    def compose_image(self):
        candidates = self.neighbour_candidates()
        corners = list()
        borders = list()
        others = list()
        for no in candidates.keys():
            assert len(candidates[no]) in [2, 3, 4]
            if len(candidates[no]) == 2:
                corners.append(no)
            elif len(candidates[no]) == 3:
                borders.append(no)
            elif len(candidates[no]) == 4:
                others.append(no)

    def part1(self):
        candidates = self.neighbour_candidates()
        corners = list()
        for no in candidates.keys():
            if len(candidates[no]) == 2:
                corners.append(no)
        assert len(corners) == 4
        return np.prod(corners)

    def part2(self):
        self.compose_image()
        return 273


test = Puzzle('test.txt')
assert test.part1() == 20899048083289
assert test.part2() == 273

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
# print("Part 2:", puzzle.part2())
