file = open("input.txt", 'r')
data = file.read()
lines = data.splitlines()

instructions = [(line[0], int(line[1:])) for line in lines]


def rotate_left(state, offset):
    (d, n, e) = state
    while offset > 0:
        if d == 'N':
            d = 'W'
        elif d == 'E':
            d = 'N'
        elif d == 'S':
            d = 'E'
        elif d == 'W':
            d = 'S'
        offset -= 90
    return (d, n, e)


def rotate_right(state, offset):
    (d, n, e) = state
    while offset > 0:
        if d == 'N':
            d = 'E'
        elif d == 'E':
            d = 'S'
        elif d == 'S':
            d = 'W'
        elif d == 'W':
            d = 'N'
        offset -= 90
    return (d, n, e)


def move_forward(state, offset):
    (d, n, e) = state
    if d == 'N':
        n += offset
    elif d == 'E':
        e += offset
    elif d == 'S':
        n -= offset
    elif d == 'W':
        e -= offset
    return (d, n, e)


def update_state(state, instruction):
    d = state[0]
    n = state[1]
    e = state[2]
    a = instruction[0]
    v = instruction[1]
    if a == 'F':
        (d, n, e) = move_forward(state, v)
    if a == 'L':
        (d, n, e) = rotate_left(state, v)
    elif a == 'R':
        (d, n, e) = rotate_right(state, v)
    elif a == 'N':
        n += v
    elif a == 'S':
        n -= v
    elif a == 'E':
        e += v
    elif a == 'W':
        e -= v
    return (d, n, e)


# Part 1
print("Part 1")
state = ('E', 0, 0)
for instruction in instructions:
    state = update_state(state, instruction)
print("Manhattan distance:", abs(state[1]) + abs(state[2]))


def rotate_waypoint_left(waypoint, angle):
    (n, e) = waypoint
    while angle > 0:
        (n, e) = (e, -n)
        angle -= 90
    return (n, e)


def rotate_waypoint_right(waypoint, angle):
    (n, e) = waypoint
    while angle > 0:
        (n, e) = (-e, n)
        angle -= 90
    return (n, e)


def update(position, waypoint, instruction):
    p_n = position[0]
    p_e = position[1]
    w_n = waypoint[0]
    w_e = waypoint[1]
    a = instruction[0]
    v = instruction[1]
    if a == 'F':
        p_n += v * w_n
        p_e += v * w_e
    if a == 'L':
        (w_n, w_e) = rotate_waypoint_left(waypoint, v)
    elif a == 'R':
        (w_n, w_e) = rotate_waypoint_right(waypoint, v)
    elif a == 'N':
        w_n += v
    elif a == 'S':
        w_n -= v
    elif a == 'E':
        w_e += v
    elif a == 'W':
        w_e -= v
    position = (p_n, p_e)
    waypoint = (w_n, w_e)
    return (position, waypoint)


# Part 2
print("Part 2")
position = (0, 0)
waypoint = (1, 10)
for instruction in instructions:
    position, waypoint = update(position, waypoint, instruction)
print("Manhattan distance:", abs(position[0]) + abs(position[1]))