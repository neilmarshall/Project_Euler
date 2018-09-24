/*
  main.cpp
  PE_28_v1 (Number spiral diagonals)
  First created by Neil Marshall on 04/12/2015.
  This version updated by by Neil Marshall on 09/08/2018.
  Copyright B) 2015 Neil Marshall. All rights reserved.
*/

#include <iostream>
#include <vector>

/**
Returns sum of diagonals of a number-spiral of size n x n

Test cases:

    >>> number_spiral_diagonal_sum(1) = 1
    >>> number_spiral_diagonal_sum(3) = 25
    >>> number_spiral_diagonal_sum(5) = 101
    >>> number_spiral_diagonal_sum(7) = 261
    >>> number_spiral_diagonal_sum(1001) = 669171001
*/
long number_spiral_diagonal_sum(long n) {

    // program only works for odd integer input
    if (n % 2 != 1) {
        std::cerr << "n must be an odd integer";
        exit(EXIT_FAILURE);
    }

    long s = 1;
    for (long t = 3; t <= n; t += 2) {
        s += 4 * t * t - 6 * (t - 1);
    }
    return s;
}

int main() {

    std::vector<long> test_values = {1, 3, 5, 7, 1001};
    for (auto test_value : test_values) {
        std::cout << test_value  << ": ";
        std::cout << number_spiral_diagonal_sum(test_value) << '\n';
    }    
}
