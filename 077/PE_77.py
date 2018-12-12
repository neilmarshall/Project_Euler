#! /usr/bin/env python3.7
"""
It is possible to write ten as the sum of primes in exactly five different ways:
 
    7 + 3
    5 + 5
    5 + 3 + 2
    3 + 3 + 2 + 2
    2 + 2 + 2 + 2 + 2
 
What is the first value which can be written as the sum of primes in over five
thousand different ways?
 
Solution: 71
"""
from functools import lru_cache
 
@lru_cache(maxsize=None)
def P(n):
    is_prime = lambda n: all(n % p != 0 for p in range(2, int(n**0.5) + 1)) and n > 1
    D = {t: 0 for t in range(1, n + 1)}
    for p in filter(is_prime, range(n, 0, -1)):
        D[p] = sum(P(n - p)[t] for t in range(1, min(p, n - p) + 1)) if n > p else 1
    return D

 
def PE_77(limit, test_value=1):
    """
    >>> PE_77(5000)
    71
    """
    if sum(P(test_value).values()) < limit:
        return PE_77(limit, test_value + 1)
    else:
        return test_value

 
if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
