import os
import sys

def intersection(lst1, lst2): 
    return set(lst1).intersection(lst2) 

def get_places(wire):
    places = []
    x = y = 0
    for instr in wire:
        coords = get_coord(x, y, instr)
        x = coords[-1][0]
        y = coords[-1][1]
        places.extend(coords)
    return places

def get_coord(x, y, instr):
    coords = []
    num = int(instr[1:])
    if instr.startswith("R"):
        for i in range(1, num+1):
            coords.append((x+i, y))
    elif instr.startswith("L"):
        for i in range(1, num+1):
            coords.append((x-i, y))
    elif instr.startswith("U"):
        for i in range(1, num+1):
            coords.append((x, y+i))
    elif instr.startswith("D"):
        for i in range(1, num+1):
            coords.append((x, y-i))
    return coords

f = open(os.path.join(sys.path[0], "testinput"), "r")
wire_1 = (f.readline()).split(",") 
wire_2 = (f.readline()).split(",")

wire_1_places = get_places(wire_1)
wire_2_places = get_places(wire_2)
inters = intersection(wire_1_places, wire_2_places)
distances = [abs(0-inter[0]) + abs(0-inter[1]) for inter in inters]
print(min(distances))