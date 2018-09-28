"""
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:

    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97

How many circular primes are there below one million?
"""

import unittest

def is_prime(n):
    """Return primality of n"""
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            return False
    return True


def is_circular_prime(n):
    """Return circular primality of n"""
    s = str(n)
    for _ in range(len(s)):
        if not is_prime(int(s)):
            return False
        s = s[1:] + s[0]
    return True


def PE_35(n):
    """Return number of circular primes less than n"""
    return sum(1 for n in range(2, n) if is_circular_prime(n))


class TestPE35(unittest.TestCase):
    def test_100_returns_13(self):
        self.assertEqual(PE_35(100), 13)

    def test_1000000_returns_55(self):
        self.assertEqual(PE_35(1000000), 55)


if __name__ == '__main__':
    unittest.main()
