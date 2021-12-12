from ctypes import sizeof
from os import stat
from collections import defaultdict
from math import *
import timeit

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    openers = ['(', '{', '[', '<']
    closers = [')', '}', ']', '>']
    corrupt_score = { ')': 3, '}': 1197, ']': 57, '>': 25137 }
    complete_score = { '(': 1, '[': 2, '{': 3, '<': 4 }

    score = 0
    scores = []

    for line in lines:
        line = line.strip()
        symbol_stack = []

        corrupt = False

        for symbol in line:
            if symbol in openers:
                symbol_stack.append(symbol)
            else:
                closer_index = closers.index(symbol)
                corresponding_opener = openers[closer_index]
                if symbol_stack[len(symbol_stack) - 1] == corresponding_opener:
                    symbol_stack.pop()
                else:
                    score += corrupt_score[symbol]
                    corrupt = True
                    break
                        
        if not corrupt:
            score = 0
            complete = ""
            for i in range(len(symbol_stack) - 1, -1, -1):
                score *= 5
                score += complete_score[symbol_stack[i]]
                complete += symbol_stack[i]

            scores.append(score)

            print(f"{complete} = {score}")             

    scores.sort()
    print(scores)
    print(len(scores))
    print(scores[int(len(scores) / 2)])

if __name__ == "__main__":
    main()
