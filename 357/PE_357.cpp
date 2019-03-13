#include <cmath>

#include <iostream>
#include <set>
#include <vector>

class MemoizedPrimeChecker
{
public:
	MemoizedPrimeChecker(long n) { known_primes = get_primes_up_to_n(n); }
	bool is_prime(long n) { return known_primes.find(n) != known_primes.end(); }

private:

	std::set<long> known_primes;

	std::set<long> get_primes_up_to_n(const long& n) {

		if (n <= 1) { return std::set<long>(); }

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

		std::set<long> primes;
		for (long i = 2; i <= n; i++) {
			if (flags[i]) { primes.insert(i); }
		}

		return primes;
	}
};

int main()
{
	long limit = 1000000;
	auto memoized_prime_checker = MemoizedPrimeChecker(limit + 1);
	long total = 0;

	std::vector<bool> flags;
	for (long i = 0; i <= limit; i++) { flags.push_back(true); }
	for (long d = 1; d <= static_cast<long>(sqrt(limit)); d++) {
		std::cout << d << '\n';
		long i = 0;
		do {
			long index = d * d + i * d;
			if (index > limit) { break; }
			long residual = d + index / d;
			if (!memoized_prime_checker.is_prime(residual)) { flags[index] = false; }
		} while (++i);
	}
	for (long i = 0; i <= limit; i++)
		if (flags[i]) { total += i; }
	std::cout << total << std::endl;
}
