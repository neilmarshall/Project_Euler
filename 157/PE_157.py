def solve(n):
    """
    >>> solve(1)
    20

    >>> solve(2)
    102

    >>> solve(3)
    356

    >>> solve(4)
    958

    >>> solve(5)
    2192
    """
    infer = lambda p, a: (10**n * a) / (p * a - 10**n)
    def solve_for_a(a):
        solutions = 0
        p = int(10**n / a) + 1
        b = infer(p, a)
        while b >= a:
            if (abs(int(b) - b) == 0):
                solutions += 1
            p += 1
            b = infer(p, a)
        return solutions
    a = 1
    solutions = 0
    while True:
        solutions += solve_for_a(a)
        a += 1
        p = int(10**n / a) + 1
        b = infer(p, a)
        if b < a:
            break
    return solutions

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
