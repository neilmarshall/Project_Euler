/*
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

    d2d3d4 = 406 is divisible by 2
    d3d4d5 = 063 is divisible by 3
    d4d5d6 = 635 is divisible by 5
    d5d6d7 = 357 is divisible by 7
    d6d7d8 = 572 is divisible by 11
    d7d8d9 = 728 is divisible by 13
    d8d9d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

Solution = 16695334890
*/

#include <algorithm>
#include <iostream>
#include <string>

bool check_string(std::string s) {
    int primes[] = {0, 2, 3, 5, 7, 11, 13, 17};
    for (int i = 1; i <= 7; i++) {
        if (std::stoi(s.substr(i, 3)) % primes[i] != 0)
            return false;
    }
    return true;
}

int main() {

    std::string s = "0123456789";
    long divisble_pandigital_sum = 0;

    do {
        divisble_pandigital_sum += (check_string(s) ? std::stol(s) : 0);
    } while (std::next_permutation(s.begin(), s.end()));
    
    std::cout << divisble_pandigital_sum << std::endl;
}
