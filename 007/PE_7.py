"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13. What is the 10,001st prime number?
"""

def get_target_prime(target):
    """
    >>> get_target_prime(6)
    13

    >>> get_target_prime(10001)
    104743
    """
    primes = [2]
    n = primes[-1]
    while len(primes) < target:
        n += 1
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
    return primes[-1]


if __name__ == '__main__':
    import doctest; doctest.testmod()
