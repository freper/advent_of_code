class Puzzle:
    def __init__(self, filename=None):
        if filename:
            self.read_input(filename)

    def read_input(self, filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        self.list_allergens = list()
        self.list_ingredients = list()
        self.all_allergens = set()
        self.all_ingredients = set()
        self.foods = dict()
        for line in lines:
            data = line.split(" (contains ")
            ingredients = set(data[0].split(" "))
            allergens = set(data[1][:-1].split(", "))
            self.list_allergens.append(allergens)
            self.list_ingredients.append(ingredients)
            self.all_allergens |= allergens.copy()
            self.all_ingredients |= ingredients.copy()
            for x in allergens:
                if x in self.foods.keys():
                    self.foods[x] &= ingredients.copy()
                else:
                    self.foods[x] = ingredients.copy()

    def part1(self):
        ingredients_with_no_allergens = self.all_ingredients.copy()
        for ingredients in self.foods.values():
            ingredients_with_no_allergens -= ingredients
        num_occurences = 0
        for ingredients in self.list_ingredients:
            num_occurences += len(ingredients_with_no_allergens.intersection(ingredients))
        return num_occurences

    def part2(self):
        remaining_allergens = self.all_allergens.copy()
        while len(remaining_allergens) > 0:
            allergens = {x for x in remaining_allergens if len(self.foods[x]) == 1}
            ingredients = set()
            for x in allergens:
                ingredients |= self.foods[x]
            remaining_allergens -= allergens
            for x in remaining_allergens:
                self.foods[x] -= ingredients
        allergens = list(self.foods.keys())
        allergens.sort()
        dangerous_ingredients = [next(iter(self.foods[x])) for x in allergens]
        return ",".join(dangerous_ingredients)


test = Puzzle("test.txt")
assert test.part1() == 5
assert test.part2() == "mxmxvkd,sqjhc,fvjkl"

puzzle = Puzzle('input.txt')
print("Part 1:", puzzle.part1())
print("Part 2:", puzzle.part2())
