import unittest
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


class TestMillerRabin(unittest.TestCase):

def test_miller_rabin_produces_primes_under_100(self):
        miller_rabin_output = [n for n in range(100) if miller_rabin_test(n)]
        primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, \
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(miller_rabin_output, primes_under_100)

    def test_miller_rabin_produces_sum_of_primes_under_1000(self):
        miller_rabin_output = sum(n for n in range(1000) if miller_rabin_test(n))
        sum_of_primes_under_1000 = sum(n for n in range(1000) if is_prime(n))
        self.assertEqual(miller_rabin_output, sum_of_primes_under_1000)


if __name__ == '__main__':
    unittest.main()
