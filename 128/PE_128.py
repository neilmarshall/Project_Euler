#! /usr/bin/env python3.7
"""
A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles,
starting at "12 o'clock" and numbering the tiles 2 to 7 in an anti-clockwise
direction.

New rings are added in the same fashion, with the next rings being numbered 8 to
19, 20 to 37, 38 to 61, and so on.

By finding the difference between tile n and each of its six neighbours we shall
define PD(n) to be the number of those differences which are prime.

For example, working clockwise around tile 8 the differences are 12, 29, 11,
6, 1, and 13. So PD(8) = 3.

In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10,
hence PD(17) = 2.

It can be shown that the maximum value of PD(n) is 3.

If all of the tiles for which PD(n) = 3 are listed in ascending order to form a
sequence, the 10th tile would be 271.

Find the 2000th tile in this sequence.

Solution: 14516824220
"""

def prime_indicator(limit):
    p_indicator = [False, False] + [True for p in range(2, limit + 1)]
    for i in range(2, (limit + 1) // 2 + 1):
        for j in range(2, limit // i + 1):
            p_indicator[i * j] = False
    return p_indicator


def main(limit):
    """
    >>> main(10)
    271
    
    >>> main(20)
    5677
    
    >>> main(2000)
    14516824220
    """
    prime_limit = 1000
    p_indicator = prime_indicator(prime_limit)
    PD_3s = [1, 2]
    n = 8
    l = 6
    while len(PD_3s) < limit:
        if (prime_limit < 2 * l + 17):
            prime_limit *= 2
            p_indicator = prime_indicator(prime_limit)
        diffs = [l + 5, l + 7, 2 * l + 17]
        if all(p_indicator[diffs[i]] for i in (0, 1, 2)):
            PD_3s.append(n)
        if n - 1 != 7:
            diffs = [l - 1, l + 5, 2 * l - 7]
            if all(p_indicator[diffs[i]] for i in (0, 1, 2)):
                PD_3s.append(n - 1)
        l += 6
        n += l
    return sorted(PD_3s)[-1]


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
