#! venv/bin/python3
"""
All square roots are periodic when written as continued fractions.

[***See full problem desciption for explanation of shorthand notation***]

The first ten continued fraction representations of (irrational) square roots are:

    √2 = [1;(2)], period = 1
    √3 = [1;(1,2)], period = 2
    √5 = [2;(4)], period = 1
    √6 = [2;(2,4)], period = 2
    √7 = [2;(1,1,1,4)], period = 4
    √8 = [2;(1,4)], period = 2
    √10 = [3;(6)], period = 1
    √11 = [3;(3,6)], period = 2
    √12 = [3;(2,6)], period = 2
    √13 = [3;(1,1,1,1,6)], period = 5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?

Solution: 1322
"""
from pyutils.sqrt_expansion import SqrtExpansion

def PE_64(limit):
    """
    >>> PE_64(10000)
    1322
    """
    count = 0
    for n in range(2, limit + 1):
        try:
            expansion = SqrtExpansion(n)
            period = len(expansion.key)
            if period % 2 != 0:
                count += 1
        except ValueError:
            pass
    return count


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
