stones = []
stone_count = 0
blinks = 0
max_blinks = 75

f = open("day11/input.txt", "r").readlines()[0]
stones = f.split(" ")
stones = [int(stone) for stone in stones]

def add_stones(stone, current_blinks):
    global stone_count

    if current_blinks == max_blinks:
        stone_count += 1
        return

    if stone == 0:
        add_stones(1, current_blinks + 1)
    elif len(str(stone)) % 2 == 0:
        add_stones(int(str(stone)[:len(str(stone)) // 2]), current_blinks + 1)
        add_stones(int(str(stone)[len(str(stone)) // 2:]), current_blinks + 1)
    else:
        add_stones(stone * 2024, current_blinks + 1)

for stone in stones:
    add_stones(stone, 0)

print(stone_count)