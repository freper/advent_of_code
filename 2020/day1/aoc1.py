file = open("input.txt", 'r')
lines = file.readlines()
data = [int(line) for line in lines]
N = len(data)

# Part 1
print("Part 1")
for i in range(0, N - 1):
    for j in range(i + 1, N):
        if (data[i] + data[j]) == 2020:
            print(data[i], data[j], data[i] * data[j])

# Part 2
print("Part 2")
for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if (data[i] + data[j] + data[k]) == 2020:
                print(data[i], data[j], data[k], data[i] * data[j] * data[k])
