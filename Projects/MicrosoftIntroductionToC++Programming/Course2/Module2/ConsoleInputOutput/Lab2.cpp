#include <iostream>
#include <iomanip>
#include <limits>
#include <string>

using namespace std;

int main() {
    string name, email, complete_dob;
    int date_of_birth_day, date_of_birth_month, date_of_birth_year, score;


    cout << setfill('-') << setw(40) << "" << endl;
    cout << setfill(' ') <<  "EMPLOYEE REPORT" << endl;
    cout << setfill('-') << setw(40) << "" << endl;

    // Name
    cout << "Enter your name: ";
    do {
        getline(cin, name);

        if (name.empty()) {
            cout << "[i] Invalid input. please enter you name: ";
        }
    } while (name.empty());

    // E-mail
    cout << "Enter your e-mail adress: ";
    while (!(cin >> email) || email.find('@') == string::npos) {
        cin.clear();
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        cout << "[i] Invalid input. Please enter your e-mail: ";
    }

    // Date of birth
    cout << "Enter your date of birth (dd mm yyyy): ";
    while (!(cin >> date_of_birth_day >> date_of_birth_month >> date_of_birth_year) || 
    date_of_birth_day < 1 || date_of_birth_day > 31 || date_of_birth_month < 1 || date_of_birth_month > 12 ||
    date_of_birth_year < 0 || date_of_birth_year > 2026) {
        cin.clear();
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        cout << "[i] Invalid input. Please enter your date of birth following the dd mm yyyy: ";
    }
    complete_dob = to_string(date_of_birth_day) + "-" + to_string(date_of_birth_month) + "-" + to_string(date_of_birth_year);

    // Score input
    std::cout << "Enter Score: ";
    while (!(std::cin >> score) || score < 0) {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Invalid input. Please enter a valid score: ";
    }

    // Output
    cout << setfill(' ');   // Reset the setfill()
    cout << fixed << setprecision(2);
    cout << setw(15) << left << "Name"
         << setw(30) << "Email"
         << setw(15) << "Date of birth"
         << setw(10) << "Score" << endl;

    cout << setw(15) << left << name
         << setw(30) << email
         << setw(15) << complete_dob
         << setw(10) << score << endl;


    return 0;    
}