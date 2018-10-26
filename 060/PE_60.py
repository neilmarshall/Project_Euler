#! venv/bin/python3.6
"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For example,
taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792,
represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

Solution: 26033
"""
from itertools import product

from pyutils.primes import get_primes_up_to_n, is_prime

def concatenated_pairs_are_prime(p1, p2):
    return is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))


def PE_60():
    """
    >>> PE_60()
    26033
    """
    
    max_prime = 9999
    
    # identify primes
    primes = get_primes_up_to_n(max_prime)
    
    # establish pairs
    pairs = []
    for p1, p2 in product(primes, primes):
        if concatenated_pairs_are_prime(p1, p2):
            pairs.append((p1, p2))

    # load pairs into triples
    triples = []
    for pair in pairs:
        p1, p2 = pair
        for p3 in primes:
            if p3 > p1 and p3 > p2:
                if (p1, p3) in pairs and (p2, p3) in pairs:
                    triples.append((p1, p2, p3))

    # load triples into quads
    quads = []
    for triple in triples:
        p1, p2, p3 = triple
        for p4 in primes:
            if p4 > p1 and p4 > p2 and p4 > p3:
                if (p1, p4) in pairs and (p2, p4) in pairs and (p3, p4) in pairs:
                    quads.append((p1, p2, p3, p4))

    # load quads into quints
    quints = []
    for quad in quads:
        p1, p2, p3, p4 = quad
        for p5 in primes:
            if p5 > p1 and p5 > p2 and p5 > p3 and p5 > p4:
                if (p1, p5) in pairs and (p2, p5) in pairs and (p3, p5) in pairs and (p4, p5) in pairs:
                    quints.append((p1, p2, p3, p4, p5))

    # return minimum sum of quints
    return min(sum(quint) for quint in quints)


if __name__ == '__main__':
    import doctest; doctest.testmod()
