"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.

Answer: 100
"""

from fractions import Fraction
from itertools import product

def is_a_digit_cancelling_fraction(n0, d0):
    """
    >>> is_a_digit_cancelling_fraction(12, 20)
    False

    >>> is_a_digit_cancelling_fraction(12, 21)
    False

    >>> is_a_digit_cancelling_fraction(49, 98)
    True

    >>> is_a_digit_cancelling_fraction(49, 99)
    False
    """
    n1, d1 = str(n0), str(d0)
    for d in range(1, 10):
        while str(d) in n1 and str(d) in d1:
            n1 = n1.replace(str(d), '', 1)
            d1 = d1.replace(str(d), '', 1)
    if d1 in {'', '0'}:
        return False
    n1, d1 = int(n1), int(d1)
    return Fraction(n0, d0) == Fraction(n1, d1) and (n0 != n1 and d0 != d1)


def PE_33():
    """
    >>> PE_33()
    100
    """
    output = Fraction(1, 1)
    for numerator, denominator in product(range(10, 100), repeat=2):
        if numerator >= denominator:
            continue
        if is_a_digit_cancelling_fraction(numerator, denominator):
            output *= Fraction(numerator, denominator)
    return output.denominator


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
