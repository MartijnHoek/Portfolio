// #include <iostream>
// #include <climits>  // For INT_MAX constant

// int main() {
//     // Declare variables of different data types
//     int playerLevel = 25;
//     long int totalScore = 150000L;
//     long long int worldPopulation = 7800000000LL;
//     float itemPrice = 19.99f;
//     double preciseCalculation = 3.14159265359;
//     char playerRank = 'A';
//     bool gameActive = true;

//     // Display the memory usage of each data type
//     std::cout << "Memory Usage Analysis:" << std::endl;
//     std::cout << "int uses: " << sizeof(int) << "bytes" << std::endl;
//     std::cout << "long int uses: " << sizeof(long int) << "bytes" << std::endl;
//     std::cout << "long long int uses: " << sizeof(long long int) << "bytes" << std::endl;
//     std::cout << "float uses: " << sizeof(float) << "bytes" << std::endl;
//     std::cout << "double uses: " << sizeof(double) << "bytes" << std::endl;
//     std::cout << "char uses: " << sizeof(char) << "byte" << std::endl;
//     std::cout << "bool uses: " << sizeof(bool) << "byte" << std::endl;

//     return 0;
// }

#include <iostream>
#include <climits>
int main() {
    // Test integer limits
    std::cout << "Integer Limits and Overflow:" << std::endl;
    int maxValue = INT_MAX;
    std::cout << "Maximum int value: " << maxValue << std::endl;
    std::cout << "What happens when we add 1: " << maxValue + 1 << std::endl;
    // Test type casting between different types
    std::cout << "\nType Casting Examples:" << std::endl;
    double precisePrice = 29.95;
    int roundedPrice = static_cast<int>(precisePrice);
    std::cout << "Original price (double): " << precisePrice << std::endl;
    std::cout << "After casting to int: " << roundedPrice << std::endl;
    // Test character to integer conversion
    char letter = 'C';
    int letterValue = static_cast<int>(letter);
    std::cout << "Character '" << letter << "' has ASCII value: " << letterValue << std::endl;
    return 0;
}
