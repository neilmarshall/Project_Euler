#! venv/bin/python3.7

"""
Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that
1219 is the smallest number such that the last digits are formed by p1 whilst
also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive
primes, p2 > p1, there exist values of n for which the last digits are formed by
p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ∑S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.

Solution: 18613426663617118
"""

from pyutils.primes import get_primes_under_n, is_prime

def PPC(p1, p2):
    """
    >>> PPC(19, 23)
    1219
    """
    period = str(p2)[-1]
    p2_copy = p2
    for position in range(len(str(p1))):
        multiplier = 1
        target_digit = str(p1)[-(position + 1)]
        rolling_digit = str(p2_copy)[-(position + 1)]
        while rolling_digit != target_digit:
            multiplier += 1
            rolling_digit = str((int(rolling_digit) + int(period)) % 10)
        p2_copy += p2 * (multiplier - 1) * 10**position
    return p2_copy


def PE134(limit):
    """
    >>> PE134(1000000)
    18613426663617118
    """
    primes = get_primes_under_n(int(limit))[2:]  # start at index 2 so p1 >= 5
    primes.append(primes[-1] + 1)
    while not is_prime(primes[-1]):
        primes[-1] += 1
    return sum(PPC(p1, p2) for p1, p2 in zip(primes, primes[1:]))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
