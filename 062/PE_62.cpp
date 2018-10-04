/*
The cube, 41063625 (345^3), can be permuted to produce two other
cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is
the smallest cube which has exactly three permutations of its digits
which are also cube.

Find the smallest cube for which exactly five permutations of its
digits are cube.

Solution: 127035954683
*/

#include <cmath>

#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>

inline long cuber (const long& n) { return static_cast<long>(pow(n, 3)); }

bool is_permutation(const long& x1, const long& x2);

int main() {

    const long PERMUTATION_COUNT = 5;

    long n = 1;
    std::vector<long> cubes;
    std::vector<long> permutations;
    
    do {
        permutations.clear();
        permutations.push_back(cuber(n));
        for (auto cube : cubes) {
            if (is_permutation(cube, cuber(n)))
                permutations.push_back(cube);
        }
        cubes.push_back(cuber(n));
    } while (permutations.size() < PERMUTATION_COUNT && n++);
    
    std::cout << *std::min_element(permutations.begin(), permutations.end()) << std::endl;
}

bool is_permutation(const long& x1, const long& x2) {
    std::string s1 = std::to_string(x1);
    std::string s2 = std::to_string(x2);
    if (s1.size() != s2.size())
        return false;
    std::multiset<char> set1(s1.begin(), s1.end());
    std::multiset<char> set2(s2.begin(), s2.end());
    return set1 == set2;
}
