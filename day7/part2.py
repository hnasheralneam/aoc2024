sum = 0

def meld_numbers(one, two):
    return int(str(one) + str(two))

def recursive(number, remaining, results):
    if len(remaining) > 0:
        recursive(number + remaining[0], remaining[1:], results)
        recursive(number * remaining[0], remaining[1:], results)
        recursive(meld_numbers(number, remaining[0]), remaining[1:], results)
    else:
        results.append(number)
        return

def parse_line(line):
    global sum

    splitted = line.split(": ")
    answer = int(splitted[0])
    numbers = list(map(int, splitted[1].split(" ")))
    
    results = []
    recursive(numbers[0], numbers[1:], results)
    if answer in results:
        sum += answer

with open("day7/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        parse_line(line.replace("\n", ""))


print(sum)