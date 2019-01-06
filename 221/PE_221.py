#! /usr/bin/env python3.7
"""
We shall call a positive integer A an "Alexandrian integer", if there exist
integers p, q, r such that:

    A = p . q . r, and 1 / A = 1 / p + 1 / q + 1 / r

For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18). In fact,
630 is the 6th Alexandrian integer, the first 6 Alexandrian integers being:

    6, 42, 120, 156, 420 and 630.

Find the 150000th Alexandrian integer.

Note -- The first such integers are:

    [6, 42, 120, 156, 420, 630, 930, 1428, 1806, 2016, 2184, 3192, 4950, 5256,
     8190, 8364, 8970, 10296, 10998, 12210, 17556, 19110, 21114, 23994, 24492,
     28050, 32640, 33306, 34362, 37506, 39270, 44310, 52326, 57684, 57840,
     70686, 74256, 79800, 83076]
    
Solution: 1884161251122450
"""
from math import floor

def PE_221(limit):
    """
    >>> PE_221(6)
    630

    >>> PE_221(39)
    83076

    >>> PE_221(150000)  #doctest: +SKIP
    1884161251122450
    """
    A = []
    p = r = 0

    # calculate initial list of values
    while len(A) < limit:
        r += 1
        p = -(r + 1)
        while (p**2 + 2 * p * r - 1) < 0:
            q = (1 - p * r) / (p + r)
            if floor(q) == q:
                A.append(int(p * q * r))
            p -= 1

    # for initial list of values, if subsequent (lower) values can be found
    # then replace components of the initial list greater than the new values
    A.sort()
    curMax = A[-1]
    while r * (r + 1) * (r + 2) < curMax:
        r += 1
        p = -(r + 1)
        while (p**2 + 2 * p * r - 1) < 0:
            q = (1 - p * r) / (p + r)
            if floor(q) == q:
                if p * q * r < curMax:
                    A.pop()
                    A.append(int(p * q * r))
                    A.sort()
                    curMax = A[limit - 1]
            p -= 1

    return A[limit - 1]


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
