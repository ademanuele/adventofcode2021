from ctypes import sizeof
from os import path, stat
from collections import defaultdict
from math import *
import timeit
import time

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    transitions = []
    template = lines[0]
    counts = defaultdict(lambda: 0)
    pair_counts = defaultdict(lambda: 0)

    for n in template.strip():
        counts[n] += 1

    for n in range(len(template.strip()) - 1):
        pair_counts[(template[n], template[n + 1])] += 1

    for i in range(2, len(lines)):
        rule_s = lines[i].strip().split(" -> ")
        f = rule_s[0][0]
        t = rule_s[0][1]
        e = rule_s[1]
        transitions.append(Transition(f, t, e))

    for iter in range(40):
        print(f"Starting {iter}")
        # print(str(pair_counts).replace(", (", ",\n("))
        new_pair_counts = defaultdict(lambda: 0)
        for transition in transitions:
            pairs_for_transition = pair_counts[(transition.origin, transition.destination)]
            counts[transition.edge] += pairs_for_transition
            new_pair_counts[(transition.origin, transition.destination)] -= pairs_for_transition
            new_pair_counts[transition.origin, transition.edge] += pairs_for_transition
            new_pair_counts[transition.edge, transition.destination] += pairs_for_transition

        # print(str(new_pair_counts).replace(", (", ",\n("))

        for i in new_pair_counts.items():
            pair_counts[i[0]] += i[1]
            
        # print(str(pair_counts).replace(", (", ",\n("))

    s = sorted(counts.items(), key=lambda kv: kv[1])
    print(str(s).replace(", (", ",\n("))
    print(s[-1][1] - s[0][1])

class Transition:
    def __init__(self, f, t, e) -> None:
        self.origin = f
        self.destination = t
        self.edge = e

if __name__ == "__main__":
    main()
