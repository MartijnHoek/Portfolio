#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <filesystem>

using namespace std;

int main() {
    const string inputFile = "inventory.txt";
    const string outputFile = "summary.txt";

    // Check if input file exists using C++17 filesystem
    if (!filesystem::exists(inputFile)) {
        cout << "Creating sample inventory file..." << endl;
        ofstream createFile(inputFile);
        createFile << "Widget A,25,15.50" << endl;
        createFile << "Widget B,40,22.00" << endl;
        createFile << "Widget C, 15,8.75" << endl;
        createFile.close();
    }

    // Read inventory data
    ifstream inFile(inputFile);
    if (!inFile.is_open()) {
        cerr << "Error opening inventory file" << endl;
        return 1;
    }

    // Process and summarize
    ofstream outFile(outputFile);
    if (!outFile) {
        cerr << "Error creating summary file" << endl;
        return 1;
    }

    outFile << "INVENTORY SUMMARY" << endl;
    outFile << "=================" << endl;
    string line;
    int totalItems = 0;
    double totalValue = 0.0;
    while (getline(inFile, line)) {
        // Simple CSV parsing (find commas)
        size_t firstComma = line.find(',');
        size_t secondComma = line.find(',', firstComma + 1);
        if (firstComma != string::npos && secondComma != string::npos) {
            string name = line.substr(0, firstComma);
            int quantity = stoi(line.substr(firstComma + 1, secondComma - firstComma - 1));\
            double price = stod(line.substr(secondComma + 1));
            totalItems += quantity;
            totalValue += quantity * price;
            outFile << "Product " << name << ", Qty: " << quantity
                    << ", Value: $" << fixed << setprecision(2)
                    << quantity * price << endl;
        }
    }

    outFile << endl << "Total Items: " << totalItems << endl;
    outFile << "Total Value: $" << fixed << setprecision(2) << totalValue << endl;
    inFile.close();
    outFile.close();
    cout << "Inventory summary completed!" << endl;
    cout << "Check summary.txt for results." << endl;
    return 0;
}





// int main() {
//     ofstream reportFile("sales_report.txt");
//     if (!reportFile) {
//         cerr << "Error: Could not create sales report file" << endl;
//         return 1;
//     }

//     // Write report header
//     reportFile  << "DAILY SALES REPORT" << endl;
//     reportFile  << "==================" << endl;
//     reportFile  << left << setw(15) << "Product"
//                 << setw(10) << "Quantity"
//                 << setw(10) << "Price" << endl;

//     // Sample sales data
//     reportFile  << left << setw(15) << "Laptop"
//                 << setw(10) << "5"
//                 << "$" << fixed << setprecision(2) << 999.99 << endl;

//     reportFile  << left << setw(15) << "Mouse" 
//                 << setw(10) << "12"
//                 << "$" << fixed << setprecision(2) << 29.99 << endl;
    

//     reportFile  << left << setw(15) << "Keyboard" 
//                 << setw(10) << "4"
//                 << "$" << fixed << setprecision(2) << 49.99 << endl;

//     reportFile.close();

//     // Append to existing file
//     ofstream appendFile("sales_report.txt", ios::app);
//         if (!appendFile) {
//         cerr << "Error: Could not append to sales report file" << endl;
//         return 1;
//     }

//     appendFile  << left << setw(15) << "Monitor"
//                 << setw(10) << "54"
//                 << "$" << fixed << setprecision(2) << 12.12 << endl;
    


//     cout << "Sales report file generated succesfully!" << endl;
//     return 0;
// }


// int main() {
//     ifstream inputFile("products.txt");
//     if (!inputFile.is_open()) {
//         cerr << "Error: Could not open products.txt" << endl;
//         return 1;
//     }

//     string productName;
//     int count = 0;
//     cout << "Product Inventory:" << endl;
//     while (getline(inputFile, productName)) {
//         count++;
//         cout << count << ". " << productName << endl;
//     }
//     inputFile.close();
//     cout << "Total products: " << count << endl;
//     return 0;

// }