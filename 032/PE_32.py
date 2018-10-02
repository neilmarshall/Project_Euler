"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand / multiplier / product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

NOTES:

    The largest 2-digit numbers we could have as multiplicand / multiplier can
    be 99, largest product therefore 99 x 99 = 9801, which has less
    than 9 - 2 - 2 = 5 digits. So one of multiplicand / multiplier must have at
    least 3 digits.

    The smallest 5-digit number we could have as multiplicand / multiplier can
    be 12345, smallest product therefore 12345 x 6 = 74070, which has more
    than 9 - 5 - 1 = 3 digits. So multiplicand / multiplier cannot have more
    than 4 digits each.

    Combining the above, we must have a 3-digit or 4-digit multiplicand.
    
    If we have a 3-digit multiplicand then the multiplier can be at most 2
    digits, and not less than 2 digits (as 999 x 9 only gives a 4-digit number).

    If we have a 4-digit multiplicand then the multiplier can be at most 1 digit.

    So for each [3 / 4]-digit permutation (without replacement) and then for each
    [2 / 1]-digit permutation respectively (from the remaining digits, without
    replacement), check if the product results in a pandigital set.

Answer: 45228
"""

from itertools import chain, permutations

def PE_32():
    """
    >>> PE_32()
    45228
    """
    product_sum, digits = set(), '123456789'
    for multiplicand in chain(permutations(digits, 3), permutations(digits, 4)):
        remaining_digits = ''.join(x for x in digits if x not in multiplicand)
        for multiplier in permutations(remaining_digits, 5 - len(multiplicand)):
            multiplicand, multiplier = map(lambda x: ''.join(x), (multiplicand, multiplier))
            product = int(multiplicand) * int(multiplier)
            if ''.join(sorted(multiplicand + multiplier + str(product))) == digits:
                product_sum.add(product)
    return sum(product_sum)


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
