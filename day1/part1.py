difference_sum = 0
left_side = []
right_side = []

def get_and_remove_smallest(arr):
    smallest = min(arr)
    arr.remove(smallest)
    return smallest

f = open("input.txt", "r")
for line in f:
    line_sides = line.split("   ")
    left_side.append(int(line_sides[0]))
    right_side.append(int(line_sides[1]))

for i in range(len(left_side)):
    difference_sum += abs(get_and_remove_smallest(left_side) - get_and_remove_smallest(right_side))

print(difference_sum)