#include <iostream>
#include <array>
#include <stdexcept>

// int main() {
//     // Declare and initialize a C-style array with 10 temperature readings
//     int c_temps[10] = {72, 75, 68, 80, 77, 73, 69, 82, 78, 76};
//     // Declare and initialize a std::array with the same temperature readings
//     std::array<int, 10> std_temps = {72, 75, 68, 80, 77, 73, 69, 82, 78, 76};
//     std::cout <<"Temperature data loaded succesfully!" << std::endl;
//     return 0;
// }

int main() {
    int c_temps[10] = {72, 75, 68, 80, 77, 73, 69, 82, 78, 76};
    std::array<int, 10> std_temps = {72, 75, 68, 80, 77, 73, 69, 82, 78, 76};
    // Access the 5th, 7th and 10th temperature readings
    std::cout << "5th reading C-style: " << c_temps[4] << std::endl;
    std::cout << "5th reading std::array: " << std_temps.at(4) << std::endl;

    std::cout << "7th reading C-style: " << c_temps[6] << std::endl;
    std::cout << "7th reading std::array: " << std_temps.at(6) << std::endl;

    std::cout << "10th reading C-style: " << c_temps[9] << std::endl;
    std::cout << "10th reading std::array: " << std_temps.at(9) << std::endl;

    // Test out-of-bounds access
    std::cout << "Out of bounds test:" << std::endl;
    std::cout << "C-style[10]: " << c_temps[10] << "(unsafe!)" << std::endl;
    try {
        std::cout << "std::array.at(10): " << std_temps.at(10) << std::endl;
    }
    catch (const std::out_of_range& e) {
        std::cout << "Exception Caught: " << e.what() << std::endl;
    }

    // Modify 3rd reading to 85 degrees
    c_temps[2] = 85;
    std_temps.at(2) = 85;
    // Modify 8th reading to 90 degrees
    c_temps[7] = 90;
    std_temps.at(7) = 90;

    // Display all temperatures to confirm modifications
    std::cout << "C-style temperatures: ";
    for (int i = 0; i < 10; i++) {
        std::cout << c_temps[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "std::array temperatures: ";
    for (const auto& temp : std_temps) {
        std::cout << temp << " ";
    }
    std::cout << std::endl;
    return 0;

}