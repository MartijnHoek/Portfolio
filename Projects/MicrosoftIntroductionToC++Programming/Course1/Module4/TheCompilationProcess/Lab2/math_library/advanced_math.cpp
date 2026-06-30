#include "advanced_math.h"
#include <cmath> // For sqrt function
double power(double base, int exponent) {
    return pow(base, exponent);
}
double squareRoot(double number) {
    return sqrt(number);
}
double absolute(double number) {
    if (number < 0) {
        return -number;
    }
    return number;
}
double cube(double number) {
    return number * number * number;
}