#include "tinyformat.h"

int main() {
    std::string weekday = "Wednesday";
    const char* month = "July";
    size_t day = 27;
    long hour = 14;
    int min = 44;

    tfm::printf("%s, %s %d, %.2d:%.2d\n", weekday, month, day, hour, min);
    return 0;
}
