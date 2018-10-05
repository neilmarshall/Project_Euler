"""
An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression:

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

Solution: 210
"""

def champernowne(n):
    """
    Return nth digit of Champernowne's constant
    
    >>> champernowne(1)
    1
    
    >>> champernowne(9)
    9

    >>> champernowne(12)
    1

    >>> champernowne(17)
    3
    """
    digit_count, next_integer = 0, 1
    while digit_count + len(str(next_integer)) < n:
        digit_count += len(str(next_integer))
        next_integer += 1
    return int(str(next_integer)[n - digit_count - 1])


def PE_40():
    """
    >>> PE_40()
    210
    """
    product = 1
    for n in (1, 10, 100, 1000, 10000, 100000, 1000000):
        product *= champernowne(n)
    return product



if __name__ == '__main__':
    import doctest; doctest.testmod()
