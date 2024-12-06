count = 0
map = []
pos = []
direction = 0

def turn():
    global direction
    direction += 90
    if direction == 360:
        direction = 0

def place_ahead_exists():
    if direction == 0:
        return pos[0] - 1 >= 0
    if direction == 90:
        return pos[1] + 1 < len(map[0])
    if direction == 180:
        return pos[0] + 1 < len(map)
    if direction == 270:
        return pos[1] - 1 >= 0

def next_spot():
    if direction == 0:
        return map[pos[0] - 1][pos[1]]
    if direction == 90:
        return map[pos[0]][pos[1] + 1]
    if direction == 180:
        return map[pos[0] + 1][pos[1]]
    if direction == 270:
        return map[pos[0]][pos[1] - 1]
    
def next_spot_index_change(type):
    if type == "x":
        if direction == 0:
            return -1
        if direction == 180:
            return 1
    if type == "y":
        if direction == 90:
            return 1
        if direction == 270:
            return -1
    return 0

def move():
    if not next_spot() == "#":
        map[pos[0]][pos[1]] = "X"
        pos[0] = pos[0] + next_spot_index_change("x")
        pos[1] = pos[1] + next_spot_index_change("y")
    else:
        turn()
        

with open("day6/input.txt", "r") as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        chars = []
        for char in lines[i]:
            if char != "\n":
                chars.append(char)
            if char == "^":
                pos = [i, len(chars) - 1]
        map.append(chars)

while (place_ahead_exists()):
    move()

for row in map:
    for item in row:
        if item == "X":
            count += 1

# for final spot
count += 1
print(count)