stones = []
blinks = 0

f = open("day11/input.txt", "r").readlines()[0]
stones = f.split(" ")
stones = [int(stone) for stone in stones]

while blinks < 25:
    for i in range(0, len(stones)):
        stone = stones[i]
        if stone == 0:
            stones[i] = 1
        elif len(str(stone)) % 2 == 0:
            stones[i] = int(str(stone)[:len(str(stone)) // 2])
            stones.append(int(str(stone)[len(str(stone)) // 2:]))
            i += 1
        else:
            stones[i] *= 2024
    blinks += 1

print(len(stones))