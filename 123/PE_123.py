#! venv/bin/python3.7
"""
Let p_n be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder
when (p_n - 1)^n + (p_n + 1)^n is divided by p_n^2.

For example, when n = 3, p_3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10^9 is 7037.

Find the least value of n for which the remainder first exceeds 10^10.

Solution: 21035
"""
from pyutils.primes import get_primes_up_to_n

def PE123(limit, prime_limit=2, skip=0):
    """
    >>> PE123(1e9)
    7037

    >>> PE123(1e10)
    21035
    """
    psr = lambda p, n: ((p - 1)**n + (p + 1)**n) % p**2
    primes = get_primes_up_to_n(prime_limit)
    for n, p in enumerate(primes[skip:], skip + 1):
        remainder = psr(p, n)
        if remainder >= limit:
            return n
    return PE123(limit, prime_limit * 2, len(primes))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
