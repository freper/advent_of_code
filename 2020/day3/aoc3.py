file = open("input.txt", 'r')
data = file.readlines()

N = len(data)
width = len(data[0]) - 1

# Part 1
print("Part 1")
num_trees = 0
x = 0
for y in range(N):
    i = x % width
    if data[y][i] == '#':
        num_trees += 1
    x += 3
print("Number of trees:", num_trees)

# Part 2
print("Part 2")

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
product = 1
for slope in slopes:
    num_trees = 0
    x = 0
    for y in range(0, N, slope[1]):
        i = x % width
        if data[y][i] == '#':
            num_trees += 1
        x += slope[0]
    print(slope, num_trees)
    product *= num_trees
print("Product:", product)

