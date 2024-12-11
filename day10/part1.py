map = []
zeros = []
trails = 0

def get_valid_neighbors(pos, num):
    valid_neighbors = []
    if pos[0] - 1 > 0 and map[pos[0] - 1][pos[1]] == num:
        valid_neighbors.append(map[pos[0] - 1][pos[1]])
    if pos[0] + 1 < len(map) and map[pos[0] + 1][pos[1]] == num:
        valid_neighbors.append(map[pos[0] + 1][pos[1]])
    if pos[1] - 1 > 0 and map[pos[0]][pos[1] - 1] == num:
        valid_neighbors.append(map[pos[0]][pos[1] - 1])
    if pos[1] + 1 < len(map) and map[pos[0]][pos[1] + 1] == num:
        valid_neighbors.append(map[pos[0]][pos[1] + 1])
    return valid_neighbors

def find_next(pos, num):
    print(num)
    target = num + 1
    print(target)
    if target == 10:
        trails += 1
        return
    for neighbor in get_valid_neighbors(pos, target):
        find_next(neighbor, target)

with open("day10/input.txt", "r") as f:
    row = 0
    for line in f:
        chars = []
        col = 0
        while col < len(line):
            char = line[col]
            if char != "\n":
                chars.append(char)
            if char == "0":
                zeros.append([row, col])
            col += 1
        map.append(chars)
        row += 1

for zero in zeros:
    find_next(zero, 0)

print(trails)