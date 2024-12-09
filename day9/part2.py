data = []
is_data = True
id_num = 0

empty_spaces = []
blocks = []

f = open("day9/input.txt", "r").readlines()[0]

def spot_available(size):
    for i in range(0, len(empty_spaces)):
        space = empty_spaces[i]
        if len(space) >= size:
            empty_spaces.pop(i)
            return space
    return -1

def swap(first, second):
    temp = data[first]
    data[first] = data[second]
    data[second] = temp

def move(block, empty_spot):
    # both block and empty_spot are in format [startIndex, length]
    for i in range(0, empty_spot[1]):
        swap(empty_spot[0] + i, block[0] + i)

for num in f:
    for i in range(0, int(num)):
        value = -1
        if is_data:
            value = id_num
        data.append(int(value))
    if is_data:
        blocks.append([len(data) - 1, int(num)])
        id_num += 1
    else:
        empty_spaces.append([len(data) - 1, int(num)])
    is_data = not is_data
 
for block in reversed(blocks):
    empty_spot = spot_available(block[1])
    if not empty_spot == -1:
        move(block, empty_spot)

checksum = 0
for i in range(0, len(data)):
    if not data[i] == -1:
        checksum += data[i] * i

print(checksum)