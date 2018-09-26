import math

def PE_20(n):
    """
    Find the sum of the digits in the number 100!

    >>> PE_20(10)
    27
    
    >>> PE_20(100)
    648
    """
    return sum(map(int, str(math.factorial(n))))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
