import re

answer = 0

def parse_mul_call(mul_call_string):
    global answer

    numbers_string = mul_call_string.replace("mul(", "").replace(")", "")
    numbers_string_array = numbers_string.split(",")
    answer += int(numbers_string_array[0]) * int(numbers_string_array[1])

def parse_mul_strings(line):
    mul_strings = re.findall("mul\([0123456789]*,[0123456789]*\)", line)
    for mul_string in mul_strings:
        parse_mul_call(mul_string)

f = open("input.txt", "r")
for line in f:
    parse_mul_strings(line)

print(answer)