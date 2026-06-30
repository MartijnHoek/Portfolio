#include <iostream>
using namespace std;

char getLetterGrade(int score) {
    /*
    Map the score against a letter grade
    Input: score (int)
    Output: grade (char)
    */ 
    if (score >= 90)
        return 'A';
    else if (score >= 80)
        return 'B';
    else if (score >= 70)
        return 'C';
    else if (score >= 60)
        return 'D';
    else
        return 'F';
}

int main() {
    // Your implementation here
    // Configuration properties
    int amountOfScores = 3;
    int scoreInput, score1, score2, score3, averageScore;
    bool validInput;
    char letterGrade;

    std::cout << " === Please enter your " << amountOfScores << " scores ===" << endl; 

    // Ask the user what their scores were
    for (int i = 1; i <= amountOfScores; i++) {
        do {
            std::cout << "Please enter score " << i << ":" << endl;
            // Validate if the input is a number between 0-100
            if (!(cin >> scoreInput)) {
                std::cout << "Invalid input, please enter a number!" << endl;
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
                validInput = false;
            }
            else if (scoreInput < 0 || scoreInput > 100) {
                validInput = false;
                std::cout << "Invalid score input, please try again!" << endl;
            }
            else {
                validInput = true;
                if (i == 1)
                    score1 = scoreInput;
                else if (i == 2)
                    score2 = scoreInput;
                else if (i == 3)
                    score3 = scoreInput;
            }
            
        } while (!validInput);  // Keep loop going till that a valid number is entered
    }
    // Calculate the average score and calculate the letter grade
    averageScore = (score1 + score2 + score3) / amountOfScores;
    letterGrade = getLetterGrade(averageScore);

    // Print results
    std::cout << "--- Score result ---" << endl;
    std::cout << "Average score: " << averageScore << endl;
    std::cout << "Letter grade: " << letterGrade << endl;
    
    return 0;
}