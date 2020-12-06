import re

file = open("input.txt", 'r')
data = file.read()
lines = data.splitlines()

full_lines = []
entry = ""
for line in lines:
    if len(line) == 0 and entry != "":
        full_lines.append(entry)
        entry = ""
    else:
        if entry == "":
            entry = line
        else:
            entry += " " + line

if entry != "":
    full_lines.append(entry)

# Part 1
print("Part 1")

byr = re.compile('byr:(\S+)')
ecl = re.compile('ecl:(\S+)')
eyr = re.compile('eyr:(\S+)')
hcl = re.compile('hcl:(\S+)')
hgt = re.compile('hgt:(\S+)')
iyr = re.compile('iyr:(\S+)')
pid = re.compile('pid:(\S+)')

num_valid_passports = 0
num_invalid_passports = 0
for line in full_lines:
    if byr.search(line) and ecl.search(line) and eyr.search(line) and hcl.search(line) and \
       hgt.search(line) and iyr.search(line) and pid.search(line):
        num_valid_passports += 1
    else:
        num_invalid_passports += 1
print("Number of valid passorts:", num_valid_passports)
print("Number of invalid passorts:", num_invalid_passports)

# Part 2
print("Part 2")

hcl = re.compile('#[0-9a-f]{6}')
pid = re.compile('\d{9}')

cm = re.compile('(\d+)cm')
inch = re.compile('(\d+)in')

required_keys = {"byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"}
valid_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

num_valid_passports = 0
num_invalid_passports = 0
for line in full_lines:
    passport = dict(map(lambda x: x.split(":"), line.split()))
    if required_keys.issubset(passport.keys()):
        valid = True

        birth = int(passport["byr"])
        if birth < 1920 or birth > 2002:
            valid = False
        
        issue = int(passport["iyr"])
        if issue < 2010 or issue > 2020:
            valid = False

        expiration = int(passport["eyr"])
        if expiration < 2020 or expiration > 2030:
            valid = False

        height = passport["hgt"]
        if cm.fullmatch(height):
            value = int(cm.fullmatch(height).group(1))
            if value < 150 or value > 193:
                valid = False
        elif inch.fullmatch(height):
            value = int(inch.fullmatch(height).group(1))
            if value < 59 or value > 76:
                valid = False
        else:
            valid = False

        if not hcl.fullmatch(passport["hcl"]):
            valid = False

        eye = passport["ecl"]
        if eye not in valid_eye_colors:
            valid = False

        if not pid.fullmatch(passport["pid"]):
            valid = False

        if valid:
            num_valid_passports += 1
        else:
            num_invalid_passports += 1
    else:
        num_invalid_passports += 1
print("Number of valid passorts:", num_valid_passports)
print("Number of invalid passorts:", num_invalid_passports)
