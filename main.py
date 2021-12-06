from os import stat
from collections import defaultdict
from math import *
import timeit

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        
        fish_initial = list(map(lambda f: int(f), lines[0].split(",")))

        fish = [0] * 9

        for f in fish_initial:
            fish[f] += 1

        for i in range(257):
            print(f"{fish} : {sum(fish)}")
            new_fish_count = fish[0]
            for f_index in range(8):
                fish[f_index] = fish[f_index + 1]

            fish[6] += new_fish_count
            fish[8] = new_fish_count

if __name__ == "__main__":
    main()
