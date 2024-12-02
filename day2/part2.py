safe_count = 0

def line_to_array(line):
    return [int(x) for x in line.split()]

def line_is_safe(arr):
    dampened = False
    increasing = arr[0] < arr[1]
    for i in range(0, len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if arr[i] > arr[i + 1] and increasing:
            if dampened:
                return False
            else:
                dampened = True
        elif arr[i] < arr[i + 1] and not increasing:
            if dampened:
                return False
            else:
                dampened = True
        elif arr[i] == arr[i + 1]:
            if dampened:
                return False
            else:
                dampened = True
        elif diff < 1 or diff > 3:
            if dampened:
                return False
            else:
                dampened = True
    return True

        

f = open("input.txt", "r")
for line in f:
    if line_is_safe(line_to_array(line)):
        safe_count += 1

print(safe_count)