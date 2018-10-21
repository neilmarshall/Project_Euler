#! /usr/bin/env python3.6
"""
It is possible to show that the square root of two can be expressed as an
infinite continued fraction:

    √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?

Solution: 153
"""

def PE_57(problemlimit):
    """
    >>> PE_57(1000)
    153
    """
    excess_digit_count = 0
    numerator, denominator = 0, 1
    for i in range(1, problemlimit):
        numerator, denominator = denominator, numerator + denominator * 2
        if len(str(numerator + denominator)) > len(str(denominator)):
            excess_digit_count += 1
    
    return excess_digit_count
    

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
