# create two arrays - one with actual values, one to put antinodes in
# create an object with arrays of the positions of each value other than .
map = []
antinodes = []
antenna = {}

with open("day8/input.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        row = []
        for char in line:
            row.append(char)
        map.append(row)

for row in map:
    for char in row:
        print(char, end=" ")
    print()