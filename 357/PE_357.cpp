/*
Consider the divisors of 30: 1, 2, 3, 5, 6, 10, 15, 30.
It can be seen that for every divisor d of 30, d + 30 / d is prime.

Find the sum of all positive integers n not exceeding 100,000,000
such that for every divisor d of n, d + n / d is prime.

Solution: 1739023853137
*/

#include <cmath>

#include <iostream>
#include <vector>

std::vector<bool> get_prime_flags_up_to_n(const long& n) {

    if (n <= 1) { return std::vector<bool>(); }

    std::vector<bool> flags = { false, false };
    for (long p = 2; p <= n; p++) {
        flags.push_back(true);
    }

    for (long p = 2; p <= n / 2; p++) {
        if (flags[p]) {
            for (long q = 2; q <= n / p; q++) {
                flags[p * q] = false;
            }
        }
    }

    return flags;
}

int main()
{
	long limit = 100000000;

	auto prime_checker = get_prime_flags_up_to_n(limit + 1);

	std::vector<bool> flags;
	for (long i = 0; i <= limit; i++) { flags.push_back(true); }

	for (long d = 1; d <= static_cast<long>(sqrt(limit)); d++) {
		long i = 0;
		do {
			long index = d * d + i * d;
			if (index > limit) { break; }
			long residual = d + index / d;
			if (!prime_checker[residual]) { flags[index] = false; }
		} while (++i);
	}

	long total = 0;
	for (long i = 0; i <= limit; i++)
		if (flags[i]) { total += i; }
	std::cout << total << std::endl;
}
