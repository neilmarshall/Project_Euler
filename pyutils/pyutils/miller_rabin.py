from math import floor, log

def is_prime(n):
    if n <= 2:
        return n == 2
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            return False
    return True


def factorise_powers_of_two(n):
    s, m = 0, n - 1
    while m % 2 == 0:
        s += 1
        m //= 2
    d = n // 2**s
    return s, d


def miller_rabin_test(n):
    """
    Miller-Rabin primality test

    Deterministic implementation of Miller-Rabin primality test
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
    if n <= 2 or n % 2 == 0:
        return n == 2
    s, d = factorise_powers_of_two(n)
    for a in range(2, min(n - 1, floor(2 * log(n)**2)) + 1):
        if a**d % n != 1:
            if all(a**(2**r * d) % n != n - 1 for r in range(0, s)):
                return False
    return True
