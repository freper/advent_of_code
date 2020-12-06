file = open("input.txt", 'r')
lines = file.readlines()

def id(line):
    row = int(line[0:7].replace("F", "0").replace("B", "1"), 2)
    col = int(line[7:10].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col

ids = [id(line) for line in lines]

# Part 1
print("Part 1")
print(max(ids))

# Part 2
print("Part 2")
ids.sort()
for i in range(len(ids) - 1):
    if ids[i+1] > ids[i] + 1:
        print(ids[i] + 1)
