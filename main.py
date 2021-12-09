from ctypes import sizeof
from os import stat
from collections import defaultdict
from math import *
import timeit

def main():
    with open('input.txt') as f:
        lines = f.readlines()

        start = timeit.default_timer()

        count = 0

        for line in lines:
            parts = line.split("|")
            digit_map_string = parts[0].strip().split(" ")
            digits = parts[1].strip().split(" ")
            
            one = digit_with_segment_count(2, digit_map_string)
            four = digit_with_segment_count(4, digit_map_string)
            seven = digit_with_segment_count(3, digit_map_string)
            eight = digit_with_segment_count(7, digit_map_string)

            occurances = defaultdict(lambda: 0)
            for m in digit_map_string:
                for char in m:
                    occurances[char] += 1

            top_segment = list(seven - one)[0]
            bottom_right_segment = list(filter(lambda o: o[1] == 9, occurances.items()))[0][0]
            top_right_segment = list(one - set([bottom_right_segment]))[0]
            bottom_left_segment = list(filter(lambda o: o[1] == 4, occurances.items()))[0][0]
            top_left_segment = list(filter(lambda o: o[1] == 6, occurances.items()))[0][0]
            middle_segment = list(four - frozenset([top_left_segment, top_right_segment, bottom_right_segment]))[0]
            bottom_segment = list(eight - set([top_segment,  bottom_right_segment, top_right_segment, bottom_left_segment, middle_segment, top_left_segment]))[0]

            digit_map = {
                frozenset([top_segment, top_left_segment, top_right_segment, bottom_left_segment, bottom_right_segment, bottom_segment]): '0',
                one: '1',
                frozenset([top_segment, top_right_segment, middle_segment, bottom_left_segment, bottom_segment]): '2',
                frozenset([top_segment, middle_segment, bottom_segment, top_right_segment, bottom_right_segment]): '3',
                four: '4',
                frozenset([top_segment, top_left_segment, middle_segment, bottom_right_segment, bottom_segment]): '5',
                frozenset([top_segment, top_left_segment, middle_segment, bottom_left_segment, bottom_right_segment, bottom_segment]): '6',
                seven: '7',
                eight: '8',
                frozenset([top_segment, top_left_segment, top_right_segment, middle_segment, bottom_right_segment, bottom_segment]): '9',
            }

            number = ""
            for digit in digits:
                number += digit_map[frozenset(digit)]
            
            count += int(number)

        end = timeit.default_timer()
        print(f"Count: {count}")
        print(f"Time: {end - start}")

def digit_with_segment_count(count, digits) -> frozenset[chr]:
    return frozenset(list(filter(lambda d: len(d) == count, digits))[0])

if __name__ == "__main__":
    main()
