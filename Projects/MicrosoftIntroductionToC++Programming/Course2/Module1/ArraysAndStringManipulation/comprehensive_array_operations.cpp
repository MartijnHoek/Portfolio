#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

// Bubble sort function
void bubbleSort(int arr[], int size) {
   for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    } 
}

double mean_c_style(int arr[]) {
    int sum = 0;
    for (int i = 0; i <= 19; i++) {
        sum = sum + arr[i];
    }
    return sum / 20;
}

double mean_std_style(array<int, 20> arr) {
    int sum = 0;
    for (int i = 0; i <= 19; i++) {
        sum = sum + arr.at(i);
    }
    return sum / 20;
}


int main() {

    int c_style[20] = {3, 54, 65, 100, 1, 5, 64, 44, 88, 99, 81, 43, 2, 33, 25, 27, 30, 10, 34, 20};
    array<int, 20> std_style = {3, 54, 65, 100, 1, 5, 64, 44, 88, 99, 81, 43, 2, 33, 25, 27, 30, 10, 34, 20};

    cout << "C-style array  : ";
    for (int i = 0; i <=19; i++) {
        cout << c_style[i] << " ";
    }
    cout << endl;

    cout << "std-style array: ";
    for (int i = 0; i <=19; i++) {
        cout << std_style.at(i) << " ";
    }
    cout << endl;

    // Bubble sort
    bubbleSort(c_style, 20);

    // Using sort library
    sort(std_style.begin(), std_style.end());

    cout << "C-style array after sorting  : ";
    for (int i = 0; i <=19; i++) {
        cout << c_style[i] << " ";
    }
    cout << endl;

    cout << "std-style array after sorting: ";
    for (int i = 0; i <=19; i++) {
        cout << std_style.at(i) << " ";
    }
    cout << endl;

    // Mean   
    cout << "Mean C-style: " << mean_c_style(c_style) << endl;
    cout << "Mean std-style: " << mean_std_style(std_style) << endl;
    return 0;
}