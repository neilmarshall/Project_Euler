#! venv/bin/python3.7
"""
Using all of the digits 1 through 9 and concatenating them freely to form
decimal integers, different sets can be formed. Interestingly with the set
{2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly
once contain only prime elements?

Solution: 44680
"""

from itertools import permutations
from pyutils.miller_rabin import MillerRabin

mr = MillerRabin()

ALLOWABLE_ENDINGS = {1, 2, 3, 5, 7, 9}  # single-digit primes and possible end-digits for primes

def add_prime_set(PD, breaks, unique_prime_sets):
    prime_set = []
    if len(breaks) == 1:
        prime = ""
        for element in PD[breaks[0]:]:
            prime += str(element)
        prime_set.append(int(prime))
        prime = ""
        for element in PD[:breaks[-1]]:
            prime += str(element)
        prime_set.append(int(prime))
    else:
        prime = ""
        for element in PD[breaks[0]:]:
            prime += str(element)
        prime_set.append(int(prime))
        for i in range(len(breaks) - 1):
            prime = ""
            for element in PD[breaks[i + 1]:breaks[i]]:
                prime += str(element)
            prime_set.append(int(prime))
        prime = ""
        for element in PD[:breaks[-1]]:
            prime += str(element)
        prime_set.append(int(prime))
    if tuple(sorted(prime_set)) not in unique_prime_sets:
        unique_prime_sets.add(tuple(sorted(prime_set)))
    return


def generate_prime_sets(PD, unique_prime_sets):
    cp = 8  # cp = 'current position' in the tuple PD
    n = PD[cp]
    breaks = []
    ineligible_primes = []
    master_ineligible_primes = []
    while cp >= 0:    
        if cp == 0 and mr.is_prime(n):
            add_prime_set(PD, breaks, unique_prime_sets)
            ineligible_prime = ""
            for element in (PD[breaks[-1]:breaks[-2]]
                            if len(breaks) > 1
                            else PD[breaks[-1]:]):
                ineligible_prime = ineligible_prime + str(element)
            master_ineligible_primes.append(int(ineligible_prime))
            ineligible_primes = master_ineligible_primes
            breaks = []
            cp = 8
            n = PD[cp]
        elif cp == 0 and not mr.is_prime(n):
            ineligible_prime = ""
            for element in (PD[breaks[-1]:breaks[-2]]
                            if len(breaks) > 1
                            else PD[breaks[-1]:]):
                ineligible_prime = ineligible_prime + str(element)
            ineligible_primes.append(int(ineligible_prime))
            del breaks[-1]
            cp = breaks[-1] - 1 if len(breaks) > 0 else 8
            n = PD[cp]
        elif (mr.is_prime(n)
              and (PD[cp - 1] in ALLOWABLE_ENDINGS )
              and (n not in ineligible_primes)):
            breaks.append(cp)
            cp -= 1
            n = PD[cp]
        else:
            cp -= 1
            n = int(str(PD[cp]) + str(n))
            if len(str(n)) == 9:
                return


def PE_118():
    """
    >>> PE_118()
    44680
    """
    unique_prime_sets = set()
    PDs = (n for n in permutations(range(1, 10)) if (n[-1] in ALLOWABLE_ENDINGS))
    for PD in PDs:
        generate_prime_sets(PD, unique_prime_sets)
    return len(unique_prime_sets)


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
