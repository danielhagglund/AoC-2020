slope_map = []
row = 0
col = 0
trees_hit = 0

input_data = open("./Day3/input.txt").read().splitlines()

for datarow in input_data:
    slope_map.append(datarow*1000)

for x in range(len(slope_map)-1):
    row += 1
    col += 3
    if slope_map[row][col] == "#":
        trees_hit += 1
print(trees_hit)
