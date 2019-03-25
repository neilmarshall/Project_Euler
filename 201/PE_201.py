#! /usr/local/bin/python3.7

from functools import lru_cache
from itertools import combinations

def U(A, k):
    """
    >>> U({1, 3, 6, 8, 10, 11}, 3)
    156
    """
    subsets = combinations(A, 3)
    subset_counts = [sum(subset) for subset in subsets]
    unique_subset_counts = [subset_count for subset_count in subset_counts if subset_counts.count(subset_count) == 1]
    return sum(unique_subset_counts)


@lru_cache(maxsize=None)
def nU(A, k, print_flag=False):
    """
    Return set of all sums of k-digit subsets of A

    >>> sorted(nU({1, 3, 6, 8, 10, 11}, 3))
    [10, 12, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 27, 29]

    >>> nU(frozenset(range(100)), 50, True)
    None
    """
    if k == 1:
        return A
    subsets, A = frozenset(), sorted(A)
    for j in range(len(A) - 1):
        if print_flag:
            print(j)
        subset = {A[j] + s for s in nU(frozenset(A[j + 1:]), k - 1)}
        subsets = frozenset(subsets | subset)
    return subsets


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
