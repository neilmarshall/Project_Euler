#! venv/bin/python3
"""
The square root of 2 can be written as an infinite continued fraction: √2 = [1;(2)], (2),
where (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots
provide the best rational approximations.

Hence the sequence of the first ten convergents for √2 are:

    1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant:

    e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17.

Find the sum of digits in the numerator of the 100th convergent of the continued
fraction for e.

Solution: 272
"""
from pyutils.sqrt_expansion import SqrtExpansion

def PE_65(problemlimit):
    """
    >>> PE_65(10)
    17

    >>> PE_65(100)
    272
    """
    key = [_] + [1 for _ in range(problemlimit - 1)]
    for n in range(problemlimit):
        if (n + 1) % 3 == 0:
            key[n] *= 2 * (n + 1) // 3

    expansion = SqrtExpansion(2, key[1:])
    
    return sum(map(int, str(expansion.get_nth_fraction(problemlimit).numerator)))
    

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
