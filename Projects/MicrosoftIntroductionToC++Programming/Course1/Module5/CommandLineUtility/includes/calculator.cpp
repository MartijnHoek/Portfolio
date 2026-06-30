#include "calculator.h"
#include "utility.h"

#include <iostream>

using namespace std;

int addition(int value1, int value2) {
    return value1 + value2;
}

int subtraction(int value1, int value2) {
    return value1 - value2;
}

int multiplication(int value1, int value2) {
    return value1 * value2;
}

double division(int value1, int value2) {
    if (value2 == 0) {
        cout << "Error: Division through 0 is not possible!" << endl;
        return 0;
    }
    else {
        return static_cast<double>(value1) / value2;    
    }
}

void calculatorInterface() {
    int menuChoice = 0;
    bool keepActive = true;

    while (keepActive) {
        cout << "==== CALCULATOR ====" << endl;
        cout << "Please select what to do:" << endl;
        cout << "1. Addition" << endl;
        cout << "2. Subtraction" << endl;
        cout << "3. Multiplication" << endl;
        cout << "4. Division" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice (1-5): " << endl;
    
        menuChoice = getValidatedInt();

        // Quit the menu to prevent requesting for the calculation values
        // Made this way to prevent asking the question multiple times later on
        if (menuChoice == 5) {
            cout << "User has decide to close the calculator, closing down now." << endl;
            keepActive = false;
            break;
        }

        // Get values to calculate with from the user
        int value1 = 0;
        int value2 = 0;
        cout << "Please enter your first value:" << endl;
        value1 = getValidatedInt();
        cout << "Please enter your second value:" << endl;
        value2 = getValidatedInt();

        if (menuChoice == 1) {
            cout << "-- Addition --" << endl;
            cout << "Result: " << addition(value1, value2) << endl;
        }
        else if (menuChoice == 2) {
            cout << "-- Subraction --" << endl;
            cout << "Result: " << subtraction(value1, value2) << endl;
        }
        else if (menuChoice == 3) {
            cout << "-- Multiplication --" << endl;
            cout << "Result: " << multiplication(value1, value2) << endl;
        }
        else if (menuChoice == 4) {
            cout << "-- Division --" << endl;
            cout << "Result: " << division(value1, value2) << endl;
        }
        else {
            cout << "Error: chosenUtility has a value of: " << menuChoice << " this should not happen, please try again." << endl;
        }
    };
};  
