from math import floor, log

from pyutils.primes import get_primes_up_to_n

class MillerRabin():
    """
    Miller-Rabin primality test

    Deterministic implementation of Miller-Rabin primality test, based on
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

    Class loads primes below 5,000. For given n, assuming n odd (returning False
    if n is not 2 otherwise), trial division is first attempted versus these
    initial primes.

    If trial division fails to identify primality, the full Miller-Rabin algorithm
    is employed, with witnesses chosen based on the value of n.

    Empirically, the MillerRabin class appears to out-perform trial division for
    primes larger than 1,000,000 (trial division tested all primes up to 1,000,000
    in just over 6s; Miller-Rabin achieved the same in just under 6s).
    """
    def __init__(self):
        self.known = get_primes_up_to_n(5000)

    def is_prime(self, n):
        """
        Return primality of n
        
        Uses trial division for small n and Miller-Rabin for larger values.
        """
        # discount even numbers
        if n <= 2 or n % 2 == 0:
            return n == 2

        # perform trial division based on initial primes
        for p in self.known:
            if n % p == 0:
                return n == p

        # test compositeness using Miller-Rabin algorithm, with suitable witnesses
        if n < 2047:
            witnesses = [2]
        elif n < 1373653:
            witnesses = [2, 3]
        elif n < 9080191:
            witnesses = [31, 73]
        elif n < 25326001:
            witnesses = [2, 3, 5]
        elif n < 3215031751:
            witnesses = [2, 3, 5, 7]
        elif n < 4759123141:
            witnesses = [2, 7, 61]
        elif n < 1122004669633:
            witnesses = [2, 13, 23, 1662803]
        elif n < 2152302898747:
            witnesses = [2, 3, 5, 7, 11]
        elif n < 3474749660383:
            witnesses = [2, 3, 5, 7, 11, 13]
        elif n < 341550071728321:
            witnesses = [2, 3, 5, 7, 11, 13, 17]

        s, d = self._factorise_powers_of_two(n)
        for a in witnesses:
            if pow(a, d, n) != 1:
                if all(pow(a, pow(2, r) * d, n) != n - 1 for r in range(s)):
                    return False
        return True

    def _factorise_powers_of_two(self, n):
        s, m = 0, n - 1
        while m % 2 == 0:
            s += 1
            m >>= 1
        d = n >> s
        return s, d
