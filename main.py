from os import stat
from collections import defaultdict
from math import *
import timeit

def main():
    with open('input.txt') as f:
        positions = f.readlines()[0].split(",")

    numbers = [int(position) for position in positions]

    costs = []

    for target in range(min(numbers), max(numbers)):
        cost = 0
        for crab_position in numbers:
            cost += sum(range(1, abs(crab_position - target) + 1))

        costs.append(cost)
        
    print(min(costs))

if __name__ == "__main__":
    main()
