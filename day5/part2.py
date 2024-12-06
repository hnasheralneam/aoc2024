import math

sum = 0
rules = []
updates = []
incorrect_updates = []

def get_middle_number(arr):
    index = math.floor(len(arr) / 2)
    return arr[index]

def parse_rules():
    global rules
    for i in range(0, len(rules)):
        rule_parts = rules[i].split("|")
        rules[i] = list(map(int, rule_parts))

def parse_updates():
    global updates
    for i in range(0, len(updates)):
        update_string_array = updates[i].split(",")
        updates[i] = list(map(int, update_string_array))

def rule_followed(update):
    for rule in rules:
        if (rule[0] in update) and (rule[1] in update):
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

def fix_update(update):
    for rule in rules:
        if (rule[0] in update) and (rule[1] in update):
            if update.index(rule[0]) > update.index(rule[1]):
                update[update.index(rule[0])] = rule[1]
                update[update.index(rule[1])] = rule[0]
    return update

with open("input.txt", "r") as f:
    for line in f:
        if "|" in line:
            rules.append(line.strip())
        elif "," in line:
            updates.append(line.strip())

parse_rules()
parse_updates()

for update in updates:
    if not rule_followed(update):
       incorrect_updates.append(update)

for update in incorrect_updates:
    current_update = update
    while (not rule_followed(current_update)):
        current_update = fix_update(current_update)
    sum += get_middle_number(current_update)

print(sum)