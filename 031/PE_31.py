"""
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), £2 (200p)

It is possible to make £2 in the following way:

    1 × £1 + 1 × 50p + 2 × 20p + 1 × 5p + 1 × 2p + 3 × 1p

How many different ways can £2 be made using any number of coins?

Solution: 73682
"""

import unittest

from functools import lru_cache

@lru_cache(maxsize=None)
def make_target(n):
    """
    Return dictionary of number of ways of making the target using specified coins
    """
    if n == 1:
        return {1: 1, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100 : 0, 200: 0}
    paths = {}
    for k in [1, 2, 5, 10, 20, 50, 100, 200]:
        if k < n:
            previous_values = make_target(n - k)
            paths[k] = sum(previous_values[p] for p in [1, 2, 5, 10, 20, 50, 100, 200] if p >= k )
        elif k == n:
            paths[k] = 1
        else:
            paths[k] = 0
    return paths


class PROGRAM_TEST(unittest.TestCase):
    def test_make_target_of_1(self):
        self.assertEqual(make_target(1), {1: 1, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100 : 0, 200: 0})

    def test_make_target_of_2(self):
        self.assertEqual(make_target(2), {1: 1, 2: 1, 5: 0, 10: 0, 20: 0, 50: 0, 100 : 0, 200: 0})

    def test_make_target_of_3(self):
        self.assertEqual(make_target(3), {1: 2, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100 : 0, 200: 0})

    def test_make_target_of_10(self):
        self.assertEqual(make_target(10), {1: 8, 2: 1, 5: 1, 10: 1, 20: 0, 50: 0, 100 : 0, 200: 0})

    def test_make_target_of_20(self):
        self.assertEqual(make_target(20), {1: 34, 2: 3, 5: 2, 10: 1, 20: 1, 50: 0, 100 : 0, 200: 0})


if __name__ == '__main__':
    unittest.main(exit=False)
    print("Solution:", sum(make_target(200).values()))
