class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        path = None
        dir_sizes = dict()
        def update_path(path, dir):
            if dir.startswith("/"):
                return (dir,)
            elif dir.startswith(".."):
                assert len(dir) == 2
                return path[:-1]
            return path + (dir + "/",)
        def update_size(path, filesize):
            for i in range(0, len(path)):
                sub_dir = path[:(i+1)]
                if sub_dir in dir_sizes.keys():
                    dir_sizes[sub_dir] += filesize
                else:
                    dir_sizes[sub_dir] = filesize
        for line in lines:
            if line.startswith("$ cd "):
                path = update_path(path, line[5:])
                ls = False
                continue
            if line == "$ ls":
                ls = True
                continue
            if ls:
                if line.startswith("dir"):
                    continue
                data = line.split()
                assert len(data) == 2
                filesize = int(data[0])
                update_size(path, filesize)
        self.dir_sizes = dir_sizes

    def part1(self):
        total_size = 0
        for size in self.dir_sizes.values():
            if size <= 100000:
                total_size += size
        return total_size

    def part2(self):
        used_size = max(self.dir_sizes.values())
        free_size = 70000000 - used_size
        required_size = 30000000
        target_size = required_size - free_size
        candidates = [size for size in self.dir_sizes.values() if size >= target_size]
        return min(candidates)


test = Puzzle('test.txt')
assert test.part1() == 95437
assert test.part2() == 24933642

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
