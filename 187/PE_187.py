"""
If n has exactly 2 primes factors then n = p.q, where p and q are primes and p (WLOG) is
less than or equal to sqrt(n).

So check primes up to sqrt(n), and if one such prime p divides n then check that n is not equal
to p.q.r, for q and r primes. That is, check that n // p has no prime divisors less than sqrt(n / p).

Pseucode algorithm:
    count = 0
    primes = generate_primes(sqrt(limit))
    for n in [1, ..., limit]:
        if n % p == 0 for some p in primes less than sqrt(n):
            if (n // p) % q !=0 for all q in primes less than sqrt(n // p):
                count += 1
    return count
"""
def get_primes_up_to_n(n):
    flags = [False, False] + [True for _ in range(2, n + 1)]
    for p in range(2, n // 2 + 1):
        if flags[p]:
            for q in range(2, n // p + 1):
                flags[p * q] = False
    return [i for i, flag in enumerate(flags) if flag]


def PE_187(limit):
    """
    >>> PE_187(30)
    10
    """
    count = 0
    primes = get_primes_up_to_n(int(limit**0.5))
    def first_divisor(n):
        for p in primes:
            if p > int(n**0.5):
                return 0
            if n % p == 0:
                return p
    for n in range(4, limit + 1):
        p = first_divisor(n)
        if p:
            if first_divisor(n // p) == 0:
                count += 1
    return count
    

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
