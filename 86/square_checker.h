#include <map>

class square_checker {
    private:
        std::map<long, bool> checked_numbers;
    public:
        bool operator()(long);
};

