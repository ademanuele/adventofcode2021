from os import stat
from collections import defaultdict
from math import *
import timeit

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        
        fish = list(map(lambda f: int(f), lines[0].split(",")))

        for i in range(256):
            new_fish_count = 0
            for f_index in range(len(fish)):
                if fish[f_index] == 0:
                    fish[f_index] = 6
                    new_fish_count += 1
                    continue

                fish[f_index] -= 1

            for i in [8] * new_fish_count:
                fish.append(i)

        print(len(fish))

if __name__ == "__main__":
    main()
