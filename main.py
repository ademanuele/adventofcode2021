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
            
            low_points.append(point)

    print(low_points)
    print(sum(low_points) + len(low_points))

if __name__ == "__main__":
    main()
