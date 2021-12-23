from copy import deepcopy


class Interval:
    def __init__(self, start, stop):
        self.min = start
        self.max = stop

    def intersection(self, interval):
        if self.xmin > interval.xmax or self.xmax < interval.xmin:
            return None
        return Interval(max(self.xmin, interval.xmin), min(self.xmax, interval.xmax))

    def size(self):
        return self.xmax - self.xmin + 1


class Cube:
    def __init__(self, intervals):
        self.xmin = intervals["xmin"]
        self.xmax = intervals["xmax"]
        self.ymin = intervals["ymin"]
        self.ymax = intervals["ymax"]
        self.zmin = intervals["zmin"]
        self.zmax = intervals["zmax"]

    def intersection(self, cube):
        if self.xmin > cube.xmax or self.xmax < cube.xmin:
            return None
        if self.ymin > cube.ymax or self.ymax < cube.ymin:
            return None
        if self.zmin > cube.zmax or self.zmax < cube.zmin:
            return None
        xmin = max(self.xmin, cube.xmin)
        xmax = min(self.xmax, cube.xmax)
        ymin = max(self.ymin, cube.ymin)
        ymax = min(self.ymax, cube.ymax)
        zmin = max(self.zmin, cube.zmin)
        zmax = min(self.zmax, cube.zmax)
        return Cube({"xmin": xmin, "xmax": xmax, "ymin": ymin, "ymax": ymax, "zmin": zmin, "zmax": zmax})

    def union(self, cube):
        output = [self]
        common = self.intersection(cube)
        if not common:
            return [self, cube]
        if cube.xmin < common.xmin:
            c1 = deepcopy(cube)
            c1.xmax = common.xmin
            cube.xmin = common.xmin
            output.append(c1)
        if cube.xmax > common.xmax:
            c2 = deepcopy(cube)
            c2.xmin = common.xmax
            cube.xmax = common.xmax
            output.append(c2)
        if cube.ymin < common.ymin:
            c3 = deepcopy(cube)
            c3.ymax = common.ymin
            cube.ymin = common.ymin
            output.append(c3)
        if cube.ymax > common.ymax:
            c4 = deepcopy(cube)
            c4.ymin = common.ymax
            cube.ymax = common.ymax
            output.append(c4)
        if cube.zmin < common.zmin:
            c5 = deepcopy(cube)
            c5.zmax = common.zmin
            cube.zmin = common.zmin
            output.append(c5)
        if cube.zmax > common.zmax:
            c6 = deepcopy(cube)
            c6.zmin = common.zmax
            cube.zmax = common.zmax
            output.append(c6)
        return output

    def size(self):
        nx = self.xmax - self.xmin + 1
        ny = self.ymax - self.ymin + 1
        nz = self.zmax - self.zmin + 1
        return nx * ny * nz


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        lines = data.splitlines()

        def parse_line(line):
            data = line.split(' ')
            cube = data[1].split(',')
            x = cube[0][2:].split('..')
            y = cube[1][2:].split('..')
            z = cube[2][2:].split('..')
            cuboid = dict()
            cuboid["xmin"] = int(x[0])
            cuboid["xmax"] = int(x[1])
            cuboid["ymin"] = int(y[0])
            cuboid["ymax"] = int(y[1])
            cuboid["zmin"] = int(z[0])
            cuboid["zmax"] = int(z[1])
            return (data[0], cuboid)

        self.reboot_steps = [parse_line(line) for line in lines]

    def part1(self):
        active_cubes = set()
        for step in self.reboot_steps:
            cubes = set()
            cuboid = step[1]
            xmin = cuboid["xmin"]
            xmax = cuboid["xmax"]
            ymin = cuboid["ymin"]
            ymax = cuboid["ymax"]
            zmin = cuboid["zmin"]
            zmax = cuboid["zmax"]
            if xmax < -50 or xmin > 50:
                continue
            if ymax < -50 or ymin > 50:
                continue
            if zmax < -50 or zmin > 50:
                continue
            xmin = max(xmin, -50)
            xmax = min(xmax, 50)
            ymin = max(ymin, -50)
            ymax = min(ymax, 50)
            zmin = max(zmin, -50)
            zmax = min(zmax, 50)
            for x in range(xmin, xmax + 1):
                for y in range(ymin, ymax + 1):
                    for z in range(zmin, zmax + 1):
                        cubes.add((x, y, z))
            if step[0] == "on":
                if active_cubes:
                    active_cubes.update(cubes)
                else:
                    active_cubes = cubes
            else:
                active_cubes -= cubes
        return len(active_cubes)

    def part2(self):
        activated_cubes = list()
        deactivated_cubes = list()
        for step in self.reboot_steps:
            print("Step")
            cube = Cube(step[1])
            if len(activated_cubes) == 0 and step[0] == "on":
                activated_cubes.append(cube)
            for activated_cube in activated_cubes:
                common = activated_cube.intersection(cube)
                if common:
                    print(common)
        return 2


test1 = Puzzle('test1.txt')
assert test1.part1() == 39

test2 = Puzzle('test2.txt')
assert test2.part1() == 590784

test3 = Puzzle('test3.txt')
assert test3.part1() == 474140
# assert test3.part2() == 2758514936282235
print("Part 2:", test3.part2())

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
# print("Part 2:", puzzle.part2())
