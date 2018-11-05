import unittest

from pyutils.miller_rabin import miller_rabin_test
from pyutils.primes import get_primes_under_n

class TestMillerRabin(unittest.TestCase):

    def test_miller_rabin_produces_primes_under_100(self):
        miller_rabin_output = [n for n in range(100) if miller_rabin_test(n)]
        primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, \
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(miller_rabin_output, primes_under_100)

    def test_miller_rabin_produces_sum_of_primes_under_1000(self):
        miller_rabin_output = sum(n for n in range(1000) if miller_rabin_test(n))
        self.assertEqual(miller_rabin_output, sum(get_primes_under_n(1000)))
