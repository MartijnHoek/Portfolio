// #include <iostream>
// using namespace std;
// int main() {
//     int score1, score2, score3;
//     cout << "Enter three test scores: ";
//     cin >> score1 >> score2 >> score3;
//     double average = (score1 + score2 + score3) / 3;
//     cout << "Average score: " << average << endl;
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main() {
//     int temperature;
//     cout << "Enter temperature in Celsius: ";
//     cin >> temperature;
//     // Convert to Fahrenheit
//     int fahrenheit = temperature * 9.0 / 5.0  + 32;  // Formula error    
//     cout << temperature << "°C = " << fahrenheit << "°F" << endl;
//     return 0;
// }

#include <iostream>
using namespace std;
int main() {
    int dividend, divisor;
    cout << "Enter two numbers for division: ";
    cin >> dividend >> divisor;

    if (divisor == 0) {
        cout << "Error: Division by zero is not allowed." << endl;
    } 
    else {
        int result = dividend / divisor;
        cout << dividend << " / " << divisor << " = " << result << endl;
    }
    
    return 0;
}