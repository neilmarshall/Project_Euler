"""
We can easily verify that none of the entries in the first seven rows of
Pascal's triangle are divisible by 7.

However, if we check the first one hundred rows, we will find that only 2361 of
the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one
billion (10^9) rows of Pascal's triangle.

Solution: 2129970655314432
"""

from math import floor, log

def PE_148(n):
    """
    >>> PE_148(1000000000)
    2129970655314432
    """
    s, m, t = 0, 1, int(floor(log(n) / log(7)))
    while t >= 0:
        b = n // 7**t
        s += m * (b * (b + 1)) // 2 * 28**t
        m *= b + 1
        n -= b * 7**t
        t -= 1
    return s


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
