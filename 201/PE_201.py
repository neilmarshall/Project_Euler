#! /usr/local/bin/python3.7

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


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
