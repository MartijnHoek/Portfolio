// #include <iostream>
// #include <string>

// using namespace std;

// int main() {
// 	string playerChoice;
// 	cout << "Welcome to the Adventure Game!" << endl;
// 	cout << "You stand at a crossroads in a mysterious forest." << endl;
// 	cout << "Do you want to go 'left' or 'right'? ";
// 	cin >> playerChoice;
// 	if (playerChoice == "left") {
// 		cout << "You discover a hidden treasure chest!" << endl;
// 		cout << "Inside you find 100 gold coins." << endl;
// 	} 
// 	else if (playerChoice == "right") {
// 		cout << "You meet a wise old sage." << endl;
// 		cout << "The sage gives you a magical potion." << endl;
// 	} 
// 	else {
// 		cout << "You stand still, unsure of your choice." << endl;
// 		cout << "Time passes and nothing happens." << endl;
// 	}

// 	return 0;
// }

// #include <iostream>
// using namespace std;

// int main() {
// 	int menuChoice;

// 	cout << "=== GAME MENU ===" << endl;
// 	cout << "1. Start New Game" << endl;
// 	cout << "2. Load Game" << endl;
// 	cout << "3. View High Scores" << endl;
// 	cout << "4. Settings" << endl;
// 	cout << "5. Exit Game" << endl;
//     cout << "6. Instructions" << endl;
// 	cout << "Enter your choice (1-6): ";

// 	cin >> menuChoice;

// 	switch (menuChoice) {
// 		case 1:
// 			cout << "Starting new adventure..." << endl;
// 			cout << "Welcome, brave explorer!" << endl;
// 			break;

// 		case 2:
// 			cout << "Loading saved game..." << endl;
// 			cout << "Game loaded successfully." << endl;
// 			break;

// 		case 3:
// 			cout << "=== HIGH SCORES ===" << endl;
// 			cout << "1. Alice - 15,000 points" << endl;
// 			cout << "2. Bob - 12,500 points" << endl;
// 			break;

// 		case 4:
// 			cout << "Opening settings menu..." << endl;
// 			cout << "Sound: ON, Difficulty: Medium" << endl;
// 			break;

// 		case 5:
// 			cout << "Thanks for playing! Goodbye!" << endl;
// 			break;

//         case 6:
//             cout << "=== INSTRUCTIONS ===" << endl;
//             cout << "Enter the number of the option that you want to chose" << endl;

// 		default:
// 			cout << "Invalid choice! Please select 1-5." << endl;
// 			break;
// 	}

// 	return 0;
// }

#include <iostream>
using namespace std;

int main() {
	int playerLevel;
	char difficulty;

	// Get player level with validation
	cout << "Enter your player level (1-20): ";
	cin >> playerLevel;

	if (playerLevel < 1 || playerLevel > 20) {
		cout << "Invalid level! Setting to level 1." << endl;
		playerLevel = 1;
	} 
    else if (playerLevel > 15) {
        cout << "Unlocked Bonusses for high levels (level 15 and higher)" << endl;
    }

	// Get difficulty choice
	cout << "Choose difficulty:" << endl;
	cout << "E - Easy" << endl;
	cout << "M - Medium" << endl;
	cout << "H - Hard" << endl;
	cout << "Enter choice (E/M/H): ";
	cin >> difficulty;

	// Process difficulty with switch
	switch (difficulty) {
		case 'E':
		case 'e':
			cout << "Easy mode selected." << endl;
			if (playerLevel >= 5) {
				cout << "Bonus: Extra health for experienced player!" << endl;
			}
			break;

		case 'M':
		case 'm':
			cout << "Medium mode selected." << endl;
			if (playerLevel >= 7) {
				cout << "Bonus: Special weapon unlocked!" << endl;
			}
			break;

		case 'H':
		case 'h':
			cout << "Hard mode selected. Good luck!" << endl;
			if (playerLevel >= 8) {
				cout << "Bonus: Elite status achieved!" << endl;
			} else {
				cout << "Warning: This will be challenging for your level." << endl;
			}
			break;

		default:
			cout << "Invalid choice! Defaulting to Easy mode." << endl;
			break;
	}

	cout << "Game starting with Level " << playerLevel << " character..." << endl;

	return 0;
}