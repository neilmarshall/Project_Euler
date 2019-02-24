#! /usr/bin/env python3.7
"""
The number 512 is interesting because it is equal to the sum of its digits
raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number
with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and insist that a number
must contain at least two digits to have a sum.

You are given that a(2) = 512 and a(10) = 614656.

Find a(30).

Solution: 248155780267521
"""

from itertools import count
from math import log

def PE_119(n):
    """
    >>> PE_119(2)
    512

    >>> PE_119(10)
    614656

    >>> PE_119(30)
    248155780267521
    """
    digit_power_sums = []
    limit = n * 2  # arbitrary limit; deemed large enough to identify first n ordered solutions
    for a in count(2):
        if len(digit_power_sums) >= limit:
            break
        for b in range(2, int(a * log(10) / log(a)) + 1):
            if a**b < 10:
                continue
            digit_sum = sum(map(int, str(a**b)))
            if digit_sum == a:        
                digit_power_sums.append(a**b)
    return sorted(digit_power_sums)[n - 1]  # -1 takes account of zero-based indexing


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
