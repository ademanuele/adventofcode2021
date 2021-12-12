from ctypes import sizeof
from os import stat
from collections import defaultdict
from math import *
import timeit

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    flashes = 0
    oct = list(map(lambda l: list(map(lambda o: int(o), l.strip())), lines))

    for _ in range(100):
        print(str(oct).replace("],", "\n").replace(", ", "").replace("[", "").replace("]", "").replace(" ", ""), end="\n\n")

        for j in range(len(oct)):
            for i in range(len(oct[j])):
                oct[j][i] += 1

        flashed = []
        check_again = True

        while check_again:
            new_flashes = []
            for j in range(len(oct)):
                for i in range(len(oct[j])):

                    if oct[j][i] > 9 and (j, i) not in flashed:
                        new_flashes.append((j, i))
                        adjacent = [(j - 1, i - 1), (j - 1, i), (j - 1, i + 1), (j, i - 1), (j, i + 1), (j + 1, i - 1), (j + 1, i), (j + 1, i + 1)]
                        for fa in adjacent:
                            invalid = fa[0] < 0 or fa[1] < 0 or fa[0] >= len(oct) or fa[1] >= len(oct[fa[0]])
                            if not invalid:
                                oct[fa[0]][fa[1]] += 1

            flashed += new_flashes

            if len(new_flashes) == 0:
                check_again = False

        for f in flashed:
            oct[f[0]][f[1]] = 0
        
        flashes += len(flashed)

    print(flashes)

if __name__ == "__main__":
    main()
