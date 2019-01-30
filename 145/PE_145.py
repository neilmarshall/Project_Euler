#! /usr/bin/env python3.7

"""
Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and
409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and
904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?

Solution: 608720
"""

def is_reversible(n):
    if str(n)[0] == '0' or str(n)[-1] == '0':
        return False
    test_string = str(n + int(str(n)[::-1]))
    return all(int(char) % 2 != 0 for char in test_string)


def reversible_numbers(limit):
    """
    >>> reversible_numbers(1000)
    120

    >>> reversible_numbers(100000000)
    608720
    """
    return sum(1 for n in range(1, limit) if is_reversible(n))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
