cpdef int digit_factorial_sum(int n):
    cdef int* factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
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

