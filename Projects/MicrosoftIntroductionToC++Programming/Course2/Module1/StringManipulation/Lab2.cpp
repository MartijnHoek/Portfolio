#include<string>
#include<iostream>
#include <sstream>
#include <map>

using namespace std;

int wordCounter(string text) {
   for (char& c : text) {
        if (ispunct(c)) {
            c = ' ';
        }
    }

    istringstream iss(text);
    
    string word;
    int word_count = 0;

    while (iss >> word) {
        word_count++;
    }

    return word_count;
}

map<char, int> countCharacters(const string& text) {
    map<char, int> frequency;

    for (char c : text) {
        // ignore non-alphabet
        if (isalpha(c)) {
            c = tolower(c);

            // Count
            frequency[c]++;
        }
    }
    return frequency;
}

int averageWordLength(string text) {
    int total_word_length = 0;
    double average_word_length = 0.00;
    string word;


    // Remove delimiters
    for (char& c : text) {
    if (ispunct(c)) {
        c = ' ';
        }
    }

    istringstream iss(text);

    while (iss >> word) {
        total_word_length = total_word_length + word.length();
    }

    average_word_length = total_word_length / wordCounter(text);

    return average_word_length;
}


int main() {
    string text = "Hello my dear world!";

    cout << "Amount of words in the string are: " << wordCounter(text) << endl;

    map<char, int> letter_count = countCharacters(text);

    for (auto pair : letter_count) {
        cout << pair.first << " : " << pair.second << endl;
    }

    cout << "Average word length is: " << averageWordLength(text) << endl;

    return 0;
}