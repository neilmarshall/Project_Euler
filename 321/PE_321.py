#! venv/bin/python3.7
"""
A horizontal row comprising of 2n + 1 squares has n red counters placed at one
end and n blue counters at the other end, being separated by a single empty
square in the centre. For example, when n = 3.

A counter can move from one square to the next (slide) or can jump over another
counter (hop) as long as the square next to that counter is unoccupied.

Let M(n) represent the minimum number of moves/actions to completely reverse
the positions of the coloured counters; that is, move all the red counters to 
the right and all the blue counters to the left.

It can be verified M(3) = 15, which also happens to be a triangle number.

If we create a sequence based on the values of n for which M(n) is a triangle
number then the first five terms would be: 

    1, 3, 10, 22, and 63, and their sum would be 99.

Find the sum of the first forty terms of this sequence.

NOTES:

    Solutions for the first 18 terms are as follows:

        [1, 3, 10, 22, 63, 133, 372, 780, 2173, 4551, 12670, 26530, 73851,
         154633, 430440, 901272, 2508793, 5253003]

    These can be presented along with differences as follows:

        n   p(n)    f(n)    g(n)
        1   1       n/a     n/a
        2   3       2       n/a
        3   10      7       5
        4   22      12      5
        5   63      41      29
        6   133     70      29
        7   372     239     169
        8   780     408     169
        9   2173    1393    985
        10  4551    2378    985

    Each first difference (denoted g(n)) can be calculated as follows:

        if n <= 1:  2
        if n >= 2:  f(n - 1) + g(n)

    Each second difference (denoted g(n)) can be calculated as follows:

        if n <= 1:      1
        if n % 2 == 0:  g(n - 1)
        if n % 2 != 0:  int(g(n - 2) * (3 + sqrt(8)))

SOLUTION: 2470433131948040
"""
from math import sqrt

def PE_321(terms):
    """
    >>> PE_321(5)
    99

    >>> PE_321(40)
    2470433131948040
    """
    def p(n):
        return p(n - 1) + f(n) if n > 1 else 1
    def f(n):
        return f(n - 1) + g(n) if n >= 3 else 2
    def g(n):
        if n <= 1:
            return 1
        if n % 2 == 0:
            return g(n - 1)
        return int(g(n - 2) * (3 + sqrt(8)))
    return sum(p(n) for n in range(1, terms + 1))

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
