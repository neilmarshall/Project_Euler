#! /usr/bin/env python3.7
"""
The positive integers, x, y, and z, are consecutive terms of an arithmetic
progression. Given that n is a positive integer, the equation, x^2 − y^2 − z^2 = n,
has exactly one solution when n = 20:

    13^2 − 10^2 − 7^2 = 20

In fact there are twenty-five values of n below one hundred for which the
equation has a unique solution.

How many values of n less than fifty million have exactly one solution?

Solution: 2544559
"""
from collections import Counter
from math import sqrt

def PE136(limit):
    solution_counter = Counter()
    for e in range(1, (limit + 1) // 4 + 1):
        if e % 1000 == 0:
            print(f"\t{4 * e / limit:.2%}", end='\r')
        x_min = 1 if 4 * e**2 - limit < 0 else int(e + sqrt(4 * e**2 - limit))
        for x in range(x_min, 3 * e):
            n = (e + x) * (3 * e - x)
            if n <= limit:
                solution_counter[n] += 1

    return len([i for i, solution in solution_counter.items() if solution == 1])


if __name__ == '__main__':
    print(PE136(int(50e6)))
