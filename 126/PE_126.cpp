/*
* The minimum number of cubes to cover every visible face on a cuboid measuring
* 3 x 2 x 1 is twenty-two.
*
* If we then add a second layer to this solid it would require forty-six cubes
* to cover every visible face, the third layer would require seventy-eight cubes,
* and the fourth layer would require one-hundred and eighteen cubes to cover
* every visible face.
* 
* However, the first layer on a cuboid measuring 5 x 1 x 1 also requires
* twenty-two cubes; similarly the first layer on cuboids measuring
* 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.
* 
* We shall define C(n) to represent the number of cuboids that contain n cubes
* in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.
* 
* It turns out that 154 is the least value of n for which C(n) = 10.
* 
* Find the least value of n for which C(n) = 1000.
* 
* Solution: 18522
*/

#include <iostream>

bool count_layers(const int& x, const int& y, const int& z, const int& n) {
    int f0 = 2 * (x * y + x * z + y * z);
    int f1 = 4 * (x + y + z);
    int layer = 0;
    int i = 0;
    while (layer < n) {
        layer = f0 + i * f1 + 4 * i * (i - 1);
        if (layer == n) { return true; }
        ++i;
    }
    return false;
}

int C(const int& n) {
    int layer_count = 0;
    int x_max = ((n / 2) - 1) / 2;
    for (int x = 1; x <= x_max; ++x) {
        int y_max = std::min(x, (n / 2 - x) / (x + 1));
        for (int y = 1; y <= y_max; ++y) {
            int z_max = std::min(y, (n / 2 - x * y) / (x + y));
            for (int z = 1; z <= z_max; ++z) {
                if (count_layers(x, y, z, n)) { ++layer_count; }
            }
        }
    }
    return layer_count;
}

int main() {
    int problem_limit = 1000;
    int n = 2;
    while (true) {
        if (n % 500 == 0) { std::cout << n << '\n'; }
        if (C(n) == problem_limit) {break;}
        n += 2;
    }
    std::cout << "Solution: " << n << std::endl;   
}
