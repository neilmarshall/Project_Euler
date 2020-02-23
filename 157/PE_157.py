#! venv/bin/python3

import os
from concurrent.futures import ProcessPoolExecutor

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
    print(f"Calculating solutions for {n} on process {os.getpid()}...")
    infer = lambda p, a: int((10**n * a) / (p * a - 10**n))
    def solve_for_a(a):
        check_solution = lambda b: 10**n * (a + b) % (a * b) == 0
        solutions = set()
        p = int(10**n / a) + 1
        b = infer(p, a)
        while b >= a:
            if check_solution(b):
                solutions.add((a, b))
            p += 1
            b = infer(p, a)
        return len(solutions)
    a = 1
    solutions = 0
    while True:
        solutions += solve_for_a(a)
        a += 1
        p = int(10**n / a) + 1
        b = infer(p, a)
        if b < a:
            break
    print(f"{n}: {solutions}")
    return solutions    

if __name__ == '__main__':
    #import doctest; doctest.testmod(verbose=True)
    with ProcessPoolExecutor() as pool:
        solutions = pool.map(solve, range(1, 10))
        print(f"Total: {sum(solutions)}")
