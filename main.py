from os import stat
from collections import defaultdict
from math import *

def main():
    print("Starting...")

    with open('input.txt') as f:
        lines = f.readlines()
        point_counts = defaultdict(lambda: 0)

        for lineS in lines:            
            line = Line(lineS)

            if line.is_diagonal():
                continue

            for point in line.to_points():
                point_counts[str(point)] += 1

        count = 0
        print_grid(point_counts, 20, 20)
        for i in point_counts.values():
            if i > 1:
                count += 1

        print(count)

def print_grid(points, width, height):
    for i in range(height):
        for j in range(width):
            count = points[f"{j}, {i}"]
            print("." if count == 0 else count, end=" ")
        print()
            
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # def __hash__(self) -> int:
    #     return self.__repr__().__hash__()

    # def __eq__(self, __o: object) -> bool:
    #     return __o is Point and __o.x == self.x and __o.y == self.y

    def __repr__(self):
        return f"{self.x}, {self.y}"

class Line:
    def __init__(self, line) -> None:
        coordinates = line.split(" -> ")
        startCoordinates = coordinates[0].split(",")
        endCoordinates = coordinates[1].split(",")

        self.x1 = int(startCoordinates[0])
        self.y1 = int(startCoordinates[1])
        self.x2 = int(endCoordinates[0])
        self.y2 = int(endCoordinates[1])

    def is_diagonal(self) -> bool:
        return self.x1 != self.x2 and self.y1 != self.y2

    def is_horizontal(self) -> bool:
        return self.y1 == self.y2

    def length(self) -> int:
        return int(sqrt(pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2)))

    def to_points(self) -> list[Point]:
        points = []

        x = self.x1
        y = self.y1

        while (x != self.x2) or (y != self.y2):
            points.append(Point(x, y))
            if self.x2 > x:
                x += 1
            elif self.x2 < x:
                x -= 1

            if self.y2 > y:
                y += 1
            elif self.y2 < y:
                y -= 1

        points.append(Point(self.x2, self.y2))
        return points

if __name__ == "__main__":
    main()
