#include <iostream>

#include "includes/utility.h"
#include "includes/calculator.h"
#include "includes/unit_conversion.h"
#include "includes/text_converter.h"
#include "includes/wedding_date.h"

using namespace std;

// Main function of the utility command line tool
int main() {
    int chosenUtility = 0;
    bool keepToolActive = true;

    while (keepToolActive) {
        // Display the options to the user
        cout << "==== UTILITY PROGRAM MENU ====" << endl;
        cout << "1. Calculator" << endl;
        cout << "2. Unit conversion" << endl;
        cout << "3. Text case converter" << endl;
        cout << "4. Days till my wedding calculator" << endl;
        cout << "5. Exit the program" << endl;
        cout << "Enter your choice (1-5): " << endl;

        chosenUtility = getValidatedInt();

        if (chosenUtility == 1) {
            calculatorInterface();        
        }
        else if (chosenUtility == 2) {
            unitConversionInterface();
        }
        else if (chosenUtility == 3) {
            textConverter();
        }
        else if (chosenUtility == 4) {
            weddingDateCalculator();
        }
        else if (chosenUtility == 5) {
            cout << "User has decide to close the utility tools, closing down now." << endl;
            keepToolActive = false;
        }
        else {
            cout << "Error: chosenUtility has a value of: " << chosenUtility << " this should not happen, please try again." << endl;
        }
    }
    return 0;
}