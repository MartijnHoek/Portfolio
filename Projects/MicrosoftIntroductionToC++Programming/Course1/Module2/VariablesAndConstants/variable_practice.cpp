// #include <iostream>
// int main() {
//     // Declare and initialize variables for player data
//     int playerLevel = 5;
//     double experiencePoints = 1250.75;
//     char difficultyRating = 'B';
//     bool hasCompletedTutorial = true;
//     float playerSpeed = 10.4;
//     short amountOfLives = 3;
//     char playerRating = 'C';

//     // Display the player information
//     std::cout << "Player Profile:" << std::endl;
//     std::cout << "Level: " << playerLevel << std::endl;
//     std::cout << "Experience: " << experiencePoints << std::endl;
//     std::cout << "Difficulty Rating: " << difficultyRating << std::endl;
//     std::cout << "Completed Tutorial: " << hasCompletedTutorial << std::endl;
//     std::cout << "Player Speed: " << playerSpeed << std::endl;
//     std::cout << "Amount of lives: " << amountOfLives << std::endl;
//     std::cout << "Player rating: " << playerRating << std::endl;
    
//     return 0;
// }


#include <iostream>
int main() {
    // Constants for game configuration
    const int MAX_PLAYER_LEVEL = 100;
    const double EXPERIENCE_MULTIPLIER = 1.5;
    const char GOLD_TIER_RATING = 'A';
    // Using auto for type deduction    
    auto currentScore = 98500;      // Compiler deduces int
    auto averagePlayTime = 45.5;    // Compiler deduces double
    auto playerInitial = 'M';       // Compiler deduces char
    auto isOnline = false;          // Compiler deduces bool    
    // Display constants
    std::cout << "Game Configuration:" << std::endl;
    std::cout << "Max Level: " << MAX_PLAYER_LEVEL << std::endl;
    std::cout << "Experience Multiplier: " << EXPERIENCE_MULTIPLIER << std::endl;   
    // Display auto variables
    std::cout << "\nPlayer Data (using auto):" << std::endl;
    std::cout << "Score: " << currentScore << std::endl;
    std::cout << "Average Play Time: " << averagePlayTime << " hours" << std::endl;
    std::cout << "Initial: " << playerInitial << std::endl;
    std::cout << "Online Status: " << isOnline << std::endl;    
    return 0;
}