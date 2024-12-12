map = []
zeros = []
trails = 0

def get_valid_neighbors(pos, num):
    valid_neighbors = []
    if pos[0] > 0 and map[pos[0] - 1][pos[1]] == num:
        valid_neighbors.append([pos[0] - 1, pos[1]])
    if pos[0] + 1 < len(map) and map[pos[0] + 1][pos[1]] == num:
        valid_neighbors.append([pos[0] + 1, pos[1]])
    if pos[1] > 0 and map[pos[0]][pos[1] - 1] == num:
        valid_neighbors.append([pos[0], pos[1] - 1])
    if pos[1] + 1 < len(map) and map[pos[0]][pos[1] + 1] == num:
        valid_neighbors.append([pos[0], pos[1] + 1])

    return valid_neighbors

def find_next(pos, num):
    global trails

    target = num + 1
    if target == 10:
        return 1
    sum = 0
    for neighbor in get_valid_neighbors(pos, target):
        sum += find_next(neighbor, target)
    return sum

with open("day10/input.txt", "r") as f:
    row = 0
    for line in f:
        chars = []
        col = 0
        while col < len(line):
            char = line[col]
            if char != "\n":
                chars.append(int(char))
            if char == "0":
                zeros.append([row, col])
            col += 1
        map.append(chars)
        row += 1

sum = 0
for zero in zeros:
    trails_from_head = find_next(zero, 0)
    sum += trails_from_head

print(sum)
