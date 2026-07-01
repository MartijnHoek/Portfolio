#include "unit_conversion.h"
#include "utility.h"

#include <iostream>

using namespace std;

double kwToHp(int value1) {
    return static_cast<double>(value1) * 1.34102209;    
}

double hpToKw(int value1) {
    return static_cast<double>(value1) * 0.745699872;    
}

double kmToMiles(int value1) {
    return static_cast<double>(value1) * 0.621371192;    
}

double milesToKm(int value1) {
    return static_cast<double>(value1) * 1.609344;    
}

void unitConversionInterface() {
    int menuChoice = 0;
    bool keepActive = true;

    while (keepActive) {
        cout << "==== Unit Conversion ====" << endl;
        cout << "Please select what to do:" << endl;
        cout << "1. kW to HP" << endl;
        cout << "2. HP to kW" << endl;
        cout << "3. Kilometers to miles" << endl;
        cout << "4. Miles to kilometers" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice (1-5): " << endl;
    
        menuChoice = getValidatedInt();

        // Quit the menu to prevent requesting for the conversion values
        // Made this way to prevent asking the question multiple times later on
        if (menuChoice == 5) {
            cout << "User has decide to close the tool, closing down now." << endl;
            keepActive = false;
            break;
        }

        // Get value to convert with from the user
        int value1 = 0;
        cout << "Please enter the value that you want to convert:" << endl;
        value1 = getValidatedInt();

        if (menuChoice == 1) {
            cout << "-- kW to HP --" << endl;
            cout << "Result: " << kwToHp(value1) << endl;
        }
        else if (menuChoice == 2) {
            cout << "-- HP to kW --" << endl;
            cout << "Result: " << hpToKw(value1) << endl;
        }
        else if (menuChoice == 3) {
            cout << "-- Kilometers to miles --" << endl;
            cout << "Result: " << kmToMiles(value1) << endl;
        }
        else if (menuChoice == 4) {
            cout << "-- Miles to kilometers --" << endl;
            cout << "Result: " << milesToKm(value1) << endl;
        }
        else {
            cout << "Error: chosenUtility has a value of: " << menuChoice << " this should not happen, please try again." << endl;
        }
    };
};  
