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
