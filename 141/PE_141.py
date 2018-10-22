"""
A positive integer, n, is divided by d and the quotient and remainder are q and
r respectively. In addition d, q, and r are consecutive positive integer terms
in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be seen
that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2). We
will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 1022, happen to also be perfect
squares. The sum of all progressive perfect squares below one hundred thousand
is 124657.

Find the sum of all progressive perfect squares below one trillion (1012).

Solution: 878454337159
"""
from collections import deque
from math import sqrt, floor

def gen_prog_sqrs(p, q, limit):
    g, s = 0, p * q**3 + p**2
    while s <= limit:
        g += 1
        s = g**2 * p * q**3 + g * p**2
        if sqrt(s) - floor(sqrt(s)) == 0:
            yield s


def main(limit):
    """
    >>> main(100000)
    124657
    
    >>> main(1000000000000)
    878454337159
    """
    progressive_squares = set()
    dq = deque([(1, 2), (1, 3)])
    while dq:
        p, q = dq.popleft()
        p_q_n1, p_q_n2, p_q_n3 = (q, 2 * q - p), (q, 2 * q + p), (p, 2 * p + q)
        if p_q_n1[0] * p_q_n1[1]**3 + p_q_n1[0]**2 <= limit:
            dq.append((p_q_n1[0], p_q_n1[1]))
        if p_q_n2[0] * p_q_n2[1]**3 + p_q_n2[0]**2 <= limit:
            dq.append((p_q_n2[0], p_q_n2[1]))
        if p_q_n3[0] * p_q_n3[1]**3 + p_q_n3[0]**2 <= limit:
            dq.append((p_q_n3[0], p_q_n3[1]))
        for element in gen_prog_sqrs(p, q, limit):
            progressive_squares.add(element)
    return sum(progressive_squares)


if __name__ == '__main__':
    import doctest; doctest.testmod()
