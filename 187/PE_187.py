#! /usr/local/bin/python3.7
"""
A composite is a number containing at least two prime factors. For
example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily
distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 108, have precisely two, not necessarily
distinct, prime factors?

Notes:
    If n has exactly 2 primes factors then n = p.q, where p and q are primes
    and p (WLOG) is less than or equal to sqrt(n). q will then be a prime in
    the range [p, ..., n / p].

    So for prime up to sqrt(n), there will be as many numbers with exactly two
    prime factors as there are primes in the range [p, ..., n / p].

    Pseudocode algorithm:
        count = 0
        for primes p in [2, ..., sqrt(limit)]:
            for primes q in [p, ..., limit / 2]:
                count += 1
        return count

Solution: 17427258
"""
def get_primes_up_to_n(n):
    flags = [False, False] + [True for _ in range(2, n + 1)]
    for p in range(2, n // 2 + 1):
        if flags[p]:
            for q in range(2, n // p + 1):
                flags[p * q] = False
    return [i for i, flag in enumerate(flags) if flag]


def PE_187(limit):
    """
    >>> PE_187(30)
    10

    >>> PE_187(10**8)
    17427258
    """
    count = 0
    primes = get_primes_up_to_n(limit // 2)
    for i, p in enumerate(primes):
        if p > int(limit**0.5):
            break
        for q in primes[i:]:
            if p * q > limit:
                break
            count += 1
    return count
    

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
