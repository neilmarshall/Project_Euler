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
    if row < 3:
        raise ValueError("n cannot be less than 3")
    def is_prime_triplet(row, n):
        def get_neighbours(row, n):
            lowerBound = 1 + T(row)
            upperBound = row + T(row)
            if n < lowerBound or n > upperBound:
                raise ValueError("invalid arguments")
            previousRowLowerBound = 1 + T(row - 1)
            previousRowUpperBound = lowerBound - 1
            subsequentRowLowerBound = upperBound + 1
            subsequentRowUpperBound = subsequentRowLowerBound + row
            def neighbours():
                # previous row
                t = n - row
                if t >= previousRowLowerBound and t <= previousRowUpperBound:
                    yield (t, row - 1)
                t = n - row + 1
                if t >= previousRowLowerBound and t <= previousRowUpperBound:
                    yield (t, row - 1)
                t = n - row + 2
                if t >= previousRowLowerBound and t <= previousRowUpperBound:
                    yield (t, row - 1)

                # current row
                t = n - 1
                if t >= lowerBound and t <= upperBound:
                    yield (t, row)
                t = n + 1
                if t >= lowerBound and t <= upperBound:
                    yield (t, row)

                # subsequent row
                t = n + row - 1
                if t >= subsequentRowLowerBound and t <= subsequentRowUpperBound:
                    yield (t, row + 1)
                t = n + row
                if t >= subsequentRowLowerBound and t <= subsequentRowUpperBound:
                    yield (t, row + 1)
                t = n + row + 1
                if t >= subsequentRowLowerBound and t <= subsequentRowUpperBound:
                    yield (t, row + 1)

            for t, r in neighbours():
                if t in primes[r]:
                    yield (t, r)
        if n in primes[row]:
            neighbours = list(get_neighbours(row, n))
            if len(neighbours) == 0:
                return False
            elif len(neighbours) >= 2:
                return True
            else:
                def extendedNeighbours(neighbours):
                    for neighbour, row in neighbours:
                        yield from get_neighbours(row, neighbour)
                return len(list(extendedNeighbours(neighbours))) >= 2
        else:
            return False
    def T(k):
        return k * (k - 1) // 2
    primes = {k: set(get_primes_parallel(T(k) + 1, T(k + 1))) for k in range(row - 2, row + 3)}
    return sum(filter(partial(is_prime_triplet, row), primes[row]))

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
