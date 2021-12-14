from ctypes import sizeof
from os import path, stat
from collections import defaultdict
from math import *
import timeit
import time

class Transition:
    def __init__(self, f, t, e) -> None:
        self.origin = f
        self.destination = t
        self.edge = e

start = timeit.default_timer()

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
    new_pair_counts = defaultdict(lambda: 0)
    for transition in transitions:
        pairs_for_transition = pair_counts[(transition.origin, transition.destination)]
        counts[transition.edge] += pairs_for_transition
        new_pair_counts[(transition.origin, transition.destination)] -= pairs_for_transition
        new_pair_counts[transition.origin, transition.edge] += pairs_for_transition
        new_pair_counts[transition.edge, transition.destination] += pairs_for_transition

    for i in new_pair_counts.items():
        pair_counts[i[0]] += i[1]
        
s = sorted(counts.items(), key=lambda kv: kv[1])
print(s[-1][1] - s[0][1])

end = timeit.default_timer()
print(end - start)