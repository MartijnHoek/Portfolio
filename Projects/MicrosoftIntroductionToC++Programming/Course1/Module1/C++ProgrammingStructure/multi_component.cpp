// Include necessary headers
#include <iostream>  // For input/output operations
#include <iomanip>   // For output formatting
#include <string>    // For string data type
#include <chrono>    // For time-related functions
#include <random>    // For random number generation

// Using the standard namespace
using namespace std;

int main() {
    // Program title and introduction
    cout << "================================================" << endl;
    cout << "           MULTI-COMPONENT PROGRAM              " << endl;
    cout << "================================================" << endl;
    cout << "This program demonstrates using multiple headers" << endl;
    cout << "and formatting techniques in C++." << endl << endl;
    
    // Component 1: Basic information display
    cout << "--------- COMPONENT 1: BASIC INFO ---------" << endl;

    // Create variables to store information
    /*
    A string is a sequence of characters
    A variable is a storage location that holds a value
    */

    string name = "C++ Programming";
    string version = "C++17";
    string creator = "Bjarne Stroustrup";
    int yearCreated = 1985;

    // Display the information
    cout << "Language: " << name << endl;
    cout << "Version: " << version << endl;
    cout << "Creator: " << creator << endl;
    cout << "Year Created: " << yearCreated << endl;

    // Add more variables and facts about C++
    string fact1 = "C++ is a general-purpose programming language.";
    bool fact2 = true; // C++ supports both procedural and object-oriented programming
    int fact3 = 100;

    // Display additional facts
    cout << "Interesting Fact 1: " << fact1 << endl;
    cout << "Interesting Fact 2: " << (fact2 ? "Yes" : "No") << endl;
    cout << "Interesting Fact 3: " << fact3 << endl;

    // Component 2: Formatted numeric output
    cout << "---------- COMPONENT 2: FORMATTED NUMBERS ---------" << endl;

    // Create numeric variables
    double pi = 3.14159265358979323846;
    double e = 2.71828182845904523536;
    double goldenRatio = 1.61803398874989484820;

    // Display with different precision
    cout << "Default display:" << endl;
    cout << "Pi = " << pi << endl;
    cout << "e = " << e << endl;
    cout << "Golden Ratio = " << goldenRatio << endl << endl;

    cout << "With 2 decimal places:" << endl;
    cout << fixed << setprecision(2);
    cout << "Pi = " << pi << endl;
    cout << "e = " << e << endl;
    cout << "Golden Ratio = " << goldenRatio << endl << endl;

    cout << "With 6 decimal places:" << endl;
    cout << fixed << setprecision(6);
    cout << "Pi = " << pi << endl;
    cout << "e = " << e << endl;
    cout << "Golden Ratio = " << goldenRatio << endl << endl;

    // Reset formatting
    cout.unsetf(ios::fixed);
    cout << setprecision(6);

    // Component 3: Table display
    cout << "------------- COMPONENT 3: TABLE DATA ------------" << endl;


    // Set up table header
    // setw sets the field witdth for the next output
    cout << left << setw(15) << "Data Type" << setw(20) << "Size (bytes)" << setw(20) << "Value Range" << endl;
    cout << string(55, '-') << endl;

    // Table rows
    cout << left << setw(15) << "int" << right << setw(20) << sizeof(int) << left << setw(20) << "  -2^31 to 2^31-1" << endl;
    cout << left << setw(15) << "double" << right << setw(20) << sizeof(double) << left << setw(20) << "  ±1.7e^308" << endl;
    cout << left << setw(15) << "char" << right << setw(20) << sizeof(char) << left << setw(20) << "  -128 to 127" << endl;
    cout << left << setw(15) << "bool" << right << setw(20) << sizeof(bool) << left << setw(20) << "  true or false" << endl;
    cout << left << setw(15) << "float" << right << setw(20) << sizeof(float) << left << setw(20) << "  1.2e-38 to 3.4e+38" << endl;
    cout << left << setw(15) << "string" << right << setw(20) << sizeof(string) << left << setw(20) << "  Variable length" << endl;


    // Component 4: Custom Component - Program Information
    cout << "------------- COMPONENT 4: PROGRAM INFO ------------" << endl;
    

    // Program end
    cout << "\nProgram execution completed." << endl;
    return 0;
}
