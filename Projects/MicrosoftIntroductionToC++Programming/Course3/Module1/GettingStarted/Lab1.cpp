#include <iostream>
#include <string>
#include <vector>

class Student {
private:
    std::string name;
    int studentId;
    std::vector<double> grades;

public:
    // Constructor
    Student(std::string studentName, int id) : name(studentName), studentId(id) {
        std::cout << "Student " << name << " enrolled with ID: " << studentId << std::endl; 
    }

    // Add a grade
    void addGrade(double grade) {
        if (grade >= 0.0 && grade <= 100.0) {
            grades.push_back(grade);
            std::cout << "Grade " << grade << " added for " << name << std::endl;
        } else {
            std::cout << "Invalid grade. Must be between 0 and 100." << std::endl;
        }
    }
    
    // Calculate the average grade
    double calculateAverage() const {
        if (grades.empty()) return 0.0;

        double sum = 0.0;
        for (double grade: grades) {
            sum += grade;
        }
        return sum / grades.size();
    }

    // Display student information
    void displayStudent() const {
        std::cout << "Student: " << name << " (ID: " << studentId << ")" << std::endl;
        std::cout << "Number of grades: " << grades.size() << std::endl;
        std::cout << "Average grade: " << calculateAverage() << std::endl;
    }
};

int main() {

    Student student1("Martijn", 23);
    Student student2("Jan Arie", 34);

    // Student 1 grades
    student1.addGrade(45);
    student1.addGrade(22);
    student1.addGrade(100);
    student1.addGrade(99);
    student1.addGrade(120);
    
    // Student 2 grades
    student2.addGrade(10);
    student2.addGrade(44);
    student2.addGrade(44);
    student2.addGrade(55);
    student2.addGrade(-10);

    // Display info
    student1.displayStudent();
    student2.displayStudent();

    return 0;
}




// #include <iostream>
// #include <string>

// class Book {
// private:
//     std::string title;
//     std::string author;
//     int pages;
//     bool isAvailable;

// public:
//     // Parameterized constructor
//     Book(std::string bookTitle, std::string bookAuthor, int pageCount) : title(bookTitle), author(bookAuthor), pages(pageCount), isAvailable(true)  {
//     }

//     // Getter methods
//     std::string getTitle() const { return title; }
//     std::string getAuthor() const { return author; }
//     int getPages() const { return pages; }
//     bool getAvailability() const {return isAvailable; }

//     // Setter methodds
//     void setPages(int newPages) {
//         if (newPages > 0) {
//             pages = newPages;
//         }
//     }
//     void setAvailability(bool status) {
//         isAvailable = status;
//     }

//     // Display book information
//     void displayInfo() const {
//         std::cout << "Title: " << title << std::endl;
//         std::cout << "Author: " << author << std::endl;
//         std::cout << "Pages: " << pages << std::endl;
//         std::cout << "Available: " << (isAvailable ? "Yes" : "No") << std::endl;
//         std::cout << "------------------------" << std::endl;
//     }
// };

// int main() {
//     // Create book objects
//     Book book1("The C++ Programming Language", "Bjarne Stroustrup", 1376);
//     Book book2("Clean Code", "Robert C. Martin", 464);
    
//     // Display book information
//     book1.displayInfo();
//     book2.displayInfo();

//     // Demonstrate object interaction
//     std::cout << "Checking out: " << book1.getTitle() << std::endl;
//     book1.setAvailability(false);
//     book1.displayInfo();
//     return 0;
// }