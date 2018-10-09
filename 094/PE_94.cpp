/*
It is easily proved that no equilateral triangle exists with integral length
sides and integral area. However, the almost equilateral triangle 5-5-6 has
an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which
two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with
integral side lengths and area and whose perimeters do not exceed
one billion (1,000,000,000).

The solution is derived from the algorithm as follows:

    Observe that an almost equilateral triangle can be thought of as
    two identical right-angled triangles back-to-back.
    
    Generate all Pythagorean triples a, b, c such that a <= b <= c,
    then these will give almost equilateral triangles with perimeter equal
    to 2 * (a + c). By construction the almost equilateral triangle will
    have integral length sides and integral areas.
    
    So we just need to check that the constructed triangle satisfies the final
    criteria. Observe that since a <= b <= c the lengths of sides of the
    constructed almost equilateral triangle will be c, c, 2 * a. So we just
    need to check that 2 * a +/- 1 = c.

SOLUTION :: 518408346

NOTE :: Code below intended to be compiled under C++14 or later
*/

#include <iostream>

int main() {

    const int limit = 1'000'000'000;

    int a = 0, c = 0, m = 0, n = 0, perimeterSum = 0;

    while (2 * (a + c) <= limit) {
        for (n = 1; n < m; ++n) {
            a = std::min(m * m - n * n, 2 * m * n);  // min. length of Pythagorean triple constructed from Euclid's algorithm
            c = std::max(m * m + n * n, 2 * m * n);  // max. length of Pythagorean triple constructed from Euclid's algorithm
            if (abs(c - 2 * a) == 1) { perimeterSum += 2 * (a + c); }
        }
        ++m;
    }

    std::cout << "Result: " << perimeterSum << std::endl;
}
