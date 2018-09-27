"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n):
    """Return the sum of proper divisors of n"""
    return sum(p for p in range(1, n // 2 + 1) if n % p == 0)


def PE_21(limit):
    """
    Return the sum of all the amicable numbers under 'limit'

    >>> PE_21(10000)
    31626
    """
    return sum(filter(lambda n: d(n) != n and d(d(n)) == n, range(1, limit)))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
