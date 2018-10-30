#include "truncate.h"
#include "gmock/gmock.h"

using namespace testing;

TEST(Truncate, LeavesEfficientMappingsUnchanged) {
    ASSERT_THAT(truncate("MMMMDCLXXII"), Eq("MMMMDCLXXII"));
}

TEST(Truncate, MapsIIIItoIV) {
    ASSERT_THAT(truncate("MDCCCXXIIII"), Eq("MDCCCXXIV"));
}

TEST(Truncate, MapsVIIIItoIX) {
    ASSERT_THAT(truncate("MMMDLXVIIII"), Eq("MMMDLXIX"));
}

TEST(Truncate, MapsXXXXtoXL) {
    ASSERT_THAT(truncate("MMMMCCXXXXI"), Eq("MMMMCCXLI"));
}

TEST(Truncate, MapsLXXXXtoXC) {
    ASSERT_THAT(truncate("MMCCCLXXXXIX"), Eq("MMCCCXCIX"));
}

TEST(Truncate, MapsDCCCCtoCM) {
    ASSERT_THAT(truncate("MMMMCCXXXXI"), Eq("MMMMCCXLI"));
}
