data = []
is_data = True
id_num = 0

f = open("day9/input.txt", "r").readlines()[0]

def get_empty_before(i):
    index = data.index(-1)
    if index >= i:
        return -1
    else:
        return index

def swap(first, second):
    temp = data[first]
    data[first] = data[second]
    data[second] = temp

for num in f:
    for i in range(0, int(num)):
        value = -1
        if is_data:
            value = id_num
        data.append(int(value))
    if is_data:
        id_num += 1
    is_data = not is_data

for i in range(len(data) - 1, -1, -1):
    if not data[i] == -1:
        empty_spot = get_empty_before(i)
        if not empty_spot == -1:
            swap(i, empty_spot)
        else:
            break;

checksum = 0
for i in range(0, len(data)):
    if not data[i] == -1:
        checksum += data[i] * i

print(checksum)