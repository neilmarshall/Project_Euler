"""
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

def PE_5(limit):
    """
    >>> PE_5(10)
    2520

    >>> PE_5(20)
    232792560
    """
    n = 0
    while True:
        n += limit
        for i in range(1, limit):
            if n % i != 0:
                break
        else:
            return n


if __name__ == '__main__':
    import doctest; doctest.testmod()
