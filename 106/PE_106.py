#! venv/bin/python3.7

"""
Let S(A) represent the sum of elements in set A of size n. We shall call it a
special sum set if for any two non-empty disjoint subsets, B and C, the following
properties are true:

    i.  S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    ii. If B contains more elements than C then S(B) > S(C).

For this problem we shall assume that a given set contains n strictly increasing
elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set
for which n = 4, only 1 of these pairs need to be tested for equality (first rule).
Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be
tested for equality?

NOTE: This problem is related to Problem 103 and Problem 105.

Solution: 21384
"""

import pyximport; pyximport.install(language_level=3)
from funcs import intersection
from itertools import combinations, product


def PE_106(n):
    """
    >>> PE_106(4)
    1

    >>> PE_106(7)
    70

    >>> PE_106(12)
    21384
    """

    def comparison_needed(subset_1, subset_2):
        l1, l2 = map(len, (subset_1, subset_2))
        if l1 != l2 or l1 == 1 or l2 == 1:
            return False
        else:
            return any(s1 >= s2 for s1, s2 in zip(subset_1, subset_2))

    subsets = [s for size in range(1, n) for s in combinations(range(n), size)]
    subset_pairs = [(s1, s2) for s1, s2 in product(subsets, subsets) if s2 > s1 and not intersection(s1, s2)]
    comparison_needed_count = sum(1 for p0, p1 in subset_pairs if comparison_needed(p0, p1))

    return comparison_needed_count


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
