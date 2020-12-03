slope_map = []

input_data = open("./Day3/input.txt").read().splitlines()

for datarow in input_data:
    slope_map.append(datarow*100)


def path_collisions(rowstep, colstep):
    row = 0
    col = 0
    trees_hit = 0
    while row < len(slope_map)-1:
        row += rowstep
        col += colstep
        if slope_map[row][col] == "#":
            trees_hit += 1
    print(trees_hit)
    return trees_hit


path1_treehit = path_collisions(1, 3)
path2_treehit = path_collisions(1, 1)
path3_treehit = path_collisions(1, 5)
path4_treehit = path_collisions(1, 7)
path5_treehit = path_collisions(2, 1)

print("Result")
print(path1_treehit*path2_treehit*path3_treehit*path4_treehit*path5_treehit)
