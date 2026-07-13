#include <iostream>
#include <iomanip>
#include <limits>
#include <string>
#include <vector>
#include <format>
#include <regex>

bool validateEmail(const std::string& email) {
    // Basic email pattern: username@domain.extension
    std::regex email_pattern(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})");
    return std::regex_match(email, email_pattern);
}

bool validatePhone(const std::string& phone) {
    // US Phone pattern: (123) 456-7890 or 123-456-7890
    std::regex phone_pattern(R"((\d3\d{3}\s?|\d{3}[-.]?)\d{3}[-.]?\d{4})");
    return std::regex_match(phone, phone_pattern);
}

bool validateName(const std::string& name) {
    // Name should contain only letters and spaces, at least 2 characters
    std::regex name_pattern(R"([a-zA-Z\s]{2,})");
    return std::regex_match(name, name_pattern) && !name.empty();
}

bool validateZip(const std::string& zip) {
    // ZIP should be 5 or 5+4 format
    std::regex zip_pattern(R"(^\d{5}(-\d{4})?$)");
    return std::regex_match(zip, zip_pattern);
}


int main() {
    std::string name, email, phone, zip;
    // Validate name
    do {
        std::cout << "Enter full name: ";
        std::getline(std::cin, name);
        if (!validateName(name)) {
            std::cerr << "Error: Name must contain only letters and spaces (minimum 2 characters)." << std::endl;
        }
    } while (!validateName(name));
    // Validate email
    do {
        std::cout << "Enter email address: ";
        std::getline(std::cin, email);
        if (!validateEmail(email)) {
            std::cerr << "Error: Invalid email format. Use: user@domain.com" << std::endl;
        }
    } while (!validateEmail(email));
    // Validate phone
    do {
        std::cout << "Enter phone number (123-456-7890 or (123) 456-7890): ";
        std::getline(std::cin, phone);
        if (!validatePhone(phone)) {
            std::cerr << "Error: Invalid phone format. Use 123-456-7890 or (123) 456-7890" << std::endl;
        }
    } while (!validatePhone(phone));
    // Validate ZIP
    do {
        std::cout << "Enter ZIP code (12345 or 12345-6789): ";
        std::getline(std::cin, zip);
        if (!validateZip(zip)) {
            std::cerr << "Error: Invalid ZIP code format. Use 12345 or 12345-6789" << std::endl;
        }
    } while (!validateZip(zip));

    // Display success message with formatted output
    std::cout << "\nRegistration successful!" << std::endl;
    std::cout << std::string(40, '=') << std::endl;
    std::cout << "Customer Information:" << std::endl;
    std::cout << std::string(40, '-') << std::endl;
    std::cout << "Name:  " << name << std::endl;
    std::cout << "Email: " << email << std::endl;
    std::cout << "Phone: " << phone << std::endl;
    std::cout << "ZIP:   " << zip << std::endl;
    std::cout << std::string(40, '=') << std::endl;

    return 0;
}

// struct Product {
//     std::string name;
//     double price;
//     int quantity;
//     double total() const {return price * quantity; }
// };

// int main() {
//     std::vector<Product> products = {
//         {"Laptop", 999.999, 2},
//         {"Mouse", 29.50, 5},
//         {"Keyboard", 89.99, 3}
//     };

//     std::cout << std::string(50, '=') << std::endl;
//     std::cout << "INVOICE SUMMARY" << std::endl;
//     std::cout << std::string(50, '=') << std::endl;
    
//     std::cout   << std::left << std::setw(15) << "Product"
//                 << std::right << std::setw(8) << "Price"
//                 << std::right << std::setw(8) << "Qty"
//                 << std::right << std::setw(10) << "Total" << std::endl;
    
//     std::cout << std::string(50, '-') << std::endl;
//     double grandTotal = 0.0;
//     for (const auto& product: products) {
//         std::cout   << std::left    << std::setw(15)    << product.name
//                     << std::right   << std::setw(7)     << std::fixed   << std::setprecision(2) << "$"  << product.price
//                     << std::right   << std::setw(8)     << product.quantity
//                     << std::right   << std::setw(9)     << "$"  << std::fixed   << std::setprecision(2) <<  product.total()
//                     << std::endl;
        
//         grandTotal += product.total();
//     }

//     std::cout << std::string(50, '-') << std::endl;
//     std::cout   << std::right << std::setw(41) << "GRAND TOTAL: $"
//                 << std::fixed << std::setprecision(2) << grandTotal << std::endl;

//     std::cout << std::format("Tax (8.5%): ${:.2f}\n", grandTotal * 0.085);
//     std::cout << std::format("Final Total: ${:.2f}\n", grandTotal * 1.085);

//     double taxRate = 0.085;
//     double tax = grandTotal * taxRate;
//     double finalTotal = grandTotal + tax;

//     std::cout << std::format("Tax (8.5%): ${:.2f}\n", tax);
//     std::cout << std::format("Final Total: ${:.2f}\n", finalTotal);

//     return 0;
// }

// int main() {
//     double price;
//     int quantity;
//     std::string productName;

//     std::cout << "Enter product price: $";
//     while (!(std::cin >> price) || price < 0) {
//         // Check what went wrong
//         if (std::cin.fail()) {
//             std::cerr << "Error: Invalid price format. Please enter a number." << std::endl;
//             std::cin.clear(); // Clear error flags
//             std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
//         } else {
//             std::cerr << "Error: Price cannot be negative." << std::endl;
//         }
//         std::cout << "Enter product price: $";
//     }
//     std::cout << "Enter quantity: ";
//     while(!(std::cin >> quantity) || quantity < 1) {
//         if (std::cin.fail()) {
//             std::cerr << "Error: Invalid quantity format. Please enter a whole number." << std::endl;
//             std::cin.clear();
//             std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
//         } else {
//             std::cerr << "Error: Quantity must be at least 1." << std::endl;
//         }
//         std::cout << "Enter quantity: ";
//     }

//     std::cout << "Enter Product name: ";
//     std::cin.ignore();  //Removes remains entered from previous entry
//     while(true) {
//         std::getline(std::cin, productName);

//         // If something was entered
//         if (!productName.empty()) {
//             break;
//         }

//         std::cerr << "Error: Input was empty please enter a product name." << std::endl;
//         std::cout << "Enter product name: ";
//     }


//     std::cout << "Valid input recieved!" << std::endl;
//     std::cout << "Price $" << price << ", Quantity: " << quantity << ", Product name: " << productName << std::endl;
//     return 0; 
// }