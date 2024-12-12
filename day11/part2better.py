stones = []
stone_count = 0
blinks = 0
max_blinks = 35
paths = {}

f = open("day11/input.txt", "r").readlines()[0]
stones = f.split(" ")
stones = [int(stone) for stone in stones]

def add_stones(stone, current_blinks):
    global stone_count

    if current_blinks == max_blinks:
        stone_count += 1
        return


    if stone in paths:
        for item in paths[stone]:
            add_stones(item, current_blinks + 1)
        return
    else:
        stone_values = []
        if stone == 0:
            stone_values.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_values.append(int(str(stone)[:len(str(stone)) // 2]))
            stone_values.append(int(str(stone)[len(str(stone)) // 2:]))
        else:
            stone_values.append(stone * 2024)

        paths[stone] = stone_values 
        for item in stone_values:
            add_stones(item, current_blinks + 1)

for stone in stones:
    add_stones(stone, 0)

print(stone_count)