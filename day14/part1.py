height = 103
width = 101
robots = []
grid = [[0] * height] * width

def move(start, change, limit):
    num = start + change
    if num >= limit:
        num = num - limit
    elif num < 0:
        num = num + limit
    return num


def find_future_position(position, velocity):
    global robots

    for i in range(0, 100):
        position[0] = move(position[0], velocity[0], width)
        position[1] = move(position[1], velocity[1], height)
    
    robots.append([position, velocity])

def parse_robot(line):
    global sum

    splitted = line.split(" ")
    position = list(map(int, splitted[0].replace("p=", "").split(",")))
    velocity = list(map(int, splitted[1].replace("v=", "").split(",")))
    
    find_future_position(position, velocity)

with open("day14/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        parse_robot(line.replace("\n", ""))

# count robots
for robot in robots:
    robot_position = robot[0]
    print(robot_position)
    grid[robot_position[0]][robot_position[1]] += 1

print(grid)