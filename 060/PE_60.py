#! venv/bin/python3
"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For example,
taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792,
represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate
to produce another prime.

Solution: 26033
"""
from itertools import combinations, permutations

from pyutils.miller_rabin import Miller_Rabin

def all_concatenations_are_prime(iterable):
    mr = Miller_Rabin()
    pairs = permutations(iterable, 2)
    for pair in pairs:
        if not mr.is_prime(int(''.join(map(str, pair)))):
            return False
    return True


def get_next_layer(current_layer, primes, pairs):
    next_layer = set()
    for prime in primes:
        for elements in current_layer:
            if prime <= max(elements):
                continue
            if all((element, prime) in pairs for element in elements):
                next_layer.add((*elements, prime))
    return next_layer


def PE_60():
    """
    >>> PE_60()
    26033
    """
    primes = get_primes_up_to_n(9999)
    primes = [primes[1]] + primes[3:]  # remove 2 and 5 as any concatenated number ending in 2 or 5 will not be prime
 
    pairs = {pair for pair in combinations(primes, 2) if all_concatenations_are_prime(pair, primes)}
    triples = get_next_layer(pairs, primes, pairs)
    quads = get_next_layer(triples, primes, pairs)
    quints = get_next_layer(quads, primes, pairs)

    return min(sum(quint) for quint in quints)


if __name__ == '__main__':
    import doctest; doctest.testmod()
