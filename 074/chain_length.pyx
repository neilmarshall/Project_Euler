cpdef int digit_factorial_sum(int n):
    cdef dict factorial = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
    cdef int t = 0
    cdef int c
    while n >= 10:
        c = n % 10
        t += factorial[c]
        n //= 10
    t += factorial[n]
    return t


cpdef int chain_length(int n):
    cdef int chain = 1
    cdef set seen = {n}
    while True:
        n = digit_factorial_sum(n)
        if n not in seen:
            seen.add(n)
            chain += 1
        else:
            break
    return chain

