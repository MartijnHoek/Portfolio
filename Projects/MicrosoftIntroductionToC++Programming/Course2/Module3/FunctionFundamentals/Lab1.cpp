#include <iostream>
#include <string>
#include <vector>

// Struct to return multiple employee statistics
struct EmployeeStats {
    double averageScore;
    double highestScore;
    double lowestScore;
    int totalEvaluations;
};

// Function returning multiple values using a struct
EmployeeStats calculateEmployeeStats(const std::vector<double>& scores) {
    if (scores.empty()) {
        return {0.0, 0.0, 0.0, 0};
    } else {
        for (double score : scores) {
            if (score < 0 || score > 100) {
                return {0.0, 0.0, 0.0, 0};
            }
        }
    }
    double sum = 0.0;
    double highest = scores[0];
    double lowest = scores[0];
    for (double score: scores) {
        sum += score;
        if (score > highest) highest = score;
        if (score < lowest) lowest = score;
    }
    return {
        sum / scores.size(),                // Average
        highest,                            // Highest
        lowest,                             // Lowest
        static_cast<int>(scores.size())     // Total count
    };
}

// Function that validates and processes employee data
bool processEmployeeData(int& employeeId, std::string& name, double& salary) {
    // Validate input data
    if (employeeId <= 0 || name.empty() || salary < 0) {
        return false;
    }
    // Process the data (example: format name and adjust salary)
    // Convert name to tile case (simplified)
    if (!name.empty()) {
        name[0] = std::toupper(name[0]);
    }
    // Ensure minimum salary
    if (salary < 30000.0) {
        salary = 30000.0;
    }
    return true;
}

int main() {
    // Test multiple return values
    std::vector<double> employeeScores = {87.5, 92.0, 78.5, 95.0, 84.0, 89.5};
    EmployeeStats stats = calculateEmployeeStats(employeeScores);
    std::cout << "Employee Performance Statistics:" << std::endl;
    std::cout << "Average Score: " << stats.averageScore << std::endl;
    std::cout << "Highest Score: " << stats.highestScore << std::endl;
    std::cout << "Lowest Score: " << stats.lowestScore << std::endl;
    std::cout << "Total Evaluations: " << stats.totalEvaluations << std::endl;
    // Test validation and processing function
    int id = 0;
    std::string name = "john doe";
    double salary = 25000.0;
    std::cout << "\nBefore processing:" << std::endl;
    std::cout << "ID: " << id << ", Name: " << name << ", Salary: $" << salary << std::endl;
    bool success = processEmployeeData(id, name, salary);
    if (success) {
        std::cout << "After processing:" << std::endl;
        std::cout << "ID: " << id << ", Name: " << name << ", Salary: $" << salary << std::endl;
    } else {
        std::cout << "Data processing failed - invalid input" << std::endl;
        // Try with valid data
        id = 102;
        name = "jane smith";
        salary = 45000.0;
        std::cout << "\nTrying with valid data:" << std::endl;
        std::cout << "Before ID: " << id << ", Name: " << name << ", Salary: $" << salary << std::endl;
        success = processEmployeeData(id, name, salary);
        if (success) {
            std::cout << "After ID: " << id << ", Name: " << name << ", Salary: $" << salary << std::endl;
        }
    }
    return 0;
}





// // Function using const reference for efficiency (no copying, no modification)
// void printEmployeeReport(const std::string& name, const std::vector<double>& scores) {
//     std::cout << "Performance Report for: " << name << std::endl;
//     std::cout << "Scores: ";
//     for (double score : scores) {
//         std::cout << score << " ";
//     }
//     std::cout << std::endl;
// }

// // Function using const reference to calculate the average score
// void printAverageScore(const std::vector<double>& scores) {
//     double total_score = 0;
    
//     for (double score: scores) {
//         total_score += score;
//     }

//     std::cout << "Average Score: " << total_score / scores.size() << std::endl;
// }

// // Function that increases the score
// void increaseScore(std::vector<double>& scores, int increase_value) {
//     for (double& score: scores) {
//         score += increase_value;
//     }
// }

// // Function using reference to modify original data
// void applyRaise(double& salary, double percentage) {
//     salary = salary * (1.0 + percentage / 100.0);
// }

// // Function using reference to modify vector elements
// void normalizeScores(std::vector<double>& scores) {
//     if (scores.empty()) return;
//     // Find maximum score
//     double maxScore = scores[0];
//     for (double score : scores) {
//         if (score > maxScore) {
//             maxScore = score;
//         }
//     }
//     // Normalize all scores to percentage of maximum
//     for (double& score : scores) {
//         score = (score / maxScore) * 100.0;
//     }
// }

// int main() {
//     std::string employeeName = "Bob Wilson";
//     std::vector<double> performanceScores = {85.0, 92.0, 78.0, 88.0, 95.0};
//     double currentSalary = 6000.0;
//     // Test const reference function
//     printEmployeeReport(employeeName, performanceScores);   
//     // Test reference modification
//     std::cout << "Original salary: $" << currentSalary << std::endl;
//     applyRaise(currentSalary, 8.5); // 8.5% raise
//     std::cout << "After raise: $" << currentSalary << std::endl;
//     // Test vector modification by reference
//     std::cout << "\nOriginal scores: ";
//     for (double score : performanceScores) {
//         std::cout << score << " ";
//     }
//     std::cout << std::endl;

//     // New code
//     printAverageScore(performanceScores);

//     increaseScore(performanceScores, 10);

//     std::cout << "\nIncreased scores: ";
//     for (double score : performanceScores) {
//         std::cout << score << " ";
//     }
//     std::cout << std::endl;

    
//     normalizeScores(performanceScores);
//     std::cout << "Normalized scores: ";
//     for (double score : performanceScores) {
//         std::cout << score << " ";
//     }
//     std::cout << std::endl;
//     return 0;
// }


// // Function to display employee information (pass-by-value for simple types)
// void displayEmployee(int id, std::string name, double salary) {
//     std::cout << "Employee ID: " << id << std::endl;
//     std::cout << "Name: " << name << std::endl;
//     std::cout << "Salary: $" << salary << std::endl;
//     std::cout << "------------------------" << std::endl;
// }
// // Function to calculate annual salary from monthly salary
// double calculateAnnualSalary(double monthlySalary) {
//     return monthlySalary * 12;
// }

// // Function to calculate a annual salary and returns a 10% bonus
// double calculateAnnualBonus(double annualSalary) {
//     return annualSalary * 0.10;
// }

// int main() {
//     // Test the functions
//     displayEmployee(101, "Alice Johnson", 5500.0);
//     double monthly = 4200.0;
//     double annual = calculateAnnualSalary(monthly);
//     double annual_bonus = calculateAnnualBonus(annual);
//     std::cout << "Monthly: $" << monthly << " -> Annual: $" << annual << "-> Annual Bonus (10%): $" << annual_bonus << std::endl;
//     return 0;
// }