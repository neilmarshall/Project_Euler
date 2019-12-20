"""
Each positive integer has up to eight neighbours in the triangle.

A set of three primes is called a prime triplet if one of the three primes has the other
two as neighbours in the triangle.

For example, in the second row, the prime numbers 2 and 3 are elements of some prime triplet.

If row 8 is considered, it contains two primes which are elements of some prime triplet, i.e. 29 and 31.
If row 9 is considered, it contains only one prime which is an element of some prime triplet: 37.

Define S(n) as the sum of the primes in row n which are elements of any prime triplet.
Then S(8)=60 and S(9)=37.

You are given that S(10000)=950007619.

Find  S(5678027) + S(7208785).

Solution:
    79697256800321526 + 242605983970758409 = 322303240771079935
"""

from functools import partial
from multiprocessing import Pool

from nmutils.miller_rabin import MillerRabin

def get_primes_parallel(lower, upper):
    """Returns sequence of all primes between lower and upper inclusive"""
    mr = MillerRabin()
    with Pool() as pool:
        return (p for p, flag in enumerate(pool.map(mr.is_prime, range(lower, upper + 1)), lower) if flag)

def PE_196(row):
    """
    >>> PE_196(8)
    60

    >>> PE_196(9)
    37

    >>> PE_196(1000)
    3500211

    >>> PE_196(10000)
    950007619

    >>> PE_196(5678027)
    79697256800321526

    >>> PE_196(7208785)
    242605983970758409
    """
    def T(k):
        return k * (k - 1) // 2
    def is_prime_triplet(row, n):
        def get_neighbours(row, n):
            lower_bound, upper_bound = 1 + T(row), row + T(row)
            if n < lower_bound or n > upper_bound:
                raise ValueError("invalid arguments")
            def neighbours():
                # previous row
                for t in (n - row, n - row + 1, n - row + 2):
                    if t >= 1 + T(row - 1) and t <= lower_bound - 1:
                        yield (row - 1, t)

                # current row
                for t in (n - 1, n + 1):
                    if t >= lower_bound and t <= upper_bound:
                        yield (row, t)

                # subsequent row
                for t in (n + row - 1, n + row, n + row + 1):
                    if t >= upper_bound + 1 and t <= upper_bound + row + 1:
                        yield (row + 1, t)

            for r, t in neighbours():
                if t in primes[r]:
                    yield (r, t)
        if n in primes[row]:
            neighbours = list(get_neighbours(row, n))
            if len(neighbours) == 0:
                return False
            elif len(neighbours) >= 2:
                return True
            else:
                def get_extended_neighbours(neighbours):
                    for row, neighbour in neighbours:
                        yield from get_neighbours(row, neighbour)
                return len(list(get_extended_neighbours(neighbours))) >= 2
        else:
            return False
    if row < 3:
        raise ValueError("n cannot be less than 3")
    primes = {k: set(get_primes_parallel(T(k) + 1, T(k + 1))) for k in range(row - 2, row + 3)}
    return sum(filter(partial(is_prime_triplet, row), primes[row]))

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
