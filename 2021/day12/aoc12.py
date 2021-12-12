class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        lines = data.splitlines()
        paths = dict()
        for line in lines:
            caves = line.split('-')
            if caves[0] in paths.keys():
                paths[caves[0]].add(caves[1])
            else:
                paths[caves[0]] = {caves[1]}
            if caves[1] in paths.keys():
                paths[caves[1]].add(caves[0])
            else:
                paths[caves[1]] = {caves[0]}
        self.valid_paths = paths

    @staticmethod
    def visited_small_caves(path):
        caves = set()
        for cave in path:
            if cave.islower():
                caves.add(cave)
        return caves

    @staticmethod
    def has_visited_small_cave_twice(path):
        caves = set()
        for cave in path:
            if cave.islower():
                if cave in caves:
                    return True
                caves.add(cave)
        return False

    def extend_path(self, path, allow_visit_small_cave_twice=False):
        last_cave = path[-1]
        small_caves = self.visited_small_caves(path)
        visited_small_cave_twice = self.has_visited_small_cave_twice(path)
        extended_paths = set()
        for cave in self.valid_paths[last_cave]:
            if cave == "start":
                continue
            if cave in small_caves:
                if allow_visit_small_cave_twice:
                    if visited_small_cave_twice:
                        continue
                else:
                    continue
            extended_paths.add(path + (cave,))
        return extended_paths

    def find_paths(self, allow_visit_small_cave_twice=False):
        open_paths = set()
        closed_paths = set()
        for cave in self.valid_paths["start"]:
            open_paths.add(("start", cave))
        while len(open_paths) > 0:
            new_open_paths = set()
            for path in open_paths:
                extended_paths = self.extend_path(path, allow_visit_small_cave_twice)
                for extended_path in extended_paths:
                    if extended_path[-1] == "end":
                        closed_paths.add(extended_path)
                    else:
                        new_open_paths.add(extended_path)
            open_paths = new_open_paths
        return closed_paths

    def part1(self):
        paths = self.find_paths()
        return len(paths)

    def part2(self):
        paths = self.find_paths(True)
        return len(paths)


test1 = Puzzle('test1.txt')
assert test1.part1() == 10
assert test1.part2() == 36

test2 = Puzzle('test2.txt')
assert test2.part1() == 19
assert test2.part2() == 103

test3 = Puzzle('test3.txt')
assert test3.part1() == 226
assert test3.part2() == 3509

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
