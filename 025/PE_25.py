def PE_25(n):
    """
    What is the index of the first term in the Fibonacci sequence to contain n digits?

    >>> PE_25(3)
    12

    >>> PE_25(1000)
    4782
    """
    n0, n1, idx = 1, 1, 2
    while len(str(n1)) < n:
        n0, n1 = n1, n0 + n1
        idx += 1
    return idx

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
