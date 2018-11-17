/*
Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into piles in
exactly seven different ways, so p(5)=7.

Find the least value of n for which p(n) is divisible by one million.

Solution: 55374
*/

#include <iostream>
#include <vector>

void sbExtendGk(std::vector<int>& Gk, std::vector<int>& power, const int& n) {
    int k = (Gk.size() + 1) / 2;
    do {
        Gk.insert(Gk.end(), {k * (3 * k - 1) / 2, -k * (3 * -k - 1) / 2});
    } while (n > Gk.back());
    
    if (k % 2 != 0) {
        power.insert(power.end(), {1, 1});
    }
    else {
        power.insert(power.end(), {-1, -1});
    }
}

int main() {

    const int LIMIT = 1000000;

    std::vector<int> Pn {1, 1}, Gk {0}, power {0};

    int n = 2;
    do {
        if (n > Gk.back()) { sbExtendGk(Gk, power, n); }
        int k = 1, temp = 0;
        do {
            if (n >= Gk[k]) {
                temp += power[k] * Pn[n - Gk[k]];
                temp %= LIMIT;
            }
        } while(n > Gk[k++]);
        Pn.push_back(temp);
    } while(n++ && Pn.back() != 0);
    
    std::cout << Pn.size() - 1 << std::endl;
}
