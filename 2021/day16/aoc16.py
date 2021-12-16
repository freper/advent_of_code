import math

hexmap = {
    "0": [0, 0, 0, 0],
    "1": [0, 0, 0, 1],
    "2": [0, 0, 1, 0],
    "3": [0, 0, 1, 1],
    "4": [0, 1, 0, 0],
    "5": [0, 1, 0, 1],
    "6": [0, 1, 1, 0],
    "7": [0, 1, 1, 1],
    "8": [1, 0, 0, 0],
    "9": [1, 0, 0, 1],
    "A": [1, 0, 1, 0],
    "B": [1, 0, 1, 1],
    "C": [1, 1, 0, 0],
    "D": [1, 1, 0, 1],
    "E": [1, 1, 1, 0],
    "F": [1, 1, 1, 1]
}


class Puzzle:
    def __init__(self, filename=None):
        if filename:
            self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        data = file.read()
        self.input = data.splitlines()[0]

    @staticmethod
    def hex_to_bits(message):
        bits = []
        for num in message:
            bits += hexmap[num]
        return bits

    def parse_packet(self, bits, offset, version_sum):
        version = int("".join([str(b) for b in bits[offset:(offset+3)]]), 2)
        version_sum += version
        offset += 3
        typeid = int("".join([str(b) for b in bits[offset:(offset+3)]]), 2)
        offset += 3
        if typeid == 4:  # literal type
            literal = ""
            while bits[offset] == 1:
                literal += "".join([str(b) for b in bits[(offset + 1):(offset + 5)]])
                offset += 5
            literal += "".join([str(b) for b in bits[(offset + 1):(offset+5)]])
            offset += 5
            value = int(literal, 2)
        else:  # operator
            length_type_id = bits[offset]
            offset += 1
            values = list()
            if length_type_id == 0:
                total_length = int("".join([str(b) for b in bits[offset:(offset+15)]]), 2)
                offset += 15
                end_offset = offset + total_length
                while offset < end_offset:
                    offset, version_sum, value = self.parse_packet(bits, offset, version_sum)
                    values.append(value)
                assert offset == end_offset
            else:
                num_sub_packets = int("".join([str(b) for b in bits[offset:(offset+11)]]), 2)
                offset += 11
                for _ in range(num_sub_packets):
                    offset, version_sum, value = self.parse_packet(bits, offset, version_sum)
                    values.append(value)
            if typeid == 0:  # sum
                value = sum(values)
            elif typeid == 1:  # product
                value = math.prod(values)
            elif typeid == 2:  # minimum
                value = min(values)
            elif typeid == 3:  # maximum
                value = max(values)
            elif typeid == 5:  # greater than
                assert len(values) == 2
                value = 1 if values[0] > values[1] else 0
            elif typeid == 6:  # less than
                assert len(values) == 2
                value = 1 if values[0] < values[1] else 0
            elif typeid == 7:  # equal
                assert len(values) == 2
                value = 1 if values[0] == values[1] else 0
            else:
                raise ValueError("Invalid type ID.")
        return offset, version_sum, value

    def get_packet_version_sum(self, message):
        bits = self.hex_to_bits(message)
<<<<<<< HEAD
        offset = 0
        version_sum = 0
        _, version_sum, _ = self.parse_packet(bits, offset, version_sum)
=======
        version_sum = self.parse_packet(bits, 0, 0)[1]
>>>>>>> Solution for 2021 day 16
        return version_sum

    def get_packet_value(self, message):
        bits = self.hex_to_bits(message)
<<<<<<< HEAD
        offset = 0
        version_sum = 0
        _, _, value = self.parse_packet(bits, offset, version_sum)
=======
        value = self.parse_packet(bits, 0, 0)[2]
>>>>>>> Solution for 2021 day 16
        return value

    def part1(self):
        return self.get_packet_version_sum(self.input)

    def part2(self):
        return self.get_packet_value(self.input)


test = Puzzle()
assert test.get_packet_version_sum("8A004A801A8002F478") == 16
assert test.get_packet_version_sum("620080001611562C8802118E34") == 12
assert test.get_packet_version_sum("C0015000016115A2E0802F182340") == 23
assert test.get_packet_version_sum("A0016C880162017C3686B18A3D4780") == 31
assert test.get_packet_value("C200B40A82") == 3
assert test.get_packet_value("04005AC33890") == 54
assert test.get_packet_value("880086C3E88112") == 7
assert test.get_packet_value("CE00C43D881120") == 9
assert test.get_packet_value("D8005AC2A8F0") == 1
assert test.get_packet_value("F600BC2D8F") == 0
assert test.get_packet_value("9C005AC2F8F0") == 0
assert test.get_packet_value("9C0141080250320F1802104A08") == 1

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
