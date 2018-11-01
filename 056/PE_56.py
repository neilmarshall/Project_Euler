#! venv/bin/python3.7
"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100
is almost unimaginably large: one followed by two-hundred zeros. Despite their
size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the
maximum digital sum?

Solution: 972
"""
def PE_56():
    """
    >>> PE_56()
    972
    """
    LIMIT = 99
    maximal_digit_sum = 0
    for a in range(1, LIMIT + 1):
        A, AexpB = NumberAsString(str(a)), NumberAsString("1")
        for b in range(1, LIMIT + 1):
            AexpB *= A
            maximal_digit_sum = max(maximal_digit_sum, sum(int(digit) for digit in str(AexpB)))
    return maximal_digit_sum


class NumberAsString():
    def __init__(self, s=None):
        if s is not None and type(s) is not str:
            raise TypeError("Argument must be nil or a string")
        self.s = s if s is not None else "0"

    def __str__(self):
        return self.s

    def __repr__(self):
        return "NumberAsString('{0}')".format(self.s)

    def __eq__(self, other):
        return self.s == other.s

    def __len__(self):
        return len(self.s)

    def __add__(self, other):
        BASE = 10
        LHS, RHS = self.s, other.s
        while len(LHS) < len(RHS):
            LHS = '0' + LHS
        while len(RHS) < len(LHS):
            RHS = '0' + RHS
    
        carry, result = 0, ""
        for left, right in zip(reversed(LHS), reversed(RHS)):
            n = int(left) + int(right) + carry
            carry = n // BASE
            result = str(n % BASE) + result
        if carry != 0:
            result = str(carry) + result

        return NumberAsString(result)

    def __mul__(self, other):
        BASE = 10
        LHS, RHS = self.s[::-1], other.s[::-1]
        while len(LHS) < len(RHS):
            LHS += '0'
        while len(RHS) < len(LHS):
            RHS += '0'

        carry, result = 0, NumberAsString()
        for i, multiplier in enumerate(LHS):
            if multiplier != '0':
                product = '0' * i
                for multiplicand in RHS:
                    if multiplicand != '0':
                        n = int(multiplier) * int(multiplicand) + carry
                        carry = n // BASE
                        product = str(n % BASE) + product
                result += NumberAsString(product)
        if carry:
            result = NumberAsString(str(carry) + str(result))
        return result

    def __pow__(self, other):
        result, power = NumberAsString("1"), NumberAsString()
        while power != other:
            power += NumberAsString("1")
            result *= self
        return result


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
