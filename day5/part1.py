import math

sum = 0
rules = []
updates = []
correct_updates = []

def get_middle_number(arr):
    arr_string_array = arr.split(",")
    index = math.floor(len(arr_string_array) / 2)
    return int(arr_string_array[index])

def rule_followed(update):
    for rule in rules:
        rule_numbers = rule.split("|")
        number_first = int(rule_numbers[0])
        number_second = int(rule_numbers[1])
        update_string_array = update.split(",")
        update_numbers = list(map(int, update_string_array))

        if (number_first in update_numbers) and (number_second in update_numbers):
            if update_numbers.index(number_first) > update_numbers.index(number_second):
                return False
    return True


with open("input.txt", "r") as f:
    for line in f:
        if "|" in line:
            rules.append(line.strip())
        elif "," in line:
            updates.append(line.strip())

for update in updates:
    if rule_followed(update):
        correct_updates.append(update)

for update in correct_updates:
    sum += get_middle_number(update)

print(sum)