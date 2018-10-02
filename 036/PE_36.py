"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)


SOLUTION: 872187
"""

def is_double_base_palindrome(n):
    """
    Return whether a number is palindromic is both base 2 and base 10

    >>> is_double_base_palindrome(585)
    True

    >>> is_double_base_palindrome(583)
    False

    >>> is_double_base_palindrome(17)
    False
    """
    def is_base_10_palindrome(n):
        return str(n) == str(n)[::-1]
    def is_base_2_palindrome(n):
        s = str(bin(n))[2:]
        return s == s[::-1]
    return is_base_10_palindrome(n) and is_base_2_palindrome(n)


def PE_36():
    """
    >>> PE_36()
    872187
    """
    return sum(filter(is_double_base_palindrome, range(1 ,1000000)))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
