file = open("input.txt", 'r')
data = file.read()
lines = data.splitlines()

numbers = [int(line) for line in lines]

def valid_numbers(numbers, index):
    valid = []
    for i in range(index - 25, index - 1):
        for j in range(i + 1, index):
            valid.append(numbers[i] + numbers[j])
    return valid

# Part 1
print("Part 1")
for index in range(25, len(numbers) + 1):
    if not numbers[index] in valid_numbers(numbers, index):
        break
print("Value:", numbers[index])

# Part 2
print("Part 2")
target = numbers[index]
for start_index in range(25, len(numbers)):
    xmas_sum = numbers[start_index]
    xmas_val = [numbers[start_index]]
    for index in range(start_index + 1, len(numbers) + 1):
        xmas_sum += numbers[index]
        xmas_val.append(numbers[index])
        if xmas_sum >= target:
            break
    if xmas_sum == target:
        break
assert(xmas_sum == target)
print("Value:", min(xmas_val) + max(xmas_val))