#include <iostream>

int main() {
    // Create a 5x5 seating chart (0 = available, 1 = occupied)
    int seating[5][5] = {
        {0, 1, 0, 1, 0},
        {1, 1, 0, 0, 1},
        {0, 0, 1, 1, 0},
        {1, 0, 0, 1, 1},
        {0, 1, 1, 0, 0}
    };
    // Check specific seats (row 2, colum 3) and (row 4, column 1)
    std::cout << "Seat at row 2, column 3: " << seating[1][2] << std::endl;
    std::cout << "Seat at row 4, column 1: " << seating[3][0] << std::endl;
    // Check specific seats (row 1, colum 4) and (row 5, column 2)
    std::cout << "Seat at row 1, column 4: " << seating[0][3] << std::endl;
    std::cout << "Seat at row 5, column 2: " << seating[4][1] << std::endl;

    // Reserve seat at row 3, column 2
    seating[2][1] = 1;
    std::cout << "Reserved seat at row 3, column 2" << std::endl;

    // Free up seat at row 2, column 1
    seating[1][0] = 0;
    std::cout << "Freed seat at row 2, column 1" << std::endl;

    std::cout << "Theater seating chart initialized!" << std::endl;
    std::cout << "0 = Available, 1 = Occupied" << std::endl;
    
    // Row-major traversale (row by row)
    std::cout << "Seating chart (row by row): " << std::endl;
    for (int row = 0; row < 5; row++) {
        std::cout << "Row " << (row + 1) << ": ";
        for (int col = 0; col < 5; col++) {
            std::cout << seating[row][col] << " ";
        }
        std::cout << std::endl;
    }
    
    std::cout << "\nSeating chart (column by column): " << std::endl;
    for (int col = 0; col < 5; col++) {
        std::cout << "Column " << (col + 1) << ": ";
        for (int row = 0; row < 5; row++) {
            std::cout << seating[row][col] << " ";
        }
        std::cout << std::endl;
    }
    
    // Count total available and occupied seats
    int available = 0, occupied = 0;
    for (int row = 0; row < 5; row++) {
        for (int col = 0; col < 5; col++) {
            if (seating[row][col] == 0) {
                available++;
            } 
            else {
                occupied++;
            }
        }
    }
    std::cout << "\nSummary: " << available << " available, " << occupied << " occupied" << std::endl;

    // Safe access function
    auto getSeat = [&](int row, int col) -> int {
        if (row >= 0 && row < 5 && col >= 0 && col < 5) {
            return seating[row][col];
        }
        else {
            std::cout << "Invalid seating position: row " << row << " , col " << col << std::endl;
            return -1; // Error value
        }
    };

    // Test valid access
    std::cout << "Valid access - Row 2, Col 3: " << getSeat(1, 2) << std::endl;
    // Test invalid access
    std::cout << "Valid access - Row 6, Col 3: " << getSeat(5, 2) << std::endl;
    std::cout << "Valid access - Row 3, Col 8: " << getSeat(2, 7) << std::endl;
    std::cout << "Valid access - Row -1, Col 2: " << getSeat(-1, 1) << std::endl;


    return 0;
}