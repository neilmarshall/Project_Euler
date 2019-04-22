#! venv/bin/python3.7

"""
There are some prime values, p, for which there exists a positive integer, n,
such that the expression n^3 + n^2 * p is a perfect cube.

For example, when p = 19, 8^3 + 8^2 × 19 = 12^3.

What is perhaps most surprising is that for each prime with this property the
value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?

Solution: 173
"""

from itertools import count
from pyutils.primes import get_primes_up_to_n

def PE_131(limit):
    """
    >>> PE_131(100)
    4

    >>> PE_131(1000000)
    173
    """
    primes = set(get_primes_up_to_n(limit))
    solutions = 0
    for g in count(1):
        x = g + g**(3/2)
        if int(x) == x:
            n = x - g
            p = int(round((x**3 - n**3) / n**2, 0))
            solutions += 1 if p in primes else 0
            if p > limit:
                break
    return solutions


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
