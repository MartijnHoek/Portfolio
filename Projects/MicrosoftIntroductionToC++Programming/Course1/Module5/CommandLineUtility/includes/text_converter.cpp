#include "text_converter.h"
#include "utility.h"

#include <iostream>
#include <limits>

using namespace std;

string setAllUpperCase(string stringInput) {
    for (char &c : stringInput) {
        c = toupper(static_cast<unsigned char>(c));
    }
    return stringInput;
}

string setAllLowerCase(string stringInput) {
    for (char &c : stringInput) {
        c = tolower(static_cast<unsigned char>(c));
    }
    return stringInput;
}

int textConverter() {
    int menuChoice = 0;
    bool keepActive = true;

    while (keepActive) {
        cout << "==== STRING CONVERTER ====" << endl;
        cout << "Please select what to do:" << endl;
        cout << "1. All uppercase" << endl;
        cout << "2. All lowercase" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice (1-3): " << endl;
    
        menuChoice = getValidatedInt();

        // Quit the menu to prevent requesting for the conversion values
        // Made this way to prevent asking the question multiple times later on
        if (menuChoice == 3) {
            cout << "User has decide to close the tool, closing down now." << endl;
            keepActive = false;
            break;
        }

        // Get value to convert with from the user
        string value1 = "";
        cout << "Please enter the string that you want to convert:" << endl;
        value1 = getValidatedString();

        if (menuChoice == 1) {
            cout << "-- All uppercase --" << endl;
            cout << "Result: " << setAllUpperCase(value1) << endl;
        }
        else if (menuChoice == 2) {
            cout << "-- All lowercase --" << endl;
            cout << "Result: " << setAllLowerCase(value1) << endl;
        }
        else {
            cout << "Error: chosenUtility has a value of: " << menuChoice << " this should not happen, please try again." << endl;
        }
    };
    return 0;
};  
