"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.

Solution: 142857
"""

from itertools import count

def PE_52():
    """
    >>> PE_52()
    142857
    """
    are_permutations = lambda m, n: sorted(str(m)) == sorted(str(n))
    for n in count(1):
        if all(are_permutations(n, m * n) for m in range(2, 7)):
            return n


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
