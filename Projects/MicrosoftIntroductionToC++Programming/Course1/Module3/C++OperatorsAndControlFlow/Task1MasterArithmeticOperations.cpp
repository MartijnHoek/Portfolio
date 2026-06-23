// #include <iostream>
// using namespace std;
// int main() {
//     // Player statistics
//     int baseScore = 90;
//     int bonusPoints = 15;
//     int timeBonus = 10; 
//     int multiplier = 5;
//     // Basic calculations
//     int totalScore = baseScore + bonusPoints + timeBonus;
//     cout << "Total Score: " << totalScore << endl;  
//     // Division and modulus examples
//     double averageScore = totalScore / 3.0;  // Integer division
//     int remainder = totalScore % 10;    // Remainder when divided by 10    
//     int scoreMultiplier = totalScore * multiplier;
//     cout << "Average per section: " << averageScore << endl;
//     cout << "Score remainder: " << remainder << endl;   
//     cout << "Score with multiplier: " << scoreMultiplier << endl;   
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main() {
//     // Player attributes
//     int playerLevel = 3;
//     int playerScore = 1250;
//     int minimumLevel = 5;
//     int minimumScore = 1000;
//     bool hasCompleteMap = false; 
//     // Relational comparisons
//     bool levelQualified = playerLevel >= minimumLevel;
//     bool scoreQualified = playerScore >= minimumScore;  
//     cout << "Level qualified: " << (levelQualified ? "Yes" : "No") << endl;
//     cout << "Score qualified: " << (scoreQualified ? "Yes" : "No") << endl; 
//     // Logical combinations
//     bool basicAchievement = levelQualified && scoreQualified;
//     bool specialAchievement = basicAchievement && hasCompleteMap;
//     bool eliteAchievement = playerScore > 1500;
//     bool anyQualification = levelQualified || scoreQualified;
//     bool beginner = playerLevel >! minimumLevel;

//     cout << "Basic achievement: " << (basicAchievement ? "Earned" : "Not earned") << endl;
//     cout << "Special achievement: " << (specialAchievement ? "Earned" : "Not earned") << endl;
//     cout << "Elite achievement: " << (eliteAchievement ? "Earned" : "Not earned") << endl;
//     cout << "Any qualification: " << (anyQualification ? "Yes" : "No") << endl; 
//     cout << "Beginner player: " << (beginner ? "Yes" : "No") << endl; 

//     return 0;
// }

#include <iostream>
using namespace std;
int main() {
    // Demonstrate precedence in arithmetic operations
    int baseDamage = 10;
    int weaponBonus = 5;
    int strengthMultiplier = 2;
    // Without parentheses - multiplication happens first
    int damage1 = baseDamage + weaponBonus * strengthMultiplier;
    cout << "Damage without parentheses: " << damage1 << endl;
    // With parentheses - addition happens first
    int damage2 = (baseDamage + weaponBonus) * strengthMultiplier;
    cout << "Damage with parentheses: " << damage2 << endl;
    // Complex expression with multiple operators
    int level = 5;
    int experience = 100;
    bool isAdvanced = level > 3 && experience >= (50 * 2);
    cout << "Advanced player: " << (isAdvanced ? "Yes" : "No") << endl;
    return 0;
}