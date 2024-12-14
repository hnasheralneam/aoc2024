import re

answer = 0
mul_strings = []
enabled = []
line = ""

def parse_mul_call(mul_call_string):
    global answer

    numbers_string = mul_call_string.replace("mul(", "").replace(")", "")
    numbers_string_array = numbers_string.split(",")
    answer += int(numbers_string_array[0]) * int(numbers_string_array[1])

def parse_mul_strings(line):
    mul_strings = re.findall(r"mul\([0123456789]*,[0123456789]*\)", line)
    for mul_string in mul_strings:
        parse_mul_call(mul_string)

def parse(line):
    while line.find("do()"):
        splitted = line.split("do()", 1)
        enabled.append(splitted[0])
        dont_splitted = splitted[0].split("don't()")
        if len(dont_splitted) > 1:
            line = dont_splitted[1]
        else:
            line = ""
    print("done")
    # parts = re.split(r"do\(\)", line)
    # for i in range(0, len(parts)):
    #     if i % 2 == 0:
    #         enabled.append(parts[i])


f = open("day3/input.txt", "r")
line = line.join(f)
parse(line)

for section in enabled:
    parse_mul_strings(section)

print(enabled)
print(answer)