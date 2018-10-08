/*
All square roots are periodic when written as continued fractions.

[***See full problem desciption for explanation of shorthand notation***]

The first ten continued fraction representations of (irrational) square roots are:

    √2 = [1;(2)], period = 1
    √3 = [1;(1,2)], period = 2
    √5 = [2;(4)], period = 1
    √6 = [2;(2,4)], period = 2
    √7 = [2;(1,1,1,4)], period = 4
    √8 = [2;(1,4)], period = 2
    √10 = [3;(6)], period = 1
    √11 = [3;(3,6)], period = 2
    √12 = [3;(2,6)], period = 2
    √13 = [3;(1,1,1,1,6)], period = 5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?

Solution: 1322
*/

#include <cmath>

#include <iostream>

bool is_square(const int& n) {
    int root = static_cast<int>(sqrt(n));
    return root * root == n;
}

int get_sqrt_expansion_period(const int& n) {
    int a_0 = static_cast<int>(sqrt(n));
    int epsilon_0 = a_0;
    int gamma_0 = n - static_cast<int>(pow(epsilon_0, 2));
    
    int a = a_0;
    int epsilon = epsilon_0;
    int gamma = gamma_0;
    
    int period = 0;
    while (++period) {
        a = (static_cast<int>(sqrt(n)) + epsilon ) / gamma;
        epsilon = a * gamma - epsilon;
        gamma = (n - static_cast<int>(pow(epsilon, 2))) / gamma;
        if (epsilon == epsilon_0 && gamma == gamma_0) break;
    }
    
    return period;
}

int main() {
    int count = 0;
    for (int n = 2; n <= 10000; n++) {
        if (!is_square(n) && get_sqrt_expansion_period(n) % 2 != 0) ++count;
    }
    std::cout << "Number of odd periods = " << count << std::endl;
}
