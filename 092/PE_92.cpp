/*
A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example:

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually arrive
at 1 or 89.

How many starting numbers below ten million will arrive at 89?


Solution: 8581146
*/

#include <iostream>
#include <string>

bool returns_89(int n) {
    while (n != 1 && n != 89) {
        std::string str = std::to_string(n);
        n = 0;
        for (auto chr  : str) {
            n += (chr - '0') * (chr - '0');
        }
    }
    return n == 89;
}

int main () {
    int count_of_digits_returning_89 = 0;
    int n = 0;
    while (++n < 10000000) {
        if (returns_89(n)) { count_of_digits_returning_89 += 1; }
    }

    std::cout << count_of_digits_returning_89 << '\n';
}

