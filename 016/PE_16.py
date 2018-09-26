def PE_16(n):
    """
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    
    What is the sum of the digits of the number 2^1000?

    >>> PE_16(15)
    26
    
    >>> PE_16(1000)
    1366
    """
    return sum(map(int, str(2**n)))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
