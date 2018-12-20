#! venv/bin/python3.7
"""
It is well known that if the square root of a natural number is not an integer,
then it is irrational. The decimal expansion of such square roots is infinite
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the
first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of
the first one hundred decimal digits for all the irrational square roots.

Solution: 40886
"""
from pyutils.sqrt_expansion import SqrtExpansion

def sum_expansion_digits(n, limit=100):
    """
    >>> sum_expansion_digits(2)
    475
    """
    def unpack(fraction):
        return fraction.numerator, fraction.denominator
    def get_digits(expansion, k=1):
        n, d = unpack(expansion.get_nth_fraction(k))
        return (n, d) if len(str(n)) >= limit else get_digits(expansion, k + 1)
    try:
        n, d = get_digits(SqrtExpansion(n))
        return sum(map(int, str(n * 10**limit // d)[:limit]))
    except ValueError:
        return 0


def PE_80():
    """
    >>> PE_80()
    40886
    """
    return sum(sum_expansion_digits(n) for n in range(1, 101))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
