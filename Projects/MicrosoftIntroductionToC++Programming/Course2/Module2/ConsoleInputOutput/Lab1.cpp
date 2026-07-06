#include <iostream>
#include <iomanip>
#include <limits>
#include <string>

// int main() {
//     int age;
//     std::cout << "Enter Customer Age: ";
//     while (!(std::cin >> age) || age < 0 || age > 120) {
//         std::cin.clear();
//         std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
//         std::cout << "Invalid input. Please enter an age between 0 and 120: ";
//     }
//     std::cout << "Age entered: " << age << std::endl;
//     return 0;
// }

int main() {
    std::string name;
    int customerID;
    double balance;

    // Name input
    std::cout << "Enter Customer Name: ";
    do {
        std::getline(std::cin, name);

        if (name.empty()) {
            std::cout << "Invalid input. Please enter a name: ";
        }
    } while (name.empty());

    // ID input
    std::cout << "Enter Customer ID (1000-9999): ";
    while (!(std::cin >> customerID) || customerID < 1000 || customerID > 9999) {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Invalid input. Please enter an ID number (1000-9999): ";
    }

    // balance input
    std::cout << "Enter Customer balance: ";
    while (!(std::cin >> balance) || balance < 0) {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Invalid input. Please enter a postive number: ";
    }

    // Header
    std::cout << std::setfill('=') << std::setw(40) << "" << std::endl;
    std::cout << std::setfill(' ') << "CUSTOMER INFORMATION" << std::endl;
    std::cout << std::setfill('=') << std::setw(40) << "" << std::endl;

    // Data display
    std::cout << std::setfill(' ') << std::left;
    std::cout << std::setw(15) << "Name:" << name << std::endl;
    std::cout << std::setw(15) << "Customer ID:" << customerID << std::endl;
    std::cout << std::setw(15) << "Balance:" << std::fixed << std::setprecision(2) << "$" << balance << std::endl;

    return 0;
}