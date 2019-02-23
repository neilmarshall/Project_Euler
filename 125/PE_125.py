#! /usr/bin/env python3.7
"""
The palindromic number 595 is interesting because it can be written as the sum
of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as
consecutive square sums, and the sum of these palindromes is 4164. Note that
1 = 0^2 + 1^2 has not been included as this problem is concerned with the
squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can
be written as the sum of consecutive squares.

Solution: 2906969179
"""

from itertools import count

def PE_125(limit):
    """
    >>> PE_125(1e8)
    2906969179
    """
    sums_of_squares = set()
    for i in range (1, int(limit**0.5) + 1):
        square_sum = i**2
        for j in count(i + 1):
            square_sum += j**2
            if square_sum > limit:
                break
            sums_of_squares.add(square_sum)
    return sum(filter(lambda n: str(n) == str(n)[::-1], sums_of_squares))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
