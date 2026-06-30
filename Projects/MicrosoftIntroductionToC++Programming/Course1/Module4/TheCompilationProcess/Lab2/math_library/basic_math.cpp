// Include the corresponding header file
#include "basic_math.h"
// Implement the functions declared in the header
double add(double a, double b) {
    return a + b;
}
double subtract(double a, double b) {
    return a - b;
}
double multiply(double a, double b) {
    return a * b;
}
double divide(double a, double b) {
    // Check for division by zero
    if (b == 0) {
        // In a real program, this should be handled better
        return 0;
    }
    return a / b;
}