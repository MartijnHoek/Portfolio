// #include <iostream>
// using namespace std;

// int main() {
// 	cout << "=== SCORE CALCULATOR ===" << endl;

// 	// Method 1: For loop - when you know exact iterations
// 	cout << "\nMethod 1 - For loop:" << endl;
// 	int totalScore = 0;

// 	for (int level = 1; level <= 8; level++) {
// 		int levelScore = level * 150;  // 100 points per level
// 		totalScore += levelScore;
// 		cout << "Level " << level << ": " << levelScore << " points" << endl;
// 	}

// 	cout << "Total with for loop: " << totalScore << " points" << endl;

// 	// Method 2: While loop - when condition-based iteration
// 	cout << "\nMethod 2 - While loop:" << endl;
// 	totalScore = 0;
// 	int level = 1;

// 	while (level <= 8) {
// 		int levelScore = level * 150;
// 		totalScore += levelScore;
// 		cout << "Level " << level << ": " << levelScore << " points" << endl;
// 		level++;  // Don't forget to increment!
// 	}

// 	cout << "Total with while loop: " << totalScore << " points" << endl;

// 	return 0;
// }

// #include <iostream>
// using namespace std;

// int main() {
// 	cout << "=== PLAYER REGISTRATION ===" << endl;

// 	// Validate player level (1-20)
// 	int playerLevel;
// 	do {
// 		cout << "Enter your player level (1-20): ";
// 		cin >> playerLevel;

// 		if (playerLevel < 1 || playerLevel > 20) {
// 			cout << "Invalid level! Please try again." << endl;
// 		}
// 	} while (playerLevel < 1 || playerLevel > 20);

// 	cout << "Valid level entered: " << playerLevel << endl;

// 	// Validate player name (non-empty)
// 	string playerName;
// 	do {
// 		cout << "Enter your player name (cannot be empty): ";
// 	    getline(cin, playerName);

// 		if (playerName.length() < 2) {
// 			cout << "Name cannot be less than 2 characters! Please try again." << endl;
// 		}
// 	} while (playerName.length() < 2);

// 	cout << "Welcome, " << playerName << " (Level " << playerLevel << ")!" << endl;

// 	return 0;
// }

#include <iostream>
using namespace std;

int main() {
	cout << "=== NUMBER PROCESSOR ===" << endl;

	cout << "\nProcessing numbers 1-20:" << endl;
	cout << "- Skip multiples of 3" << endl;
	cout << "- Stop when reaching 15" << endl;

	for (int num = 1; num <= 20; num++) {
		// Skip multiples of 3
		if (num % 3 == 0) {
			cout << num << " (skipped - multiple of 3)" << endl;
			continue;  // Skip rest of loop body, go to next iteration
		}

		// Stop processing when reaching 12
		if (num >= 12) {
			cout << num << " (stopping here)" << endl;
			break;  // Exit loop completely
		}

		// Process the number
		cout << num << " (processed)" << endl;
	}

	cout << "\nLoop finished." << endl;

	// Example: Finding first even number in a list
	cout << "\nFinding first even number in list:" << endl;

	int numbers[] = {7, 13, 9, 19, 11, 8, 4};
	int arraySize = 7;

	for (int i = 0; i < arraySize; i++) {
		cout << "Checking " << numbers[i] << "... ";

		if (numbers[i] % 2 == 0) {
			cout << "Found first even number: " << numbers[i] << endl;
			break;  // Stop searching once we find the first even number
		} 
		else {
			cout << "odd, continuing..." << endl;
		}
	}

	return 0;
}