"""Module containing functions to identify primes, generate primes, and
factorize numbers into primes"""

def is_prime(n):
    """
    Return primality of n

    >>> is_prime(5)
    True

    >>> is_prime(6)
    False
    """
    if n <= 1:
        return False

    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            return False

    return True


def get_primes_under_n(n):
    """
    Return list of primes less than n

    >>> get_primes_under_n(23)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if n <= 1:
        return []

    flags = [False, False] + [True for _ in range(2, n + 1)]
    for p in range(2, n // 2 + 1):
        for q in range(2, n // p + 1):
            flags[p * q] = False

    return [i for i, prime in enumerate(flags) if prime and i < n]


def get_primes_up_to_n(n):
    """
    Return list of primes up to and including n

    >>> get_primes_up_to_n(23)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    """
    return get_primes_under_n(n + 1)


def get_prime_factors(n):
    """
    Return list of (non-unique) prime factors of n

    >>> get_prime_factors(100)
    [2, 2, 5, 5]
    """
    if n <= 1:
        return []

    factors = []
    primes = get_primes_up_to_n(int(n**0.5))
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n /= prime

    if n > 1:
        factors.append(n)

    return factors


def get_unique_prime_factors(n):
    """
    Return list of unique prime factors of n

    >>> get_unique_prime_factors(100)
    [2, 5]
    """
    return sorted(set(get_prime_factors(n)))

