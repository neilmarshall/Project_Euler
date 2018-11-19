#! /usr/local/bin/python3.7
"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?

Solution: 190569291
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def P(n):
    if n <= 1:
        return {1: 1}
    D = {n: 1}
    for t in range(n - 1, 0, -1):
        D[t] = sum(P(n - t)[x] for x in range(1, t + 1) if x <= n - t)
    return D


def PE_76(n):
    """
    >>> PE_76(100)
    190569291
    """
    return sum(P(n).values()) - 1


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
