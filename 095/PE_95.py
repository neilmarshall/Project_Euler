#! /usr/bin/env python3.7
"""
The proper divisors of a number are all the divisors excluding the number
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the
sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the
proper divisors of 284 is 220, forming a chain of two numbers. For this reason,
220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we
form a chain of five numbers:

    12,496
    14,288
    15,472
    14,536
    14,264

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding
one million.

Solution: 14316
"""
def PE_95(limit):
    """
    >>> PE_95(1000000)
    14316
    """
    divisor_sums = generate_proper_divisor_sums(limit)
    max_chain_length = 0
    for n in range(1, limit + 1):
        chain_length = calculate_chain_length(n, divisor_sums, limit)
        if chain_length > max_chain_length:
            max_chain_length = chain_length
            result = n
    return result


def generate_proper_divisor_sums(limit):
    """
    >>> generate_proper_divisor_sums(20)
    [0, 0, 1, 1, 3, 1, 6, 1, 7, 4, 8, 1, 16, 1, 10, 9, 15, 1, 21, 1, 22]
    """
    divisor_sums = [0 for _ in range(limit + 1)]
    for i in range(1, limit // 2 + 1):
        for j in range(2, limit // i + 1):
            divisor_sums[i * j] += i
    return divisor_sums


def calculate_chain_length(n, divisor_sums, limit):
    """
    >>> divisor_sums = generate_proper_divisor_sums(300)
    >>> calculate_chain_length(220, divisor_sums, 300)
    2
    """
    chain = [n]
    while True:
        divisor_sum = divisor_sums[chain[-1]]
        if divisor_sum in {0, 1} or divisor_sum > limit or divisor_sum in chain:
            break
        chain.append(divisor_sum)
    return len(chain) if divisor_sum == n else 0


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
