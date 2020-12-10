file = open("input.txt", 'r')
data = file.read()
lines = data.splitlines()

adapters = [int(line) for line in lines]
adapters.sort()

# Part 1
print("Part 1")
n1 = 0
n3 = 0
prev = 0
for i in range(0, len(adapters)):
    diff = adapters[i] - prev
    if diff == 1:
        n1 += 1
    elif diff == 3:
        n3 += 1
    else:
        print("Invalid jolt difference!")
    prev = adapters[i]
print("Value:", n1 * (n3 + 1))


# Part 2
print("Part 2")
first = 0
last = adapters[-1] + 3
jolts = adapters.copy()
jolts.insert(first, 0)
jolts.append(last)

connections = []
for i in range(0, len(jolts)):
    inputs = []
    outputs = []
    for offset in [1, 2, 3]:
        j = i - offset
        if j >= 0 and jolts[i] - jolts[j] <= 3:
            inputs.append(j)
        j = i + offset
        if j < len(jolts) and jolts[j] - jolts[i] <= 3:
            outputs.append(j)
    connections.append((inputs,outputs))

def collect_output(outputs):
    num = {}
    for o in outputs:
        if o[0] in num.keys():
            num[o[0]] += o[1]
        else:
            num[o[0]] = o[1]
    return [(key, val) for key, val in num.items()]


outputs = [(o, 1) for o in connections[0][1]]
finished = False
while not finished:
    inputs, outputs = outputs, []
    finished = True
    for i in inputs:
        ocs = connections[i[0]][1]
        if len(ocs) != 0:
            outputs += [(o,i[1]) for o in ocs]
            finished = False
        else:
            outputs += [i]
    outputs = collect_output(outputs)
assert(len(outputs) == 1)
print("Number of ways:", outputs[0][1])
