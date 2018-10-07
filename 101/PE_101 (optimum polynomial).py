import numpy as np

def sum_of_FITs():
    """
    >>> sum_of_FITs()
    37076114526
    """
    u = lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
    FIT_sum = 0
    for k in range(1, 11):
        OP = [u(n) for n in range (1, k + 1)]
        C_inverse = np.linalg.inv([[n**(k - 1) for k in range(1, k + 1)] for n in range (1, k + 1)])
        A = [sum(C_inverse[i][j] * OP[j] for j in range(len(C_inverse[i]))) for i in range(len(C_inverse))]
        FIT = sum(A[coefficient] * (k + 1)**coefficient for coefficient in range(len(A)))
        if FIT != u(k + 1):
            FIT_sum += int(round(FIT))
    return FIT_sum

if __name__ == '__main__':
    import doctest; doctest.testmod()
