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
    primes_up_to_root_of_limit = get_primes_up_to_n(int(limit**0.5))
    primes_up_to_root_of_limit_over_2 = get_primes_up_to_n(int((limit / 2)**0.5))
    count = 0
    def has_one_factor_below_root_of_limit(n):
        result = False
        for p in primes_up_to_root_of_limit:
            if p > int(n**0.5):
                return False
            if n % p == 0 and not result:
                result = True
            if n % p == 0 and result:
                return False
        return result
    def has_one_factor_below_root_of_limit_over_2(n):
        result = False
        for p in primes_up_to_root_of_limit_over_2:
            if p > int(n**0.5):
                return False
            if n % p == 0 and not result:
                result = True
            if n % p == 0 and result:
                return False
        return result
    for n in range(4, limit + 1):
        if has_one_factor_below_root_of_limit(n):
            if not has_one_factor_below_root_of_limit_over_2(n // p):
                count += 1
    return count


if __name__ == '__main__':
    import doctest; doctest.testmod()
