"""
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2    =    0.5
    1/3    =    0.(3)
    1/4    =    0.25
    1/5    =    0.2
    1/6    =    0.1(6)
    1/7    =    0.(142857)
    1/8    =    0.125
    1/9    =    0.(1)
    1/10   =    0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.

NOTES:

    For a number k to have a finite reciprocal, then k * 10^p for some p must
    result in an integer. That means k must divide 10*p, for some p. In other
    words, k must be of the form 2^a x 5^b, for some a, b.
    
    So exclude all numbers of the form 2^a x 5 ^ b.
    
    If 10^a * 1 / k - 10^b * 1 / k = 1 / k * (10^a - 10^b) is an integer then
    the period of k is equal to a - b.
    
    So for the remaining numbers, check if 10^a - 10^b is a multiple of k for
    some a, b; then the period is a - b.

Solution: 983
"""

from itertools import count

def is_power_of_2_and_5(n):
    """
    >>> is_power_of_2_and_5(36)
    False

    >>> is_power_of_2_and_5(50)
    True
    """
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    return n == 1


def get_period(n):
    """
    >>> get_period(2)
    0

    >>> get_period(3)
    1

    >>> get_period(6)
    1

    >>> get_period(7)
    6

    >>> get_period(16)
    0
    """
    if is_power_of_2_and_5(n):
        return 0
    for k in count():
        for p in range(1, n + 1):
            if (10**(k + p) - 10**k) % n == 0:
                return p


def PE_26():
    """
    >>> PE_26()
    983
    """
    periods = {n: get_period(n) for n in range(2, 1001)}
    return max(periods, key=lambda x: periods[x])


if __name__ == '__main__':
    import doctest; doctest.testmod()
