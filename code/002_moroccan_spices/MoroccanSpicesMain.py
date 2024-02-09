# The Moroccan Spices Box Set Puzzle by 101Computing.net - www.101computing.net/the-moroccan-spices-box-set-puzzle


def get_solution(usable_jars: list[int], used_jars: list[int], target_weight: int, remaining_jars: int):
    found_combinations = []
    for u in usable_jars:
        if remaining_jars <= 0:
            break

        combination = used_jars.copy()
        combination.append(u)
        sum_of_combination = sum(combination)

        if sum_of_combination == target_weight:
            return [combination]

        if sum_of_combination > target_weight:
            continue

        if sum_of_combination < target_weight:
            new_usable_jars = usable_jars.copy()
            new_usable_jars.remove(u)
            new_combinations = get_solution(new_usable_jars, combination, target_weight, remaining_jars-1)
            if len(new_combinations) > 0:
                found_combinations.extend(new_combinations)
    return found_combinations




jars = [150, 20, 20, 10, 80, 130, 110, 90, 100, 40]

numberOfJars = len(jars)
weight_target = 250
totalWeight = 0
for x in jars:
    totalWeight = totalWeight + x

print("Total Weight: " + str(totalWeight) + "g")
print("Number of Jars: " + str(numberOfJars))
print("")

# Complete this program using an algorithm to work out how to use all the values from the jars list to create three lists (box sets) with a total value of 250 per list.
# ...


solutions = get_solution(jars, [], weight_target, 3)

for i in range(len(solutions)):
    print(f"Box set {i}: {solutions[i]}")
