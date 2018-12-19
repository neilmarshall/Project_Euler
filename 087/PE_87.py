#! /usr/bin/env python3.7
"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

    28 = 2^2 + 2^3 + 2^4
    33 = 3^2 + 2^3 + 2^4
    49 = 5^2 + 2^3 + 2^4
    47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

Solution: 1097343
"""
from itertools import product

def get_primes(limit):
    flags = [False, False] + [True for _ in range(2, limit + 1)]
    for p in range(2, limit // 2 + 1):
        for q in range(2, limit // p + 1):
            flags[p * q] = False
    return [i for (i, flag) in enumerate(flags) if flag]


def get_prime_powers(limit, powers):
    primes = get_primes(limit)
    prime_powers = []
    for power in powers:
        prime_powers.append([prime**power for prime in primes if prime**power <= limit])
    return prime_powers


def PE_87(limit):
    """
    >>> PE_87(50)
    4

    >>> PE_87(50000000)
    1097343
    """
    prime_squares, prime_cubes, prime_quads = get_prime_powers(limit, [2, 3, 4])
    prime_power_sums = set()
    for (p1, p2, p3) in product(prime_squares, prime_cubes, prime_quads):
        prime_power_sums.add(p1 + p2 + p3)
    return sum(1 for prime_power_sum in prime_power_sums if prime_power_sum <= limit)


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
