from copy import deepcopy

file = open("input.txt", 'r')
data = file.read()
lines = data.splitlines()

def split_line(line):
    return [char for char in line]

original_seats = [split_line(line) for line in lines]
num_rows = len(original_seats)
num_cols = len(original_seats[0])

def update_seat(seats, row, col):
    if seats[row][col] == ".":
        return seats[row][col]
    
    num_occupied = 0
    for row_offset in [-1, 0, 1]:
        r = row + row_offset
        if r < 0 or r >= num_rows:
            continue
        for col_offset in [-1, 0, 1]:
            if row_offset == 0 and col_offset == 0:
                continue
            c = col + col_offset
            if c < 0 or c >= num_cols:
                continue
            if seats[r][c] == '#':
                num_occupied += 1

    if seats[row][col] == "#" and num_occupied >= 4:
        return "L"
    elif seats[row][col] == "L" and num_occupied == 0:
        return "#"
    else:
        return seats[row][col]

def num_occupied_seats(seats):
    num_occupied = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if seats[row][col] == "#":
                num_occupied += 1
    return num_occupied


# Part 1
print("Part 1")
seats = deepcopy(original_seats)
num_switches = -1
while num_switches != 0:
    num_switches = 0
    updated_seats = deepcopy(seats)
    for row in range(num_rows):
        for col in range(num_cols):
            old = seats[row][col]
            new = update_seat(seats, row, col)
            updated_seats[row][col] = new
            if new != old:
                num_switches += 1
    seats = updated_seats
print("Number of occupied seats:", num_occupied_seats(seats))


def update_seat2(seats, row, col):
    if seats[row][col] == ".":
        return seats[row][col]
    
    num_occupied = 0
    for offset in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1 , 1), (1, 0), (1, -1), (0, -1)]:
        r = row
        c = col
        while True:
            r += offset[0]
            c += offset[1]
            if r < 0 or r >= num_rows:
                break
            if c < 0 or c >= num_cols:
                break
            if seats[r][c] == "L":
                break
            if seats[r][c] == "#":
                num_occupied += 1
                break

    if seats[row][col] == "#" and num_occupied >= 5:
        return "L"
    elif seats[row][col] == "L" and num_occupied == 0:
        return "#"
    else:
        return seats[row][col]

# Part 2
print("Part 2")
seats = deepcopy(original_seats)
num_switches = -1
while num_switches != 0:
    num_switches = 0
    updated_seats = deepcopy(seats)
    for row in range(num_rows):
        for col in range(num_cols):
            old = seats[row][col]
            new = update_seat2(seats, row, col)
            updated_seats[row][col] = new
            if new != old:
                num_switches += 1
    seats = updated_seats
print("Number of occupied seats:", num_occupied_seats(seats))
