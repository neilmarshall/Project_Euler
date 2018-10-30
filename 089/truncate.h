#include <string>
#include <vector>

std::string truncate(std::string numeral) {

    std::vector< std::pair<std::string, std::string> > mappings {
        {"VIIII", "IX"}, {"IIII", "IV"}, {"LXXXX", "XC"},
        {"XXXX", "XL"}, {"DCCCC", "CM"}, {"CCCC", "CD"}
    };

    for (auto mapping : mappings) {
        auto location = numeral.find(mapping.first);
        if (location != std::string::npos) {
            numeral.replace(location, mapping.first.size(), mapping.second);
        }
    }

    return numeral;
}
