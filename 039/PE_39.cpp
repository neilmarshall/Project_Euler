/*
If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120:

    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

Solution: 840
*/

#include <algorithm>
#include <iostream>
#include <map>

inline bool is_pythagorean_triple(int a, int b, int c) { return a * a + b * b == c * c; }

int main() {

    std::map<int, int> perimeter_counts;  // map to hold count of number of solutions for each perimeter value p 

    // the following nested for-loop generates triples a, b, c such that
    // a < b < c so WLOG can be passed into the above function to check if
    // they form a Pythagorean triple - if so increment the solution count for
    // the perimeter a + b + c
    for (int a = 1; a <= 1000 / 3; a++) {
        for (int b = a + 1; b <= (1000 - a) / 2; b++) {
            for (int c = b + 1; c <= 1000 - a - b; c++) {
                if (is_pythagorean_triple(a, b, c))
                    perimeter_counts[a + b + c] += 1;
            }
        }
    }
    
    // identify value in solution map with greatest count
    using pair = std::pair<int, int>;
    auto max_element = std::max_element(perimeter_counts.begin(), perimeter_counts.end(),
        [] (const pair& p1, const pair& p2) { return p1.second < p2.second; });
    
    std::cout << max_element->first << std::endl;
}
