farm = []
plant_types = []
regions = []

def item_in(item, main_list):
  for sublist in main_list:
    if item in sublist:
      print(item, sublist)
      return True
  return False

def get_matching_neighbors(pos, value):
    valid_neighbors = []
    if pos[0] > 0 and farm[pos[0] - 1][pos[1]] == value:
        valid_neighbors.append([pos[0] - 1, pos[1]])
    if pos[0] + 1 < len(farm) and farm[pos[0] + 1][pos[1]] == value:
        valid_neighbors.append([pos[0] + 1, pos[1]])
    if pos[1] > 0 and farm[pos[0]][pos[1] - 1] == value:
        valid_neighbors.append([pos[0], pos[1] - 1])
    if pos[1] + 1 < len(farm) and farm[pos[0]][pos[1] + 1] == value:
        valid_neighbors.append([pos[0], pos[1] + 1])
    return valid_neighbors

def add_unique(arr_one, arr_two):
    for item in arr_two:
        if not item in arr_one:
            arr_one.append(item)
    return arr_one

def get_region(pos, plots_in_region):
    plant = farm[pos[0]][pos[1]]

    matching_neighbors = get_matching_neighbors(pos, plant)
    if len(matching_neighbors) > 0:
        for match in matching_neighbors:
            add_unique(plots_in_region, get_matching_neighbors(match, plant))
    
    return plots_in_region

with open("day12/input.txt", "r") as f:
    for line in f:
        plots = []
        for plot in line:
            if plot != "\n":
                plots.append(plot)
                if not plot in plant_types:
                    plant_types.append(plot)
        farm.append(plots)

for i in range(0, len(farm)):
    for j in range(0, len(farm[i])):
        if not item_in([i, j], regions):
           regions.append(get_region([i, j], [[i, j]]))

print(regions)
print("done")