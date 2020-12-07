import re

file = open("input.txt", 'r') 
lines = file.readlines()

p = re.compile(r'(\d+)-(\d+) ([a-z]): (\w+)')

# Part 1
print("Part 1")
num_valid_passords = 0
num_invalid_passords = 0
for line in lines:
    m = p.match(line)
    if m:
        lower_limit = int(m.group(1))
        upper_limit = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        num_letter = password.count(letter)
        if num_letter < lower_limit or num_letter > upper_limit:
            num_invalid_passords += 1
        else: 
            num_valid_passords += 1
    else:
        print(line)
print('Number of valid passwords:', num_valid_passords)
print('Number of invalid passwords:', num_invalid_passords)

# Part 2
print("Part 2")
num_valid_passords = 0
num_invalid_passords = 0
for line in lines:
    m = p.match(line)
    if m:
        first = int(m.group(1)) - 1
        second = int(m.group(2)) - 1
        letter = m.group(3)
        password = m.group(4)
        if (password[first] == letter and password[second] == letter) or \
           (password[first] != letter and password[second] != letter):
            num_invalid_passords += 1
        else: 
            num_valid_passords += 1
    else:
        print(line)
print('Number of valid passwords:', num_valid_passords)
print('Number of invalid passwords:', num_invalid_passords)
