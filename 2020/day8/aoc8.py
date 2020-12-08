file = open("input.txt", 'r')
data = file.read()
lines = data.splitlines()

def parse_op(line):
    x = line.split()
    return (x[0], int(x[1]))


ops = [parse_op(line) for line in lines]
num_ops = len(ops)

# Part 1
print("Part 1")
visited = [False] * num_ops
acc = 0
i = 0
while visited[i] == False:
    visited[i] = True
    op = ops[i]
    if op[0] == "acc":
        acc += op[1]
        i += 1
    elif op[0] == "jmp":
        i += op[1]
    else:
        i += 1
print("Value:", acc)


def check_infinite_loop(ops):
    num_ops = len(ops)
    visited = [False] * num_ops
    acc = 0
    i = 0
    while i < num_ops and visited[i] == False:
        visited[i] = True
        op = ops[i]
        if op[0] == "acc":
            acc += op[1]
            i += 1
        elif op[0] == "jmp":
            i += op[1]
        else:
            i += 1
    return (i < num_ops, acc)
    

def switch_op(op):
    if op[0] == "jmp":
        op = ("nop", op[1])
    elif op[0] == "nop":
        op = ("jmp", op[1])
    return op


# Part 2
j = num_ops - 1
print("Part 2")
for i in range(num_ops):
    if visited[i] == False:
        continue
    ops[i] = switch_op(ops[i])
    (infinite, acc) = check_infinite_loop(ops)
    if infinite == False:
        break
    ops[i] = switch_op(ops[i])
print("Value:", acc)