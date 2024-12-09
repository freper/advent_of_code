def checksum(memory):
    checksum = 0
    for index, value in enumerate(memory):
        if value < 0:
            continue
        checksum += index * value
    return checksum


class Puzzle:
    def __init__(self, filename):
        self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        disk = file.read().rstrip("\n") + "0"
        data = [int(value) for value in disk]
        self.map = list(zip(data[0::2], data[1::2]))

        
    def part1(self):
        memory = []
        free_space = []
        memory_adress = 0
        for file_index, data in enumerate(self.map):
            for _ in range(data[0]):
                memory.append(file_index)
                memory_adress += 1
            for _ in range(data[1]):
                memory.append(-1)
                free_space.append(memory_adress)
                memory_adress += 1
        last_index = len(memory) - 1

        while free_space:
            free_index = free_space.pop(0)
            if free_index >= last_index:
                break
            memory[free_index], memory[last_index] = memory[last_index], memory[free_index]
            last_index -= 1
            while last_index > 0 and memory[last_index] < 0:
                last_index -= 1

        return checksum(memory)


    def part2(self):
        free_space = {}
        file_space = {}
        file_map = {}
        memory_adress = 0
        for file_index, data in enumerate(self.map):
            file_space[memory_adress] = (file_index, data[0])
            file_map[file_index] = memory_adress
            memory_adress += data[0]
            if data[1] > 0:
                free_space[memory_adress] = data[1]
                memory_adress += data[1]
        
        file_index = len(self.map) - 1
        while file_index > 0:
            memory_adress = file_map[file_index]
            file_size = file_space[memory_adress][1]
            for free_adress, free_size in sorted(free_space.copy().items()):
                if free_size >= file_size:
                    file_adress = file_map.pop(file_index)
                    file_map[file_index] = free_adress
                    file_space[free_adress] = (file_index, file_size)
                    del file_space[file_adress]
                    del free_space[free_adress]
                    if free_size > file_size:
                        free_space[free_adress + file_size] = free_size - file_size
                    break
            file_index -= 1
        
        def checksum(file_space):
            checksum = 0
            for file_adress, (file_index, file_size) in file_space.items():
                for adress in range(file_adress, file_adress + file_size):
                    checksum += file_index * adress
            return checksum

        return checksum(file_space)

test = Puzzle('test.txt')
print("Part 1:", test.part1())
print("Part 2:", test.part2())
# assert test.part1() == 1928
# assert test.part2() == 2858

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
