import re

file = open("input.txt", 'r')
data = file.read()
lines = data.splitlines()

p = re.compile(r"(\d+) (.+) bags?\.?")

def parse_bag(s):
    if (p.fullmatch(s)):
        m = p.fullmatch(s)
        return (int(m.group(1)), m.group(2).replace(" ", "_"))
    else:
        return (0, "")

def contain_bag(rules, bag, color):
    colors = rules[bag]
    if colors == {""}:
        return False
    elif color in colors:
        return True
    else:
        return any([contain_bag(rules, c, color) for c in colors])
    
# Part 1
print("Part 1")
rules = dict()
for line in lines:
    bags = line.split(" bags contain ")
    color = bags[0].replace(" ", "_")
    content = [parse_bag(s) for s in bags[1].split(', ')]
    if content[0]:
        colors = {c[1] for c in content}
    else:
        colors = {}
    rules[color] = colors

color = "shiny_gold"
num_bags = 0
for bag in rules.keys():
    if contain_bag(rules, bag, color):
        num_bags += 1
print("Number of bags:", num_bags)


def accumulate_num_bags(rules, color, num):
    if color == "" or rules[color][0] == 0:
        return num
    else:
        return num + sum([c[0] * accumulate_num_bags(rules, c[1], 1) for c in rules[color]])

# Part 2
print("Part 2")
rules = dict()
for line in lines:
    bags = line.split(" bags contain ")
    color = bags[0].replace(" ", "_")
    content = [parse_bag(s) for s in bags[1].split(', ')]
    rules[color] = content

color = "shiny_gold"
num_bags = accumulate_num_bags(rules, "shiny_gold", 0)
print("Number of bags:", num_bags)