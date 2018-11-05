from math import floor, log

def factorise_powers_of_two(n):
    s, m = 0, n - 1
    while m % 2 == 0:
        s += 1
        m >>= 1
    d = n >> s
    return s, d


def miller_rabin_test(n):
    """
    Miller-Rabin primality test

    Deterministic implementation of Miller-Rabin primality test
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
    # discount even numbers
    if n <= 2 or n % 2 == 0:
        return n == 2

    # perform trial division based on initial primes
    initial_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                      53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n in initial_primes:
        return True
    if any(n % p == 0 and n < p for p in initial_primes):
        return False

    # test compositeness using Miller-Rabin algorithm, with suitable witnesses
    if n < 2047:
        witnesses = [2]
    elif n < 1373653:
        witnesses = [2, 3]
    elif n < 9080191:
        witnesses = [31, 73]
    elif n < 25326001:
        witnesses = [2, 3, 5]
    elif n < 3215031751:
        witnesses = [2, 3, 5, 7]
    elif n < 4759123141:
        witnesses = [2, 7, 61]
    elif n < 1122004669633:
        witnesses = [2, 13, 23, 1662803]
    elif n < 2152302898747:
        witnesses = [2, 3, 5, 7, 11]
    elif n < 3474749660383:
        witnesses = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        witnesses = [2, 3, 5, 7, 11, 13, 17]

    s, d = factorise_powers_of_two(n)
    for a in witnesses:
        if pow(a, d, n) != 1:
            if all(pow(a, pow(2, r) * d, n) != n - 1 for r in range(s)):
                return False
    return True
