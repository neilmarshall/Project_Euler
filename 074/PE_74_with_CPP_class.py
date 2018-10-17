================
factorial_digit_sum_chain_counter.pyx
================
# distutils: language = c++
# distutils: sources = FactorialDigitSumChainCounter.cpp

cdef extern from "FactorialDigitSumChainCounter.h":
    cdef cppclass FactorialDigitSumChainCounter:
        FactorialDigitSumChainCounter(int)
        int CountChainsOfLength(int)


cdef class Py_FactorialDigitSumChainCounter():
    cdef FactorialDigitSumChainCounter c_factorial_digit_sum_chain_counter

    def __cinit__(self, int n):
        self.c_factorial_digit_sum_chain_counter = FactorialDigitSumChainCounter(n)

    def __dealloc__(self):
        del self.c_factorial_digit_sum_chain_counter

    def CountChainsOfLength(self, int n):
        return self.c_factorial_digit_sum_chain_counter.CountChainsOfLength(n)
================


================
PE_74.py
================
from factorial_digit_sum_chain_counter import Py_FactorialDigitSumChainCounter

def main() {
    """
    >>> main()
    402
    """
    factorial_digit_sum_chain_counter = Py_FactorialDigitSumChainCounter (1000000)
    return factorial_digit_sum_chain_counter.CountChainsOfLength(60)


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)

================
