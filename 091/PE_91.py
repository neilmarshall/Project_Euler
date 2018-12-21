#! /usr/bin/env python3.7
"""
There are exactly fourteen triangles containing a right angle that can be
formed when each co-ordinate lies between 0 and 2 inclusive; that
is, 0 <= x1, y1, x2, y2 <= 2.

Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed?

Solution: 14234
"""
from itertools import product

def PE_91(limit):
    """
    >>> PE_91(2)
    14

    >>> PE_91(50)
    14234
    """

    triCount = 0
    
    for x1, y1 in product(range(limit + 1), repeat=2):
        for x2, y2 in product(range(x1, limit + 1), range(y1 + 1)):
            if (x1 != x2 or y1 != y2) and (x1 != 0 or y1 != 0) and (x2 != 0 or y2 != 0):
                if x1 == 0 and y2 == 0:
                    triCount += 1
                elif (x1**2 + y1**2 == x1 * x2 + y1 * y2):
                    triCount += 1
                elif (x2**2 + y2**2 == x1 * x2 + y1 * y2):
                    triCount += 1
    
    return triCount


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
