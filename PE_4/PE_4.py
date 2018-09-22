"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def find_largest_palindrome_product(digits):
    """
    >>> find_largest_palindrome_product(2)
    9009

    >>> find_largest_palindrome_product(3)
    906609
    """
    def candidates():
        for i in range (10**(digits - 1), 10**digits):
            for j in range (i, 10**digits):
                if str(i * j) == str(i * j)[::-1]:
                    yield i * j
    return max(candidates())


if __name__ == '__main__':
    import doctest; doctest.testmod()
