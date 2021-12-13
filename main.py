from ctypes import sizeof
from os import path, stat
from collections import defaultdict
from math import *
import timeit
import time

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    coordinates = []
    folds = []
    max_x = 0
    max_y = 0

    for line in lines:
        if line == "\n":
            continue

        if line.startswith("fold along"):
            s = line.strip().split(" ")[2].split("=")
            folds.append((s[0], int(s[1])))
            continue

        s = line.strip().split(",")
        x = int(s[0])
        if x > max_x:
            max_x = x

        y = int(s[1])
        if y > max_y:
            max_y = y

        coordinates.append((x, y))

    grid = [[0] * (max_x + 1) for i in range(max_y + 1)]

    for c in coordinates:        
        grid[c[1]][c[0]] = 1

    new_grid = grid
    for f in folds:
        top_half = sub_grid_horizontal(new_grid, 0, f[1]) if f[0] == "y" else sub_grid_vertical(new_grid, 0, f[1])
        bottom_half = sub_grid_horizontal(new_grid, f[1] + 1, len(new_grid)) if f[0] == "y" else sub_grid_vertical(new_grid, f[1] + 1, len(new_grid[0]))
        bottom_flipped = flip_vertically(bottom_half, []) if f[0] == "y" else flip_horizontally(bottom_half, [])
        overlayed = overlay(top_half, bottom_flipped)
        new_grid = overlayed

        # print_grid(top_half)
        # print("\n\n")
        # print_grid(bottom_half)
        # print("\n\n")
        # print_grid(bottom_flipped)
        # print("\n\n")
        # print_grid(overlayed)
        # print("-----------")

    grid_to_file(new_grid)

def sub_grid_horizontal(grid, y1, y2):
    return [grid[y] for y in range(y1, y2)]

def sub_grid_vertical(grid, x1, x2):
    sub_grid = []
    for j in range(len(grid)):
        sub_grid.append([grid[j][i] for i in range(x1, x2)])
    return sub_grid

def flip_vertically(grid, new_grid):
    if len(new_grid) == len(grid):
        return new_grid

    next_row = grid[len(new_grid)]
    return flip_vertically(grid, [next_row] + new_grid)

def flip_horizontally(grid, new_grid):
    if len(new_grid) > 0 and len(new_grid[0]) == len(grid[0]):
        return new_grid

    for y in range(len(grid)):
        if len(new_grid) < len(grid):
            new_grid.append([])

        new_grid[y].append(grid[y][(len(grid[y]) - len(new_grid[y]) - 1)])

    return flip_horizontally(grid, new_grid)

def overlay(ga, gb):
    overlayed = list(ga)
    gby = 0
    gbx = 0
    for j in range(len(ga) - len(gb), len(ga)):
        for i in range(len(ga[0]) - len(gb[0]), len(ga[0])):
            ga_value = ga[j][i]
            gb_value = gb[gby][gbx]
            overlayed[j][i] = min(ga_value + gb_value, 1)
            gbx += 1
        gby += 1
        gbx = 0
    return overlayed

def count_grid(grid):
    count = 0
    for line in grid:
        count += sum(line)
    
    return count

def print_grid(grid):
    print(grid_string(grid))

def grid_string(grid):
    s = ""
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            s += "." if grid[j][i] == 0 else "#"
        s += "\n"
    return s

def grid_to_file(grid):
    with open('grid.txt', mode="w") as f:
        f.write(grid_string(grid))

if __name__ == "__main__":
    main()
