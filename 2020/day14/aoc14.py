from copy import deepcopy
import re

pmask = re.compile(r"^mask = ([0,1,X]{36})$")
pmem = re.compile(r"^mem\[(\d+)\] = (\d+)$")


class Puzzle:
  def __init__(self, filename):
    self.read_input(filename)

  def read_input(self, filename):
    file = open(filename, 'r')
    data = file.read()
    self.input = data.splitlines()

  def update_mask(self, mask):
    assert len(mask) == 36
    self.bitmask = 0
    self.mask = 0
    self.floatbits = []
    self.floatmask = 0
    for offset, char in enumerate(mask):
      if char != 'X':
        bitmask = 2**(35 - offset)
        value = int(char) * bitmask
        self.bitmask = self.bitmask | bitmask
        self.mask = self.mask | value
      else:
        self.floatbits.append(35 - offset)
        self.floatmask |= 2**(35 - offset)

  def update_memory(self, address, value):
    if address not in self.memory.keys():
      self.memory[address] = 0
    self.memory[address] = (value & ~self.bitmask) | self.mask

  def update_memory2(self, address, value):
    if self.floatbits:
      addresses = []
      bit = self.floatbits[0]
      addresses.append(((address & ~self.floatmask) | self.mask) & ~(2**bit))
      addresses.append(((address & ~self.floatmask) | self.mask) | 2**bit)
    for bit in self.floatbits[1:]:
      prev_addresses = deepcopy(addresses)
      for address in prev_addresses:
        addresses.append(address | 2**bit)

    for address in addresses:
      self.memory[address] = value

  def part1(self):
    self.memory = {}
    for line in self.input:
      if pmask.fullmatch(line):
        m = pmask.fullmatch(line)
        self.update_mask(m.group(1))
      elif pmem.fullmatch(line):
        m = pmem.fullmatch(line)
        address = int(m.group(1))
        value = int(m.group(2))
        self.update_memory(address, value)
    return sum(self.memory.values())

  def part2(self):
    self.memory = {}
    for line in self.input:
      if pmask.fullmatch(line):
        m = pmask.fullmatch(line)
        self.update_mask(m.group(1))
      elif pmem.fullmatch(line):
        m = pmem.fullmatch(line)
        address = int(m.group(1))
        value = int(m.group(2))
        self.update_memory2(address, value)
    return sum(self.memory.values())


test1 = Puzzle('test1.txt')
assert test1.part1() == 165
test2 = Puzzle('test2.txt')
assert test2.part2() == 208

puzzle = Puzzle('input.txt')
print(puzzle.part1())
print(puzzle.part2())
