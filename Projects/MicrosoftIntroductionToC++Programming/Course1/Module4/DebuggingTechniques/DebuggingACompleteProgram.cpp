#include <iostream>
using namespace std;

int main() {
	cout << "=== Simple Banking Calculator ===" << endl;

	double balance = 1000.0;
	int choice;
	double amount;
	bool continueOperations = true;

	while (continueOperations == true) {	// Assignment instead of comparison
		cout << "\nCurrent Balance: $" << balance << endl;
		cout << "1. Deposit" << endl;
		cout << "2. Withdrawal" << endl;
		cout << "3. Check Balance" << endl;
		cout << "4. Exit" << endl;
		cout << "Choose an option: ";
		cin >> choice;

		switch (choice) {
			case 1:
				cout << "Enter deposit amount: $";
				cin >> amount;

				if (amount > 0) {
					balance = balance + amount;	// Wrong operation
					cout << "Deposited $" << amount << endl;
				} else {
					cout << "Invalid amount!" << endl;
				}
				break;

			case 2:
				cout << "Enter withdrawal amount: $";
				cin >> amount;

				if (amount > 0 && amount <= balance) {
					balance = balance - amount;
					cout << "Withdrew $" << amount << endl;
				} else if (amount > balance) {
					cout << "Insufficient funds!" << endl;
				} else {
					cout << "Invalid amount!" << endl;
				}
				break;

			case 3:
				cout << "Current balance: $" << balance << endl;
				break;

			case 4:
				continueOperations = false;
				cout << "Thank you for banking with us!" << endl;
				break;

			default:
				cout << "Invalid choice! Please try again." << endl;
		}

		// Calculate and display interest (2% annually)
		double annualInterest = balance * 0.02;
		cout << "Annual interest earned: $" << annualInterest << endl;
	}

	return 0;
}