#!/usr/bin/env python3.7
"""
A row measuring n units in length has red blocks with a minimum length of m
units placed on it, such that any two red blocks (which are allowed to be
different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a row
can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for which
the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and
F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count
function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first
exceeds one million.

Solution: 168
"""
from itertools import count, dropwhile, islice

def PE115(m, limit):
    """
    >>> PE115(50, 1000000)
    168
    """
    def extend(block_counter, m, n):
        triangle = lambda x: x * (x + 1) // 2
        new_block = [1, triangle(n - m + 1)]
        block_count = (n + 1) // (m + 1) + 1
        j = 2
        while len(new_block) < block_count:
            if (block_count == (n + 1) / (m + 1) + 1) and (len(new_block) == block_count - 1):
                new_element = 1
            else:
                new_element = block_counter[n - 1][j] + sum(block_counter[i][j - 1] for i in range(1, n - m) if len(block_counter[i]) > j - 1)
                j += 1
            new_block.append(new_element)
        block_counter.append(new_block)

    def F(m, n):
        block_counter = [[] for _ in range(m)] + [[1, 1]]
        while len(block_counter) <= n:
            extend(block_counter, m, len(block_counter))
        return sum(block_counter[n])

    return list(islice(dropwhile(lambda f: f[1] <= limit, enumerate(map(lambda n: F(m, n), count(m)), m)), 1))[0][0]


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
