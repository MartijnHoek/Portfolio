#include <iostream>
#include <chrono>
using namespace std;
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
int main() {
    int n = 35; 
    auto start = chrono::high_resolution_clock::now();
    int result = fibonacci(n);
    auto end = chrono::high_resolution_clock::now();    
    auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);   
    cout << "Fibonacci(" << n << ") = " << result << endl;
    cout << "Execution time: " << duration.count() << " ms" << endl;
    return 0;
}