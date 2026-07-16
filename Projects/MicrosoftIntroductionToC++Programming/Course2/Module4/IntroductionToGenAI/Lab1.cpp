// student_management.cpp
#include <iostream>
#include <string>
#include <vector>

// // main.cpp - Mathematical Utility Library
// #include <iostream>
// #include <vector>
// #include <cmath>
// // TODO: Use AI to generate the following functions:
// // 2. Function to check if a number is prime
// // 3. Function to calculate average of a vector of numbers
// // Iterative factorial: returns n! (for n up to 20 safely in 64-bit)
// unsigned long long factorial(unsigned int n) {
//     unsigned long long result = 1;
//     for (unsigned int i = 2; i <= n; ++i) result *= i;
//     return result;
// }
// // Check whether n is prime (simple trial division)
// bool isPrime(unsigned int n) {
//     if (n < 2) return false;
//     if (n % 2 == 0) return n == 2;
//     for (unsigned int i = 3; i * i <= n; i += 2) {
//         if (n % i == 0) return false;
//     }
//     return true;
// }

// // Calculate average of a vector of doubles. Returns 0.0 for empty vector.
// double calculateAverage(const std::vector<double>& v) {
//     if (v.empty()) return 0.0;
//     double sum = 0.0;
//     for (double x : v) sum += x;
//     return sum / static_cast<double>(v.size());
// }
// int main() {
//     std::cout << "Mathematical Utility Library" << std::endl;
//     // Test factorial function
//     std::cout << "Testing factorial function..." << std::endl;
// student_management.cpp
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

class Student {
private:
	std::string name_;
	int id_;
	std::vector<double> grades_;
public:
	Student(const std::string& name, int id) : name_(name), id_(id) {}
	void addGrade(double g) { grades_.push_back(g); }
	double calculateGPA() const {
		if (grades_.empty()) return 0.0;
		double sum = 0.0;
		for (double g : grades_) sum += g;
		return sum / static_cast<double>(grades_.size());
	}
	void displayInfo() const {
		std::cout << "Name: " << name_ << ", ID: " << id_ << ", Grades: ";
		if (grades_.empty()) {
			std::cout << "(none)";
		} else {
			for (size_t i = 0; i < grades_.size(); ++i) {
				if (i) std::cout << ", ";
				std::cout << grades_[i];
			}
		}
		std::cout << ", Avg: " << std::fixed << std::setprecision(2) << calculateGPA() << std::defaultfloat << std::endl;
	}
	const std::string& getName() const { return name_; }
	int getId() const { return id_; }
};

class StudentManager {
private:
	std::vector<Student> students_;
public:
	void addStudent(const Student& s) { students_.push_back(s); }
	// Returns pointer to student in container or nullptr if not found
	Student* findStudent(int id) {
		for (auto& s : students_) if (s.getId() == id) return &s;
		return nullptr;
	}
	void displayAllStudents() const {
		if (students_.empty()) {
			std::cout << "No students available." << std::endl;
			return;
		}
		for (const auto& s : students_) s.displayInfo();
	}
};

int main() {
	std::cout << "Student Management System" << std::endl;

	StudentManager mgr;

	Student s1("Alice", 1);
	s1.addGrade(3.7);
	s1.addGrade(3.9);

	Student s2("Bob", 2);
	s2.addGrade(2.8);
	s2.addGrade(3.2);
	s2.addGrade(3.0);

	Student s3("Carol", 3);
	// no grades yet for Carol

	mgr.addStudent(s1);
	mgr.addStudent(s2);
	mgr.addStudent(s3);

	std::cout << "\nAll students:\n";
	mgr.displayAllStudents();

	int queryId = 2;
	std::cout << "\nLooking up student with ID " << queryId << ":\n";
	Student* found = mgr.findStudent(queryId);
	if (found) found->displayInfo();
	else std::cout << "Student not found." << std::endl;

	return 0;
}
