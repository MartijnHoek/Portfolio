#include <iostream>
#include <ctime>

using namespace std;

int weddingDateCalculator() {
    int d, m, y;

    cout << "==== DAYS TILL WEDDING DATE CALCULATOR ====" << endl;
    cout << "Enter current date (dd mm yyyy): ";
    cin >> d >> m >> y;

    tm current = {};
    current.tm_mday = d;
    current.tm_mon = m - 1;   // months start at 0
    current.tm_year = y - 1900;

    tm target = {};
    target.tm_mday = 15;
    target.tm_mon = 4;       // months start at 0 so december is 11 for example
    target.tm_year = 2027 - 1900;

    time_t currentTime = mktime(&current);
    time_t targetTime = mktime(&target);

    double seconds = difftime(targetTime, currentTime);
    int days = seconds / (60 * 60 * 24);

    if (days > 0)
        cout << days << " days remaining.\n";
    else if (days == 0)
        cout << "Today is the target date!\n";
    else
        cout << -days << " days past the target date.\n";

    return 0;
}