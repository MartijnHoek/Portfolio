#include <iostream>
#include "basic_math.h"
#include "advanced_math.h"
#include "geometry.h"
#include "statistics.h"
int main() {
    std::cout << "===== Math Library Demonstration =====" << std::endl;
    // Test basic math operations
    std::cout << "\n--- Basic Math ---" << std::endl;
    std::cout << "Addition: 5 + 3 = " << add(5, 3) << std::endl;
    std::cout << "Subtraction: 5 - 3 = " << subtract(5, 3) << std::endl;
    std::cout << "Multiplication: 5 * 3 = " << multiply(5, 3) << std::endl;
    std::cout << "Division: 5 / 3 = " << divide(5, 3) << std::endl; 
    // Test advanced math operations
    std::cout << "\n--- Advanced Math ---" << std::endl;
    std::cout << "Power: 2^3 = " << power(2, 3) << std::endl;
    std::cout << "Square Root of 16 = " << squareRoot(16) << std::endl;
    std::cout << "Absolute of -7.5 = " << absolute(-7.5) << std::endl; 
    // Test geometric calculations
    std::cout << "\n--- Geometry ---" << std::endl;
    double radius = 5.0;
    std::cout << "Circle with radius " << radius << ":" << std::endl;
    std::cout << "  Area = " << circleArea(radius) << std::endl;
    std::cout << "  Perimeter = " << circlePerimeter(radius) << std::endl;
    double length = 4.0, width = 6.0;
    std::cout << "Rectangle with length " << length << " and width " << width << ":" << std::endl;
    std::cout << "  Area = " << rectangleArea(length, width) << std::endl;
    std::cout << "  Perimeter = " << rectanglePerimeter(length, width) << std::endl;    
    std::cout << "Cube of 3 = " << cube(3) << std::endl;

    std::cout << "\n--- Statistics ---" << std::endl;
    double data[] = {4.2, 7.8, 3.1, 9.5, 2.6};
    int dataSize = sizeof(data) / sizeof(data[0]);
    std::cout << "Data set: ";
    for (int i = 0; i < dataSize; i++) {
    std::cout << data[i] << " ";
    }
    std::cout << std::endl;
    std::cout << "Average = " << average(data, dataSize) << std::endl;
    std::cout << "Minimum = " << minimum(data, dataSize) << std::endl;
    std::cout << "Maximum = " << maximum(data, dataSize) << std::endl;
    return 0;
}