/*
The number 145 is well known for the property that the sum of the factorial of
its digits is equal to 145:

	1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers
that link back to 169; it turns out that there are only three such loops that exist:

    169 → 363601 → 1454 → 169
    871 → 45361 → 871
    872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck
in a loop. For example:

    69 → 363600 → 1454 → 169 → 363601 (→ 1454)
    78 → 45360 → 871 → 45361 (→ 871)
    540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty
non-repeating terms?

Solution: 402
*/

#include <iostream>
#include <set>

class FactorialDigitSumChainCounter {
    private:
        constexpr static int factorial[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
        int limit;
        
        static int digit_factorial_sum(int n) {
            int t = 0;
            while (n >= 10) {
                t += factorial[n % 10];
                n /= 10;
            }
            return t + factorial[n];
        }
        
        static int get_chain_length(int n) {
            int chain = 1;
            std::set<int> seen;
            while (true) {
                n = digit_factorial_sum(n);
                if (seen.find(n) == seen.end()) {
                    seen.insert(n);
                    chain += 1;
                } else {
                    break;
                }
            }
            return chain;
        }

    public:
        FactorialDigitSumChainCounter(int _limit) : limit(_limit) {}
        
        int CountChainsOfLength(int chain_length) {
            int count = 0;
            for (int n = 1; n < limit; n++) {
                if (get_chain_length(n) == chain_length) { count += 1; }
            }
            return count;
        }
};

int main() {
    FactorialDigitSumChainCounter factorial_digit_sum_chain_counter(1000000);
    std::cout << factorial_digit_sum_chain_counter.CountChainsOfLength(60) << std::endl;
}
