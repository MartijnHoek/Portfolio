#include <iostream>
#include <cmath>  // For mathematical functions like sqrt(), pow(), etc.
#include <limits>

using namespace std;

int main() {
	// Display a welcome message
	cout << "=======================================" << endl;
	cout << "        INTERACTIVE CALCULATOR         " << endl;
	cout << "=======================================" << endl;
	cout << "This calculator allows you to perform" << endl;
	cout << "various mathematical operations." << endl << endl;

    // Main program code will go here
    bool exitProgram = false;   // Controls whether the program should exit
    int choice;                 // Stores the user's menu choice

    while (!exitProgram) {
	// Display the menu
	cout << "\nPlease select an operation:" << endl;
	cout << "1. Addition" << endl;
	cout << "2. Subtraction" << endl;
	cout << "3. Multiplication" << endl;
	cout << "4. Division" << endl;
	cout << "5. Square Root" << endl;
	cout << "6. Exponentiation (Power)" << endl;
	cout << "7. Exit" << endl;
    cout << "8. Remainder (Modulo)" << endl;
    cout << "9. Absolute Value" << endl;
	cout << "\nEnter your choice (1-9): ";

	// Get the user's choice
	cin >> choice;

    // Get the user's choice
    if (!(cin >> choice)) {
        // If input is not a number, clear the error state and discard the input
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Invalid input! Please enter a number." << endl;
        continue;   // Skip the rest of the loop and start over
    }

// 	// Process the choice using conditional statements
// 	// We'll implement this in the next activity
//     // Variables to store the operands
    double num1, num2, result;

//     // Process the user's choice using if-else statements
//     if (choice == 1) {  // Addition
//         cout << "Enter first number: ";
//         cin >> num1;
//         cout << "Enter second number: ";
//         cin >> num2;

//         result = num1 + num2;
//         cout << "Result: " << num1 << " + " << num2 << " = " << result << endl;
//     }
//     else if (choice == 2) {  // Subtraction
//         cout << "Enter first number: ";
//         cin >> num1;
//         cout << "Enter second number: ";
//         cin >> num2;

//         result = num1 - num2;
//         cout << "Result: " << num1 << " - " << num2 << " = " << result << endl;
//     }
//     else if (choice == 3) {  // Multiplication
//         cout << "Enter first number: ";
//         cin >> num1;
//         cout << "Enter second number: ";
//         cin >> num2;

//         result = num1 * num2;
//         cout << "Result: " << num1 << " * " << num2 << " = " << result << endl;
//     }
//     else if (choice == 4) {     // Division
//         cout << "Enter numerator: ";
//         cin >> num1;
//         cout << "Enter denominator: ";
//         cin >> num2;
//         // Check for division by zero
//         if (num2 == 0) {
//             cout << "Error: Division by zero is not allowed." << endl;
//         } else {
//             result = num1 / num2;
//             cout << "Result: " << num1 << " / " << num2 << " = " << result << endl;
//         }
//     }
//     else if (choice == 5) { // Square Root
//         cout << "Enter a number: " << endl;
//         cin >> num1;
//         // Check if number is negative
//         if (num1 < 0) {
//             cout << "Error: Cannot calculate square root of a negative number" << endl;
//         }
//         else {
//             result = sqrt(num1); // Using sqrt function from cmath
//             cout << "Result: sqrt (" << num1 << ") = " << result << endl; 
//         }
//     }
//     else if (choice == 6) { // Exponentation
//         cout << "Enter the base number: " << endl; 
//         cin >> num1;
//         cout << "Enter the exponent: " << endl;
//         cin >> num2;
        
//         if (num1 < 0) {
//             cout << "Error: Cannot calculate exponent of a negative base number" << endl;
//         }
//         else if (num2 < 0) {
//             cout << "Error: Cannot calculate exponent of a negative exponent number" << endl;
//         }
//         else {
//                 result = pow(num1, num2);
//                 cout << "Result: " <<  result << endl;
//             }
//     }

//     else if (choice == 7) {  // Exit
//         exitProgram = true;
//         cout << "Thank you for using the Interactive Calculator. Goodbye!" << endl;
//     }
//     else {
//         cout << "Please implement other operations or handle invalid input" << endl;
//     }
// }

    // Process the user's choice using a switch statement
    switch (choice) {
        case 1:  // Addition
            cout << "Enter first number: ";
            cin >> num1;
            cout << "Enter second number: ";
            cin >> num2;

            result = num1 + num2;
            cout << "Result: " << num1 << " + " << num2 << " = " << result << endl;
            break;

        case 2:  // Subtraction
            cout << "Enter first number: ";
            cin >> num1;
            cout << "Enter second number: ";
            cin >> num2;

            result = num1 - num2;
            cout << "Result: " << num1 << " - " << num2 << " = " << result << endl;
            break;

        case 3:  // Multiplication
            cout << "Enter first number: ";
            cin >> num1;
            cout << "Enter second number: ";
            cin >> num2;

            result = num1 * num2;
            cout << "Result: " << num1 << " * " << num2 << " = " << result << endl;
            break;

        case 4:  // Division
            cout << "Enter numerator: ";
            cin >> num1;
            cout << "Enter denominator: ";
            cin >> num2;

            // Check for division by zero
            if (num2 == 0) {
                cout << "Error: Division by zero is not allowed." << endl;
            } 
            else {
                result = num1 / num2;
                cout << "Result: " << num1 << " / " << num2 << " = " << result << endl;
            }
            break;

        case 5:  // Square Root
            cout << "Enter a number: ";
            cin >> num1;

            // Check if the number is negative
            if (num1 < 0) {
                cout << "Error: Cannot calculate square root of a negative number." << endl;
            } 
            else {
                result = sqrt(num1);  // Using the sqrt function from cmath
                cout << "Result: sqrt(" << num1 << ") = " << result << endl;
            }
            break;

        case 6:  // Exponentiation (to be implemented in Practice Challenge 2)
            cout << "Please implement the exponentiation operation." << endl;
            break;

        case 7:  // Exit
            exitProgram = true;
            cout << "Thank you for using the Interactive Calculator. Goodbye!" << endl;
            break;

        default:  // Invalid choice
            cout << "Invalid choice! Please enter a number between 1 and 7." << endl;
            break;
    }


	return 0;
    }
}
