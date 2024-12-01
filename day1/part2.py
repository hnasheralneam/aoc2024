difference_sum = 0
left_side = []
right_side = []

def instances_in_array(arr, num):
    count = 0
    for i in arr:
        if i == num:
            count += 1
    return count

f = open("input.txt", "r")
for line in f:
    line_sides = line.split("   ")
    left_side.append(int(line_sides[0]))
    right_side.append(int(line_sides[1]))

for i in range(len(left_side)):
    difference_sum += left_side[i] * instances_in_array(right_side, left_side[i])

print(difference_sum)