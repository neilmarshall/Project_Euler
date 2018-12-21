#! /usr/bin/env python3.7
"""
Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that
there are only 12951 numbers below one-million that are not bouncy and only
277032 non-bouncy numbers below 10^10.

How many numbers below a googol (10^100) are not bouncy?

Solution: 51161058134250
"""
def PE_113(limit):
    """
    >>> PE_113(10)
    277032

    >>> PE_113(100)
    51161058134250
    """
    increasing_numbers, increasing_number_count = list(range(10)), 0
    decreasing_numbers, decreasing_number_count = [], 9
    for exponent in range(2, limit + 1):
        for i in range(1, 10):
            increasing_number_count += increasing_numbers[i]
            increasing_numbers[i] += increasing_numbers[i - 1]
        decreasing_numbers.append(increasing_number_count + 9)
    for decreasing_number in decreasing_numbers:
        decreasing_number_count += decreasing_number - 9
    return increasing_number_count + decreasing_number_count


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
