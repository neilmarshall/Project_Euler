"""
Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing
a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half
of the numbers below one-thousand (525) are bouncy. In fact, the least number
for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we
reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

from fractions import Fraction

def decreasing(n):
    """
    >>> decreasing(66420)
    True

    >>> decreasing(155349)
    False

    >>> decreasing(206)
    False
    """
    def check(s):
        if len(s) == 1:
            return True
        return s[0] >= s[1] and decreasing(s[1:])
    return check(str(n))


def increasing(n):
    """
    >>> increasing(134468)
    True

    >>> increasing(155349)
    False

    >>> increasing(206)
    False
    """
    def check(s):
        if len(s) == 1:
            return True
        return s[0] <= s[1] and increasing(s[1:])
    return check(str(n))


def is_bouncy(n):
    """
    >>> is_bouncy(155349)
    True
    """
    return not decreasing(n) and not increasing(n)


def count_bouncy(limit):
    """
    >>> count_bouncy(1000)
    525
    """
    return sum(1 for n in range(limit) if is_bouncy(n))


def PE_112(threshold):
    """
    >>> PE_112(Fraction(1, 2))
    538

    >>> PE_112(Fraction(9, 10))
    21780

    >>> PE_112(Fraction(99, 100))
    1587000
    """
    bouncy_count, n = 0, 1
    while Fraction(bouncy_count, n) < threshold:
        n += 1
        if is_bouncy(n):
            bouncy_count += 1
    return n


if __name__ == '__main__':
    import doctest; doctest.testmod()
