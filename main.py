from ctypes import sizeof
from os import path, stat
from collections import defaultdict
from math import *
import timeit
import time

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    nodes = dict()

    for line in lines:
        caves = line.strip().split("-")
        f = Cave(caves[0]) if caves[0] not in nodes else nodes[caves[0]]
        t = Cave(caves[1]) if caves[1] not in nodes else nodes[caves[1]]
        t.neighbours.append(f)
        f.neighbours.append(t)

        nodes[f.name] = f
        nodes[t.name] = t

    print(nodes)

    paths = [[nodes["start"]]]
    done = False

    while not done:
        new_paths = []
        for path in paths:
            new_paths += progress(path)

        if len(new_paths) == len(paths):
            done = True

        paths = new_paths

    print(str(paths).replace("],", "\n").replace("[", "").replace(" ", "").replace("]", ""))
    print(len(paths))

def progress(path):
    has_double = has_double_small(path)
    last_node = path[-1]

    if last_node.name == "end":
        return [path]

    paths = []
    for neighbour in last_node.neighbours:
        if neighbour.name == "start":
            continue

        if has_double and neighbour.is_small() and neighbour in path:
            continue
        
        paths.append(list(path) + [neighbour])

    return paths

def has_double_small(path) -> bool:
    counts = defaultdict(lambda: 0)
    for node in path:
        if node.is_small():
            counts[node] += 1
            if counts[node] == 2:
                return True

    return False

class Cave:
    def __init__(self, name) -> None:
        self.name = name
        self.neighbours = []

    def is_small(self) -> bool:
        return self.name.islower()

    def __repr__(self) -> str:
        return self.name

if __name__ == "__main__":
    main()
