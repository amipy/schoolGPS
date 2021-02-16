import math

import networkx as nx
import networkx.drawing
import matplotlib.pyplot as plt


def getDirection(last, current, target):
    tgtx, tgty = target
    lstx, lsty = last
    curx, cury = current

    tgtx = tgtx - lstx
    tgty = tgty - lsty
    curx = curx - lstx
    cury = cury - lsty
    lstx = 0
    lsty = 0
    invert_direction = False
    if curx < 0:
        invert_direction = True
    normaly = (tgty/tgtx)*curx
    if cury < normaly:
        if invert_direction:
            return "Left"
        return "Right"
    if invert_direction:
        return "Right"
    return "Left"
roomNums = {(1, 1): 9, (1, 2): 8, (1, 3): 10, (1, 4): 11, (1, 5): 11, (1, 6): 12, (1, 7): 1, (1, 8): 2, (1, 9): 7,
            (2, 1): 18, (2, 2): 18, (2, 3): 17, (2, 6): 20, (3, 1): 23, (3, 2): 23}

paths = [
    # floor 1
    [1, 2, 3],
    [1, 14, 1],
    [1, 13, 4],
    [2, 1, 3],
    [2, 5, 2],
    [3, 2, 2],
    [3, 4, 2],
    [4, 7, 8],
    [4, 21, 3],
    [5, 2, 2],
    [5, 4, 2],
    [6, 5, 5],
    [6, 7, 3.5],
    [7, 6, 3.5],
    [8, 9, 8],
    [8, 6, 7.75],
    [9, 18, 2],
    [10, 8, 3.75],
    [10, 11, 4],
    [10, 16, 4],
    [11, 12, 15],
    [12, 13, 9],
    [12, 20, 3],
    [13, 1, 3],
    [13, 2, 6],
    [14, 6, 6],
    [14, 10, 10],
    # floor 2
    # part 1
    [15, 11, 12],
    [16, 15, 2],
    [17, 8, 6],
    [17, 16, 9],
    [18, 9, 14],
    [18, 17, 9],
    [18, 23, 3],
    # part 2
    [19, 12, 5],
    [20, 19, 7],
    # part 3
    [21, 22, 4],
    [22, 7, 9],
    [23, 24, 6.5],
    [23, 25, 5],
    [24, 17, 3],
    [25, 18, 7]
]
# g.add_edges([(2, 0)])
# g.add_vertices(3)
# g.add_edges([(2, 3), (3, 4), (4, 5), (5, 3)])


# https://igraph.org/python/doc/tutorial/tutorial.html

g = nx.DiGraph()

biggest_node = 0
for i in paths:
    if i[0] > biggest_node:
        biggest_node = i[0]
    if i[1] > biggest_node:
        biggest_node = i[1]

orig = input("Origin room: ")
dest = input("Destination room: ")
orig_node = roomNums[(int(orig[1]), int(orig[0]))]
dest_node = roomNums[(int(dest[1]), int(dest[0]))]

first_floor_coords = {12: (227, 469), 11: (347, 223), 13: (393, 469), 10: (416, 232), 14: (449, 411), 1: (449, 440),
                      2: (503, 455), 3: (503, 489), 8: (553, 232), 6: (553, 355), 5: (553, 455), 4: (553, 492),
                      7: (607, 355), 9: (695, 235)}

edges = [(i[0], i[1], i[2]) for i in paths]
g.add_node(biggest_node)
# print(g.nodes)
g.add_weighted_edges_from(edges)
# print(g.edges)
nx.draw(g, with_labels=True)
path = nx.shortest_path(g, orig_node, dest_node)
print(path)
last = first_floor_coords[path[0]]
current = first_floor_coords[path[1]]
old_angle = 0
del path[:2]
print("Follow arrows")
for i in path:
    print(getDirection(last,current,first_floor_coords[i]), i)
    last=current
    current=first_floor_coords[i]
