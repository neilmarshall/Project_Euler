"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to
left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Solution: 748317
"""

class TruncatablePrimeGenerator():
    """Calling the class returns the next truncatable prime"""
    def __init__(self):
        self.primes = [2, 3, 5, 7]

    def __call__(self):
        while True:
            next_prime = self.primes[-1] + 2
            while not self._is_prime(next_prime):
                next_prime += 2
            self.primes.append(next_prime)
            if self._is_truncatable_prime(next_prime):
                return next_prime

    def _is_prime(self, n):
        if n <= self.primes[-1]:
            return n in self.primes
        for prime in self.primes:
            if prime > int(n**0.5):
                return True
            if n % prime == 0:
                return False

    def _is_truncatable_prime(self, p):
        left_truncation = right_truncation = str(p)
        for _ in range(len(str(p)) - 1):
            left_truncation, right_truncation = left_truncation[:-1], right_truncation[1:]
            if not self._is_prime(int(left_truncation)) or not self._is_prime(int(right_truncation)):
                return False
        return True


def PE_37():
    """
    >>> PE_37()
    748317
    """
    truncatable_prime_generator = TruncatablePrimeGenerator()
    return sum(truncatable_prime_generator() for _ in range(11))


if __name__ == '__main__':
    import doctest; doctest.testmod()
