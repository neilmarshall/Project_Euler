"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family:

    56003
    56113
    56333
    56443
    56663
    56773
    56993

Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

from itertools import combinations

def get_primes_in_range(digits):
    """
    Return list of all primes of specified number of digits
 
    >>> primes = get_primes_in_range(1)
    >>> [min(primes), max(primes), len(primes)]
    [2, 7, 4]
 
    >>> primes = get_primes_in_range(2)
    >>> [min(primes), max(primes), len(primes)]
    [11, 97, 21]
    """
    limit = 10**digits
    flags = [False, False] + [True for _ in range(limit)]
    for p in range(2, limit // 2 + 1):
        for q in range(2, limit // p + 1):
            flags[p * q] = False
    return [p for p in range(limit // 10, limit) if flags[p]]
 
 
def get_index_combinations(n):
    """
    Return list of all combinations of indices of length 1, ..., n - 1
 
    >>> sorted(get_index_combinations(5))
    [(0,), (0, 1), (0, 1, 2), (0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 3), \
     (0, 1, 3, 4), (0, 1, 4), (0, 2), (0, 2, 3), (0, 2, 3, 4), (0, 2, 4), \
     (0, 3), (0, 3, 4), (0, 4), (1,), (1, 2), (1, 2, 3), \
     (1, 2, 3, 4), (1, 2, 4), (1, 3), (1, 3, 4), (1, 4), \
     (2,), (2, 3), (2, 3, 4), (2, 4), (3,), (3, 4), (4,)]
    """
    return {idx for r in range(1, n) for idx in combinations(range(n), r)}
 
 
def swap_digits(n, indices, replacement_digit):
    """
    Return number with digits at specified indices replaced with specified replacement digit
   
    >>> swap_digits(12345, (0,), 7)
    72345
 
    >>> swap_digits(12345, (1, 2), 8)
    18845
 
    >>> swap_digits(12345, (2, 3, 4), 9)
    12999
    """
    return int(''.join(str(replacement_digit) if i in indices else str(n)[i] for i in range(len(str(n)))))
 
 
def get_smallest_prime_in_family(family_size, seed=1):
    """
    Return smallest prime such that there are family_size such primes obtained
    by replacing digits
 
    >>> get_smallest_prime_in_family(6)
    13
 
    >>> get_smallest_prime_in_family(7)
    56003
 
    >>> get_smallest_prime_in_family(8)
    121313
    """
    def check_solution(family_size, n):
        """Check if there exist family_size solutions that are all n digits in length"""
        primes = set(get_primes_in_range(n))  # convert to set for ease of checking inclusion
        index_combinations = get_index_combinations(n)
        for base_prime in sorted(primes):
            for indices in index_combinations:
                if len({str(base_prime)[i] for i in indices}) != 1:  # this checks that the base prime is of the correct form (i.e. identical digits at the specified indices)
                    continue
                test_primes = {swap_digits(base_prime, indices, digit) for digit in range(10)}
                if len(test_primes & primes) == family_size:
                    return base_prime
        return None
    return check_solution(family_size, seed) or get_smallest_prime_in_family(family_size, seed + 1)
 
 
if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)

