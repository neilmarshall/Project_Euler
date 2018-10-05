#include "../include/utilities.h"

#include <iostream>
#include <memory>

int main() {

    std::unique_ptr< primes::Phi<int> > phi (new primes::Phi<int>(20));

    for (int n = 1; n <= 20; n++) {
        std::cout << n << ": " << (*phi)(n) << '\n';
    }

    std::cout << std::endl;

    std::unique_ptr< combinations::nCr_Calculator<int> > nCr (new combinations::nCr_Calculator<int>);
    for (int n = 1; n <= 15; n++) {
        for (int r = 0; r <= n; r++) {
            std::cout << (*nCr)(n, r) << " ";
        }
        std::cout << '\n';
    }

    std::cout << std::endl;
}

