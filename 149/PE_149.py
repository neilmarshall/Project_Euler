#! venv/bin/python3.7

"""
Looking at the table below, it is easy to verify that the maximum possible sum
 of adjacent numbers in any direction (horizontal, vertical, diagonal or 
anti-diagonal) is 16 (= 8 + 7 + 1).

    -2  5   3   2
     9 -6   5   1
     3  2   7   3
    -1  8  -4   8

Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of what
is known as a "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k^3] (modulo 1000000) − 500000.
For 56 ≤ k ≤ 4000000, sk = [s(k−24) + s(k−55) + 1000000] (modulo 1000000) − 500000.

Thus, s10 = −393027 and s100 = 86613.

The terms of s are then arranged in a 2000×2000 table, using the first 2000
numbers to fill the first row (sequentially), the next 2000 numbers to fill the
second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any
direction (horizontal, vertical, diagonal or anti-diagonal).

Solution: 52852124
"""

import numpy as np

def generate_test_matrix():
    M = [(100003 - 200003 * k + 300007 * k**3) % 1000000 - 500000 for k in range(1, 56)]
    for k in range(56, 4000001):
        M.append((M[k - 24 - 1] + M[k - 55 - 1] + 1000000) % 1000000 - 500000)
    return np.array(M).reshape(2000, 2000)


def check_matrix(M):
    '''
    >>> check_matrix(generate_test_matrix())
    52852124
    '''

    def check_subarrays(arr):
        cumulative_sums = [arr[0]]
        for i in range(1, len(arr)):
            cumulative_sums.append(arr[i] + max(0, cumulative_sums[i - 1]))
        return max(cumulative_sums)

    s, max_val = len(M), 0

    max_val = max(max_val, max(map(check_subarrays, [M[r, :] for r in range(s)])))
    max_val = max(max_val, max(map(check_subarrays, [M[:, c] for c in range(s)])))
    max_val = max(max_val, max(map(check_subarrays, [[M[i, i + d] for i in range(s - d)] for d in range(s)])))
    max_val = max(max_val, max(map(check_subarrays, [[M[i + d, i - 1] for i in range(1, s - d)] for d in range(s - 1)])))
    max_val = max(max_val, max(map(check_subarrays, [[M[i, d - i] for i in range(d + 1)] for d in range(s)])))
    max_val = max(max_val, max(map(check_subarrays, [[M[i + d, s - i] for i in range(1, s - d)] for d in range(s - 1)])))

    return max_val


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
