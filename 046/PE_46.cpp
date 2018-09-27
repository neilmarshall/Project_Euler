/*
PE_46 (Goldbach's other conjecture)
-----------------------------------
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.
    9 = 7 + 2 × 1^2
    15 = 7 + 2 × 2^2
    25 = 7 + 2 × 3^2
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
Note:
	For a given integer n, starting from k = int(sqrt(n / 2)) and working down
	to 1, check if n - 2 * k^2 is prime; if so iterate n by 2. End procedure
	when k = 1 does not produce a residual prime.
*/

#include <cmath>
#include <iostream>

bool isprime(int n) {
    for (int p = 2; p <= static_cast<int>(sqrt(n)); p++) {
        if (n % p == 0) return false;
    }
    return true;
}

int solve_conjecture() {

	int n = 9;  // first odd composite number

	do {
		if (!isprime(n)) {  // if true then we have an odd composite number
			for (int k = static_cast<int>(sqrt(n / 2)); k >= 0; --k) {
			    if (k == 0) return n;  // if true then we have exhausted all values for k
			    if (isprime(n - 2 * k * k)) break;
			}
		}
	} while (n += 2);  // increment k by 2 so continue to check odd numbers
}

int main() {
	std::cout << "Result = " << solve_conjecture() << '\n';	
}
