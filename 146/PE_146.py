#! venv/bin/python3.7
"""
The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7,
n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. The sum of all such
integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?

Solution: 676333270

    Note: current fastest time is 198 seconds in Julia (Python/Cython solution
    is 608 seconds)
"""
import unittest
from functools import reduce

from pyutils.miller_rabin import MillerRabin

def PE_146(limit):

    # define get_mods function
    def get_mods(p):
        mods = []
        for r in range(0, p):
            if all([(r**2 + a) % p != 0 for a in [1, 3, 7, 9, 13, 27]]):
                mods.append(r)
        return mods

    # establish inital variables
    solutions = []
    remainders = set()
    primes = [2, 3, 5, 7, 11]
    primes_product = reduce(lambda x, y : x * y, primes, 1)

    prime_checker = MillerRabin()

    # observe solutions mod product of initial primes must take certain values
    for r in range(0, primes_product):
        if all([r % p in get_mods(p) for p in primes]):
            remainders.add(r)

    # define is_solution function
    def is_solution(n):
        mods = []
        for a in range(1, 28):
            if prime_checker.is_prime(n**2 + a):
                mods.append(a)
        return mods == [1, 3, 7, 9, 13, 27]

    # determine eligible candidates and check if they are solutions
    for n in range(0, limit + 1, 10):
        if n % 1_000_000 == 0:
            print(f"  progress >>> {n / limit:2.1%}", end='\r')
        if n % primes_product in remainders:
            if is_solution(n):
                solutions.append(n)

    return sum(solutions)


class TestPE146(unittest.TestCase):
    def test_PE_146(self):
        self.assertEqual(PE_146(150000000), 676333270)


if __name__ == '__main__':
    unittest.main()
