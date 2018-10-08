"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime,
and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

Solution: 296962999629
"""
def get_primes_in_range(a, b):
    """Return all primes in the half-open interval [a, b)"""
    flags = [False, False] + [True for _ in range(2, b + 1)]
    for p in range(2, b // 2 + 1):
        for q in range(2, b // p + 1):
            flags[p * q] = False
    return [i for i, p in enumerate(flags) if p and i >= a and i < b]


def PE_49():
    """
    >>> PE_49()
    296962999629
    """
    are_permutations = lambda m, n: sorted(str(m)) == sorted(str(n))
    primes = get_primes_in_range(1000, 9999)
    for idx, initial_prime in enumerate(primes, 1):
        permutations = [initial_prime]
        for next_prime in primes[idx:]:
            if are_permutations(initial_prime, next_prime):
                permutations.append(next_prime)
        if len(permutations) == 3:
            if permutations[2] - permutations[1] == permutations[1] - permutations[0]:
                return int(''.join(map(str, permutations)))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
