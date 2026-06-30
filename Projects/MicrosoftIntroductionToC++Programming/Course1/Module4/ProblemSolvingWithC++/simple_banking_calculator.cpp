#include <iostream>
#include <cmath>    // For pow() function
#include <limits>
using namespace std;

// Generic function to validate the user input
double validateInput() {
    double input;
    bool validInput;

    do {
        if (!(cin >> input)) {
            std::cout << "Invalid input, please enter a number!" << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
            validInput = false;
        }
        else if (input < 0) {
            std::cout << "Invalid score input, please try again!" << endl;
            validInput = false;
        }
        else {
            validInput = true;
        }
    } while (!validInput);
    return input;
}

int main() {
    double principal, rate, years;
    double finalAmount;
    // Your implementation here 
    cout << "Please enter your initial deposit amount: " << endl;
    principal = validateInput();

    cout << "Please enter your annual interest rate (%): " << endl;
    rate = validateInput() / 100.0; // Divide number to %

    cout << "Please enter the number of years: " << endl;
    years = validateInput();

    finalAmount = principal * pow(1 + rate, years);

    cout << "--- Results ---" << endl;
    cout << "Final amount: " << finalAmount << endl;
    cout << "Interest earned: " << finalAmount - principal << endl;

    return 0;
}