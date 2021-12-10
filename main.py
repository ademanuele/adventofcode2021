from ctypes import sizeof
from os import stat
from collections import defaultdict
from math import *
import timeit

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    start = timeit.default_timer()

    points = list(map(lambda line: list(map(lambda p: int(p), line.strip())), lines))
    low_points = []

    for y in range(len(points)):
        for x in range(len(points[y])):
            point = points[y][x]
            left_is_lower = x > 0 and points[y][x - 1] <= point
            right_is_lower = x < len(points[y]) - 1 and points[y][x + 1] <= point
            above_is_lower = y > 0 and points[y - 1][x] <= point
            below_is_lower = y < len(points) - 1 and points[y + 1][x] <= point

            if left_is_lower or right_is_lower or above_is_lower or below_is_lower:
                continue
            
            low_points.append((y, x))

    basin_sizes = []

    for point in low_points:
        boundary = [point]
        checked_points = set()

        while len(boundary) > 0:
            p = boundary.pop()
            checked_points.add(p)

            py = p[0]
            px = p[1]
            p_value = points[py][px]

            for adjacent in [(py, px - 1), (py, px + 1), (py - 1, px), (py + 1, px)]:
                if (adjacent[0] < 0) or (adjacent[0] >= len(points)) or (adjacent[1] < 0) or (adjacent[1] >= len(points[adjacent[0]])):
                    continue
                
                in_value_range = points[adjacent[0]][adjacent[1]] >= p_value and points[adjacent[0]][adjacent[1]] < 9
                if in_value_range and adjacent not in checked_points:
                    boundary.append(adjacent)

            # print(f"Checked: {len(checked_points)} Boundary: {len(boundary)}")
            
        # print(list(map(lambda p: points[p[0]][p[1]], checked_points)))
        print(f"Basin size: {len(checked_points)}")
        basin_sizes.append(len(checked_points))

    basin_sizes.sort()
    basins = len(basin_sizes)
    print(basin_sizes[basins - 1] * basin_sizes[basins - 2] * basin_sizes[basins - 3])

if __name__ == "__main__":
    main()
