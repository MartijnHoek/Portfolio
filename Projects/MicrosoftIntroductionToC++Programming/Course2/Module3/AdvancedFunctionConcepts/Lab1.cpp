#include <iostream>
#include <chrono>
#include <vector>
#include <string>

// Recursive Fibonacci (inefficient - exponential time)
long long fibonacciRecursive(int n) {
    if (n <= 1) return n;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Iterative Fibonacci (efficient - linear time)
long long fibonacciIterative(int n) {
    if (n <= 1) return n;

    long long prev = 0, curr = 1;
    for (int i = 2; i <= n; i++) {
        long long next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr;
}

// Recursive array sum
int sumArrayRecursive(const std::vector<int>& arr, int index = 0) {
    // Base case: reached end of array
    if (index >= arr.size()) {
        return 0;
    }

    // Recursive step: current element + sum of rest
    return arr[index] + sumArrayRecursive(arr, index + 1);
}

// Iterative array sum
int sumArrayIterative(const std::vector<int>& arr) {
    int sum = 0;
    for (int value : arr) {
        sum += value;
    }
    return sum;
}

// Function to measure execution time
template<typename Function>
void measureTime(const std::string& description, Function func) {
    auto start = std::chrono::high_resolution_clock::now();
    auto result = func();
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);

    std::cout << description << ": " << result
              << " (Time: " << duration.count() << " microseconds)" << std::endl;
}

int main() {
    std::cout << "=== Performance Comparison ===" << std::endl;

    // Compare Fibonacci implementations
    int fibNumber = 35; // Try 35 first, then maybe 40 if you're patient!

    std::cout << "Fibonacci(" << fibNumber << "):" << std::endl;

    measureTime("Recursive", [=]() { return fibonacciRecursive(fibNumber); });
    measureTime("Iterative", [=]() { return fibonacciIterative(fibNumber); });

    // Compare array sum implementations
    std::vector<int> testArray = {1, 5, 3, 9, 2, 8, 4, 7, 6, 10};

    std::cout << "\nArray Sum:" << std::endl;
    measureTime("Recursive", [&]() { return sumArrayRecursive(testArray); });
    measureTime("Iterative", [&]() { return sumArrayIterative(testArray); });

    // Demonstrate stack depth concerns
    std::cout << "\n=== Stack Depth Demonstration ===" << std::endl;

    // Test with larger arrays
    std::vector<int> largeArray(10000, 1); // 10,000 elements, all value 1

    std::cout << "Large array (10,000 elements):" << std::endl;
    std::cout << "Iterative sum: " << sumArrayIterative(largeArray) << std::endl;

    // Note: Recursive version might cause stack overflow with large arrays
    std::cout << "Recursive sum: ";
    try {
        std::cout << sumArrayRecursive(largeArray) << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Stack overflow or other error occurred!" << std::endl;
    }

    return 0;
}



// #include <iostream>

// // Recursive factorial calculation
// long long factorial(int n) {
//     // Base case: factorial of 0 or 1 is 1
//     if (n <= 1) {
//         return 1;
//     }

//     // Recursive step: n! = n * (n-1)!
//     return n * factorial(n - 1);
// }

// // Recursive Fibonacci sequence
// long long fibonacci(int n) {
//     // Base cases
//     if (n <= 0) return 0;
//     if (n == 1) return 1;

//     // Recursive step: F(n) = F(n-1) + F(n-2)
//     return fibonacci(n - 1) + fibonacci(n - 2);
// }

// // Recursive power calculation (alternative to iterative version)
// long long recursivePower(int base, int exponent) {
//     // Base case
//     if (exponent == 0) return 1;
//     if (exponent == 1) return base;

//     // Recursive step for positive exponents
//     if (exponent > 0) {
//         return base * recursivePower(base, exponent - 1);
//     }

//     // Handle negative exponents (returns 0 for integer division)
//     return 0;
// }

// // Recursive sum of digits
// int sumOfDigits(int number) {
//     // Make number positive if negative
//     number = std::abs(number);

//     // Base case: single digit
//     if (number < 10) {
//         return number;
//     }

//     // Recursive step: last digit + sum of remaining digits
//     return (number % 10) + sumOfDigits(number / 10);
// }

// int main() {
//     std::cout << "=== Recursive Calculations ===" << std::endl;

//     // Test factorial
//     std::cout << "Factorial of 6: " << factorial(6) << std::endl;
//     std::cout << "Factorial of 10: " << factorial(10) << std::endl;

//     // Test Fibonacci
//     std::cout << "Fibonacci sequence (first 10 numbers): ";
//     for (int i = 0; i < 10; i++) {
//         std::cout << fibonacci(i) << " ";
//     }
//     std::cout << std::endl;

//     // Test recursive power
//     std::cout << "Recursive power: 3^4 = " << recursivePower(3, 4) << std::endl;

//     // Test sum of digits
//     std::cout << "Sum of digits in 12345: " << sumOfDigits(12345) << std::endl;
//     std::cout << "Sum of digits in 987: " << sumOfDigits(987) << std::endl;

//     return 0;
// }


// #include <iostream>
// #include <cmath>
// // Overloaded functions for calculating area
// double calculateArea(double radius) {
//     // Circle area pi * r^2
//     return 3.14159 * radius * radius;
// }
// int calculateArea(int length) {
//     // Square area: length * length
//     return length * length;
// }
// double calculateArea(double length, double width) {
//     // Rectangle area: lentgh * width
//     return length * width;
// }
// double calculateArea(double base, double height, bool isTriangle) {
//     // Triangle area: 0.5 * base * height
//     // The bool value is used to distinguish from the rectangle
//     return 0.5 * base * height;
// }
// // Overloaded functions for power calculations
// int power(int base, int exponent) {
//     // Integer power using repeated multiplication
//     if (exponent == 0) return 1;
//     if (exponent == 1) return base;
//     if (exponent > 0) {
//         int result = 1;
//         for (int i = 0; i < exponent; i++) {
//             result *=base;
//         }
//         return result; 
//     } else {
//         return 0;
//     }
// }
// double power(double base, double exponent) {
//     // Floating-point power using library function
//     return std::pow(base, exponent);
// }


// int main() {
//     // Test area calculations
//     std::cout << "=== Area Calculations ===" << std::endl;
//     std::cout << "Circle (radius 5): " << calculateArea(5.0) << std::endl;
//     std::cout << "Square (4x4): " << calculateArea(4, 4) << std::endl;
//     std::cout << "Rectangle (4x6): " << calculateArea(4.0, 6.0) << std::endl;
//     std::cout << "Triangle (base 4, height 6): " << calculateArea(4.0, 6.0, true) << std::endl;
//     // Test power calculations
//     std::cout << "\n=== Power Calculations ===" << std::endl;
//     std::cout << "Integer: 2^8 = " << power(2, 8) << std::endl;
//     std::cout << "Float: 2.5^3.2 = " << power(2.5, 3.2) << std::endl;
//     return 0;
// }