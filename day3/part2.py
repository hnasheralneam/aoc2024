import re

answer = 0
mul_strings = []
sections = []

def parse_mul_call(mul_call_string):
    global answer

    numbers_string = mul_call_string.replace("mul(", "").replace(")", "")
    numbers_string_array = numbers_string.split(",")
    answer += int(numbers_string_array[0]) * int(numbers_string_array[1])

def parse_mul_strings(section):
    global mul_strings
    for section in sections:
        if not ("don't" in section):
            parse_mul_strings(section)

    mul_strings += re.findall("mul\([0123456789]*,[0123456789]*\)", section)
    for mul_string in mul_strings:
        parse_mul_call(ul_string)

def parse_sections(line):

    s = "This is a test don't()and this is another test don't()final part"
    result = s.split("don't()")
    print(result)

    enabled = []
    parts = line.split("don't()")
    
    for part in parts:
        print(part)
        print("\n\n")
    

#
f = open("input.txt", "r")
for line in f:
    parse_sections(line)

print(answer)