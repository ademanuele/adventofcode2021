from os import stat
from collections import defaultdict
from math import *
import timeit

def main():
    with open('input.txt') as f:
        positions = f.readlines()[0].split(",")
        numbers = [int(position) for position in positions]

        costs = []

        for i in range(min(numbers), max(numbers)):
            costs.append(sum(list(map(lambda n: abs(n - i), numbers))))
        
        print(min(costs))

if __name__ == "__main__":
    main()
