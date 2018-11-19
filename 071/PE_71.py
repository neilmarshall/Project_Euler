#! /usr/local/bin/python3.7
"""
Consider the fraction, n/d, where n and d are positive integers. If n < d and 
HCF(n,d) = 1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of 
size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending 
order of size, find the numerator of the fraction immediately to the left of 3/7.

Solution: 428570
"""
from fractions import Fraction

def PE_71():
    """
    >>> PE_71()
    428570
    """
    target, solution = Fraction(3, 7), Fraction(0, 1)
    for d in range(2, 1_000_000):
        current_solution = Fraction(int(d * 3 / 7), d)
        while current_solution < target:
            solution = max(solution, current_solution)
            current_solution = Fraction(current_solution.numerator + 1,
                    current_solution.denominator)
    return solution.numerator


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
