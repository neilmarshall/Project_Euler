#! /usr/bin/env python3.7
"""
We shall call a positive integer A an "Alexandrian integer", if there exist
integers p, q, r such that:

    A = p . q . r, and 1 / A = 1 / p + 1 / q + 1 / r

For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18). In fact,
630 is the 6th Alexandrian integer, the first 6 Alexandrian integers being:

    6, 42, 120, 156, 420 and 630.

Find the 150000th Alexandrian integer.

Solution: 1884161251122450
"""
from math import floor

def main(l):
    A = []
    p = 0
    q = 0
    r = 0
    curMax = 0
    print("Initialising array...")
    # while len(A) <= l:
    while len(A) < l:
        r += 1
        p = -(r + 1)
        while (p**2 + 2 * p * r - 1) < 0:
            q = (1 - p * r) / (p + r)
            if floor(q) == q:
                A.append(p * q * r)
            p -= 1
    A = sorted(A)
    curMax = A[-1]
    print("Calculating further results...")
    while r * (r + 1) * (r + 2) < curMax:
        r += 1
        p = -(r + 1)
        while (p**2 + 2 * p * r - 1) < 0:
            q = (1 - p * r) / (p + r)
            if floor(q) == q:
                if p * q * r < curMax:
                    A.pop()
                    A.append(p * q * r)
                    A = sorted(A)
                    curMax = A[l]
                    print(int(curMax))
            p -= 1
    print("Finished...")
    return A


if __name__ == '__main__':
    # l = 150000
    print(main(6))
    # A = [int(a) for a in main(l)]
    # print(A[l])
