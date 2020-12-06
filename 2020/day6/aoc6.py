file = open("input.txt", 'r')
data = file.read()

groups = data.split('\n\n')

# Part 1
print("Part 1")
num_answers = 0
for group in groups:
    num_answers += len(set(group) - {'\n'})
print("Number of answers:", num_answers)

# Part 2
print("Part 2")
num_answers = 0
for group in groups:
    combined = set(group) - {'\n'}
    persons = group.split('\n')
    for person in persons:
        if len(person) > 0:
            combined = combined.intersection(set(person))
    num_answers += len(combined)
print("Number of answers:", num_answers)