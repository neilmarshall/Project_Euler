"""
The 5-digit number, 16807=7^5, is also a fifth power.

Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

Solution: 49
"""

def PE_63():
    """
    >>> PE_63()
    49
    """
    total = 0
    for x in range(1, 10):
        n = 1
        while len(str(x**n)) >= n:
            total += 1 if len(str(x**n)) == n else 0
            n += 1
    return total


if __name__ == '__main__':
   import doctest; doctest.testmod(verbose=True)
