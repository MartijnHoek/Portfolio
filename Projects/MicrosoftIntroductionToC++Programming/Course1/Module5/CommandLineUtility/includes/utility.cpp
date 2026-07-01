#include "utility.h"

#include <iostream>
#include <limits>

using namespace std;

int getValidatedInt() {
    /*
    Function created to validate a integer input
    */
    bool validInput = false;
    int inputValue;

    do {
        if (!(cin >> inputValue)) {
            std::cout << "Invalid input, please enter a number!" << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
            validInput = false;
        }
        else {
            validInput = true;
        }
    } while (!validInput);
    return inputValue;
}

string getValidatedString() {
    /*
    Function created to validate a string input
    */
    bool validInput = false;
    string inputValue;

    do {
        if (!(cin >> inputValue)) {
            std::cout << "Invalid input, please enter a string!" << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
            validInput = false;
        }
        else {
            validInput = true;
        }
    } while (!validInput);
    return inputValue;
}