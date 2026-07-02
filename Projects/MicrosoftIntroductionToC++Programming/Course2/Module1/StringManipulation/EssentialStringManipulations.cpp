#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cctype>

// int main () {
//     std::string message = "Welcome to the world of C++ programming!";
//     std::cout << "Original message: " << message << std::endl;
//     // Extract the first word using substr()
//     size_t first_space = message.find(' ');
//     if (first_space != std::string::npos) {
//         std::string first_word = message.substr(0, first_space);
//         std::cout << "First word: " << first_word << std::endl;
//     }

//     size_t last_space = message.rfind(' ');
//     if (last_space != std::string::npos) {
//         std::string last_word = message.substr(last_space + 1);
//         std::cout << "Last word: " << last_word << std::endl;
//     }

//     int oCount = 0;

//     for (char c : message) {
//         if (c == 'o' || c == 'O') {
//             oCount++;
//         }
//     }
//     std::cout << "Amount of o/O in the string is: " << oCount << std::endl;

// }

// int main() {
//     std::string text = "Hello world! The world is beautiful.";
//     std::cout << "Original: " << text << std::endl;
//     // Replace "world" with "universe"
//     size_t pos = text.find("world");
//     if (pos != std::string::npos) {
//         text.replace(pos, 5, "universe");
//         std::cout << "After first replacement: " << text << std::endl;
//     }

//     pos = text.find("world", pos + 8); // After the first replacement
//     if (pos != std::string::npos) {
//         text.replace(pos, 5, "universe");
//         std::cout << "After second replacement: " << text << std::endl;
//     }

//     // Remove exclamation marks
//     size_t exclamations_pos = text.find('!');
//     while (exclamations_pos != std::string::npos) {
//         text.erase(exclamations_pos, 1);
//         exclamations_pos = text.find('!', exclamations_pos);
//     }

//     for (char& c : text) {
//         c = std::toupper(c);
//     }
//     std::cout << "Uppercase: " << text << std::endl;

//     return 0;
// }

// int main() {
//     // C-style string operations
//     const char* c_str = "Hello";
//     char c_buffer[20];
//     strcpy(c_buffer, c_str);
//     strcat(c_buffer, " World");
//     std::cout << "C-style result: " << c_buffer << std::endl;
//     std::cout << "C-style length: " << strlen(c_buffer) << std::endl;

//     // std::string operations
//     std::string cpp_str = "Hello";
//     cpp_str += " World";
//     std::cout << "std::string result: " << cpp_str << std::endl;
//     std::cout << "std::string length: " << cpp_str.length() << std::endl;

//     try {
//         if (cpp_str.at(15)) {
//             std::cout << "Index 15 with library " << (cpp_str.at(15)) << std::endl;
//         }
//     }
//     catch (const std::out_of_range) {
//         std::cout << "Error when trying to get index 15 in library string" << std::endl;
//     }

//     // Your code here: Show what happens when you try to concatenate 
//     // a very long string to c_buffer (comment out to avoid crash)
//     // strcat(c_buffer, " This is a very long string that will cause overflow");
//     return 0;
// }


int main() {
    std::string text = "The Quick Brown Fox Jumps Over The Lazy Dog";
    std::cout << "Analyzing: " << text << std::endl;

    // Count words (spaces + 1)
    int word_count = std::count(text.begin(), text.end(), ' ') + 1;
    std::cout << "Word count: " << word_count << std::endl;

    // Find the amount of vowels in text
    int vowelCount = 0;
    for (char c : text) {
        c = std::toupper(c);
        if (c == 'A') {
            vowelCount++;
        }
        else if (c == 'E') {
            vowelCount++;
        }
        else if (c == 'I') {
            vowelCount++;
        } 
        else if (c == 'O') {
            vowelCount++;
        }
        else if (c == 'U') {
            vowelCount++;
        }
    }
    std::cout << "Amount of vowels in text are: " << vowelCount << std::endl;

    std::string longestWord = "";
    size_t start = 0;
    size_t pos = 0;
    while ((pos = text.find(' ', start)) != std::string::npos) {
        std::string word = text.substr(start, pos - start);
        if (word.length() > longestWord.length()) {
            longestWord = word;
        }
        start = pos + 1;
    }
    // Check last word
    std::string last_word = text.substr(start);
    if (last_word.length() > longestWord.length()) {
        longestWord = last_word;
    }
    std::cout << "Longest word is: " << longestWord << std::endl;

}