#include <iostream>
#include <climits>  // For data type limits like INT_MAX

int main() {
    // Display program header
    std::cout << "=======================================" << std::endl;
    std::cout << "   PRACTICAL DATA TYPE APPLICATION     " << std::endl;
    std::cout << "=======================================" << std::endl;
    std::cout << "This program demonstrates appropriate usage of different data types" << std::endl;
    std::cout << "for various kinds of information." << std::endl << std::endl;
    
    // ------ AGE DATA SECTION ------
    std::cout << "\n------ AGE DATA SECTION ------" << std::endl;
    std::cout << "Selecting appropriate data types for age information:" << std::endl;

    // Integer type for ages (no fractional years needed)
    int childAge = 8;
    int teenAge = 15;
    int adultAge = 42;
    
    // Display age information
    std::cout << "Child age: " << childAge << " years" << std::endl;
    std::cout << "Teen age: " << teenAge << " years" << std::endl;
    std::cout << "Adult age: " << adultAge << " years" << std::endl;

    // Show memory usage
    std::cout << "\nAge data memory usage:" << std::endl;
    std::cout << "Size of int (for ages): " << sizeof(int) << " bytes" << std::endl;
    
    // Demonstrate age calculations
    std::cout << "\nAge calculations:" << std::endl;
    int totalAges = childAge + teenAge + adultAge;
    std::cout << "Total of all ages: " << totalAges << " years" << std::endl;

    // ------ AGE CALCULATION PRACTICE ------
    // Average Age Calculation
    float averageAge = (childAge + teenAge + adultAge) / 3.0f;
    std::cout << "Average age: " << averageAge << " years" << std::endl;

    // Age difference calculation
    int ageDifference = adultAge - childAge;
    std::cout << "Age difference between adult and child: " << ageDifference << " years" << std::endl;

    // Your personal age calculation
    int currentYear = 2026;
    int birthYear = 1998;
    int myAge = currentYear - birthYear;
    std::cout << "My age based on birth year (" << birthYear << "): " << myAge << " years" << std::endl;


    // ------ PRICE DATA SECTION ------
    std::cout << "\n------ PRICE DATA SECTION ------" << std::endl;
    std::cout << "Selecting appropriate data types for price information:" << std::endl;

    // Use double for prices (needs decimal precision)
    double coffeePrice = 3.99;
    double laptopPrice = 1299.99;
    double housePrice = 350000.00;

    // Display price information
    std::cout << "Coffee price: $" << coffeePrice << std::endl;
    std::cout << "Laptop price: $" << laptopPrice << std::endl;
    std::cout << "House price: $" << housePrice << std::endl;

    // Show memory usage comparison
    float priceAsFloat = 19.99f;
    double priceAsDouble = 19.99;
    std::cout << "\nPrice storage comparison:" << std::endl;
    std::cout << "Price as float: $" << priceAsFloat << " (uses " << sizeof(float) << " bytes)" << std::endl;
    std::cout << "Price as double: $" << priceAsDouble << " (uses " << sizeof(double) << " bytes)" << std::endl;
    
    // Simple price calculations
    double totalPrice = coffeePrice + laptopPrice;
    std::cout << "\nPrice calculations:" << std::endl;
    std::cout << "Coffee + Laptop total: $" << totalPrice << std::endl;
 

    // ------ CHARACTER DATA SECTION ------
    std::cout << "\n------ CHARACTER DATA SECTION ------" << std::endl;
    std::cout << "Selecting appropriate data types for character information:" << std::endl;

    // Character variables for single characters
    char grade = 'A';
    char symbol = '#';
    char initial = 'J';

    // My personal characters
    char myFirstNameInitial = 'M';
    char myLastNameInitial = 'H';
    char myFavoriteLetter = 'J';

    // Display character information
    std::cout << "Student grade: " << grade << std::endl;
    std::cout << "Special symbol: " << symbol << std::endl;
    std::cout << "First initial: " << initial << std::endl;

    // Show how characters relate to numbers (ASCII values)
    std::cout << "\nCharacter to number conversion:" << std::endl;
    std::cout << "Grade '" << grade << "' has ASCII value: " << (int)grade << std::endl;
    std::cout << "Symbol '" << symbol << "' has ASCII value: " << (int)symbol << std::endl;
    
    // My personal characters
    std::cout << "My first name initial '" << myFirstNameInitial << "' has ASCII value: " << (int)myFirstNameInitial << std::endl;
    std::cout << "My last name initial '" << myLastNameInitial << "' has ASCII value: " << (int)myLastNameInitial << std::endl;
    std::cout << "My favorite letter: '" << myFavoriteLetter << "' has ASCII value: " << (int)myFavoriteLetter << std::endl;

    // Show memory usage
    std::cout << "\nCharacter data memory usage:" << std::endl;
    std::cout << "Size of char: " << sizeof(char) << " byte" << std::endl;


    // ------ BOOLEAN DATA SECTION ------
    std::cout << "\n------ BOOLEAN DATA SECTION ------" << std::endl;
    std::cout << "Using boolean data types for true/false information:" << std::endl;

    // Boolean variables for simple flags
    bool isActive = true;
    bool hasPermission = false;
    bool isCompleted = true;

    // Display boolean values (they show as 1 for true, 0 for false)
    std::cout << "User account active: " << isActive << std::endl;
    std::cout << "User has admin permission: " << hasPermission << std::endl;
    std::cout << "Task completed: " << isCompleted << std::endl;

    // Show memory usage
    std::cout << "\nBoolean data memory usage:" << std::endl;
    std::cout << "Size of bool: " << sizeof(bool) << " byte(s)" << std::endl;
    
    // Simple boolean comparisons
    std::cout << "\nBoolean comparisons:" << std::endl;
    std::cout << "Are both account active AND task completed? ";
    if (isActive == true && isCompleted == true) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }


    // ------ SIMPLE PRODUCT EXAMPLE ------
    std::cout << "\n------ SIMPLE PRODUCT EXAMPLE ------" << std::endl;
    std::cout << "Combining multiple data types for a product:" << std::endl;

    // Product information using different data types
    int productId = 12345;
    double productPrice = 29.99;
    char productGrade = 'B';
    bool inStock = true;

    // Personal product
    int productId2 = 123675;
    double productPrice2 = 95.99;
    char productGrade2 = 'F';
    bool inStock2 = false;

    // Display product information
    std::cout << "\nProduct Information:" << std::endl;
    std::cout << "Product ID: " << productId << std::endl;
    std::cout << "Price: $" << productPrice << std::endl;
    std::cout << "Quality Grade: " << productGrade << std::endl;
    std::cout << "In Stock: " << inStock << std::endl;

    // Display personal product information
    std::cout << "\nProduct Information:" << std::endl;
    std::cout << "Product ID: " << productId2 << std::endl;
    std::cout << "Price: $" << productPrice2 << std::endl;
    std::cout << "Quality Grade: " << productGrade2 << std::endl;
    std::cout << "In Stock: " << inStock2 << std::endl;

    // Simple calculations
    double salesTax = productPrice * 0.08;  // 8% tax
    double totalPrice_2 = productPrice + salesTax;
    
    std::cout << "\nPrice Calculations:" << std::endl;
    std::cout << "Sales tax (8%): $" << salesTax << std::endl;
    std::cout << "Total with tax: $" << totalPrice_2 << std::endl;
    
    // Memory usage summary
    int totalMemory = sizeof(productId) + sizeof(productPrice) + sizeof(productGrade) + sizeof(inStock);
    std::cout << "\nTotal memory used for this product: " << totalMemory << " bytes" << std::endl;

    return 0;
}
