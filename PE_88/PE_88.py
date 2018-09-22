#!/usr/bin/env python3.6

"""
A natural number, N, that can be written as the sum and product of a given set
of at least two natural numbers is called a product-sum number.

For example, 6 = 1 + 2 + 3 = 1 x 2 x 3

For a given set of size k we shall call we shall call the smallest N with this
property a minimal product-sum number. The minimal product-sum numbers for sets
of size, k = 2, 3, 4, 5, and 6 are as follows:

    k = 2: 4 = 2 x 2 = 2 + 2
    k = 3: 6 = 1 x 2 x 2 = 1 + 2 + 3
    k = 4: 8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
    k = 5: 8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
    k = 6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is
4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is
{4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?
"""

import operator
from functools import reduce
from math import log2

product  = lambda items: reduce(operator.__mul__, items, 1)
 
def get_values(N):
    """
    The solution for an array of length k is arrived at from the following
    observations:
        
        The array [1, ..., 1, 2, k] gives an instant P-S number of length k,
        with value 2k. We can use this as an upper bound on the solution.
        
        We have at most int(log2(2k)) non-trivial terms (a trivial term is a '1'
        as it does not contribute to the product of the terms). Else the product
        would be greater than 2k, meaning it is not the minimum solution as per
        the above.
        
        Therefore we construct sets of non-trivial terms of length int(log2(2k)).
        We increment through all candidates sets of non-trivial terms and if a
        set would give a valid solution for some k then we update the dictionary
        of recorded solutions with that solution, if smaller than the existing
        solution.
        
        Note at least two terms must be non-trivial for k >= 2. So we start with
        the small viable candidate [1, ..., 1, 2, 2].
        
    >>> get_values(6)
    30
 
    >>> get_values(12)
    61
 
    >>> get_values(60)
    890

    >>> get_values(12000)  #doctest: +SKIP
    7587457
    """
    PS_terms = {}  # define a dictionary (indexed by k) to hold all product-sum numbers formed of k terms
    non_trivial_terms = int(log2(2 * N))  # this is how many terms can have a value >= 2
    arr = [1] * (non_trivial_terms - 2) + [2, 2]  # start by checking terms [1, ..., 1, 2, 2]
    while arr is not None:
        p = product(arr)
        k = p - sum(arr) + len(arr)
        if 2 <= k and k <= N:
            PS_terms[k] = min(p, PS_terms.get(k, float("inf")))
        arr = generate_terms(arr, 2 * N)
    return sum(set(PS_terms.values()))

    
def generate_terms(terms, bound, i=-1):
    """
    Generate the next viable set of terms
    
    This is achieved by incrementing the final term by 1, and if the product of
    the terms (WLOG we can assume all terms can be presented in ascending order)
    exceeds the boundary condition then we can 'reset' the terms by moving to
    the next term, incrementing this by 1 and setting all subsequent terms to
    its value.

    >>> generate_terms([1, 1, 1, 2, 3, 20], 120)
    [1, 1, 1, 2, 4, 4]
    """
    try:
        new_terms = terms[:i] + [terms[i] + 1 for _ in range(-i)]
        if product(new_terms) <= bound:
            return new_terms
    except IndexError:
        return None
    return generate_terms(terms, bound, i - 1)

 
if __name__ == '__main__':
    import doctest; doctest.testmod()
    print(get_values(12000))

