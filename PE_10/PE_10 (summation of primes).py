"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def sum_of_primes(limit):
    """
    >>> sum_of_primes(10)
    17

    >>> sum_of_primes(2000000)
    142913828922
    """
    indicators = [False, False] + [True for _ in range (2, limit + 1)]
    for i in range(2, limit // 2 + 1):
        for j in range(2, limit // i + 1):
            indicators[i * j] = False
    return sum(p for p, indicator in enumerate(indicators) if indicator)


if __name__ == '__main__':
    import doctest; doctest.testmod()
