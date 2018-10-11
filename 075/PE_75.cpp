/*
It turns out that 12cm is the smallest length of wire that can be bent to form
an integer sided right angle triangle in exactly one way, but there are many
more examples.

    12cm: (3,4,5)
    24cm: (6,8,10)
    30cm: (5,12,13)
    36cm: (9,12,15)
    40cm: (8,15,17)
    48cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
integer sided right angle triangle, and other lengths allow more than one
solution to be found; for example, using 120 cm it is possible to form exactly
three different integer sided right angle triangles.

    120cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can
exactly one integer sided right angle triangle be formed?

Solution: 161667
*/

#include "../utilities/include/utilities.h"

#include <iostream>
#include <map>
#include <tuple>

using namespace PythagoreanTriples;

int get_length(const std::tuple<int, int, int>& tup, int n) {
    return n * (std::get<0>(tup) + std::get<1>(tup) + std::get<2>(tup));
}

int main () {

    const int LIMIT = 1500000;

    std::map<int, int> length_count_map;  // holds count of number of triples indexed by perimeter length

    PythagoreanTripleGenerator<int>* ptg = new PythagoreanTripleGenerator<int>;

    // for each primitive triple ...
    while (true) {
        auto triple = ptg->GetNextTriple();
        if (get_length(triple, 1) > LIMIT) { break; }

        // for each multiple of each primitive triple ...
        int n = 0;
        while (++n) {
            int length = get_length(triple, n);
            if (length > LIMIT) { break; }
            length_count_map[length] += 1;
        }
    }

    delete ptg;

    // cycle through map of perimeter counts and count the number equal to 1
    int length_one_count = 0;
    for (auto length_count : length_count_map) {
        if (length_count.second == 1) { length_one_count += 1; }
    }

    std::cout << length_one_count << std::endl;
}

