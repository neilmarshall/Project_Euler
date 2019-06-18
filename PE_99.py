#! /usr/bin/env python3.7
"""
Comparing two numbers written in index form like 211 and 37 is not difficult, as
any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult,
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line, determine
which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

Solution: 709
"""
from math import log

class BaseExponentPair():

    def __init__(self, base, exponent):
        self.base, self.exponent = base, exponent
 
    def __gt__(self, other):
        return self.exponent / other.exponent * log(self.base) >= log(other.base)


def PE_99():
    """
    >>> PE_99()
    709
    """
    with open('p099_base_exp.txt') as f:
        data = [(int(base), int(exponent)) for base, exponent in (line.split(',') for line in f)]
    return data.index(max(data, key = lambda base_exponent_pair: BaseExponentPair(base_exponent_pair[0], base_exponent_pair[1]))) + 1


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True) 