"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

def PE_2():
    """
    >>> PE_2()
    4613732
    """
    def generate_limited_fibs(limit):
        n0, n1 = 0, 1
        while n1 < limit:
            yield n1
            n0, n1 = n1, n0 + n1
    return sum(filter(lambda x: x % 2 == 0, generate_limited_fibs(4e6)))


if __name__ == '__main__':
    import doctest; doctest.testmod()

