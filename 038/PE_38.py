"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9
and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

NOTES:

    Since n > 1, we will be concatenating an integer with a tuple at least
    equal to (1, 2) - so the integer cannot be greater than 4 digits in length,
    i.e. it must be no greater than 9,999.
    
    So we check each integer from 1 to 9,999. For each integer, consecutively
    check if integer x n (starting from n = 1) contains previously seen digits,
    and if not if the concatenated products are 1-through-9 pandigital.

Solution: 932718654
"""

from itertools import count

def PE_38():
    """
    >>> PE_38()
    932718654
    """
    def is_pandigital(number):
        return len(number) == 9 and set(str(number)) == set('123456789')
    def generate_pandigital_number(base):
        observed_digits, concatenated_products = set(), ''
        for n in count(1):
            product = str(base * n)
            if observed_digits.isdisjoint(set(product)):
                observed_digits |= set(product)
                concatenated_products += product
                if is_pandigital(concatenated_products):
                    return int(concatenated_products)
            else:
                return None
    pandigital_numbers = set()
    for base in range(1, 9999):
        pandigital_number = generate_pandigital_number(base)
        if pandigital_number is not None:
            pandigital_numbers.add(pandigital_number)
    return max(pandigital_numbers)


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
