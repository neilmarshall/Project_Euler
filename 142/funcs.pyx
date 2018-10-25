from libc.math cimport floor, sqrt

cdef bint is_square(long n):
    cdef long root = <long>sqrt(n)
    return root**2 == n

cdef bint all_square(long x, long y, long z):
    cdef long numbers[6]
    numbers[:] = [x + y, x - y, x + z, x - z, y + z, y - z]
    cdef int i
    for i in range(6):
        if not is_square(numbers[i]):
            return False
    return True

cdef (long, long) get_limits(long alpha, long beta):
    cdef long lowerlimit, upperlimit
    lowerlimit = <long>sqrt(beta + 2)
    upperlimit = <long>sqrt(((alpha - 1) / 2)**2) + 1
    return lowerlimit, upperlimit

cpdef long check_primitive_solution(long a, long b):
    cdef long alpha, beta, n, x, y, z
    alpha, beta = a**2, b**2
    lowerlimit, upperlimit = get_limits(alpha, beta)
    for n in range (lowerlimit, upperlimit + 1):
        y = (n**2 + beta) / 2
        x = y + alpha
        z = y - beta
        if all_square(x, y, z):
            return x + y + z
    return 0
