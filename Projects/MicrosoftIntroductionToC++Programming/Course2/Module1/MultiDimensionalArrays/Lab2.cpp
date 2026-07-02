#include <iostream>

using namespace std;

void transposeMatrix(int matrix[3][3], int transposedMatrix[3][3]) {
    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 2; j++) {
            transposedMatrix[j][i] = matrix[i][j];
        }
    }
}


int main() {
    int matrix1[3][3] = {
        {3, 3, 3},
        {4, 5, 6},
        {1, 2, 3}
    };
    int matrix2[3][3] = {
        {2, 2, 2},
        {255, 105, 25},
        {201, 96, 76},
    };

    int matrixAdd[3][3];
    int matrixProduct[3][3];

    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 2; j++) {
            matrixAdd[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }

    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 2; j++) {
            matrixProduct[i][j] = matrix1[i][j] * matrix2[i][j];
        }
    }

    // Print result matrix
    cout << "Sum matrix" << endl;
    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 2; j++) {
            std::cout << matrixAdd[i][j] << " ";
        }
        std::cout << std::endl;
    }

    cout << "Product matrix" << endl;
    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 2; j++) {
            std::cout << matrixProduct[i][j] << " ";
        }
        std::cout << std::endl;
    }

    // Transpose matrix
    int transposedMatrix1[3][3];
    int transposedMatrix2[3][3];

    transposeMatrix(matrix1, transposedMatrix1);
    transposeMatrix(matrix2, transposedMatrix2);

    cout << "Matrix 1" << endl;
    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 2; j++) {
            std::cout << matrix1[i][j] << " ";
        }
        std::cout << std::endl;
    }
    cout << "Transposed matrix 1" << endl;
    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 2; j++) {
            std::cout << transposedMatrix1[i][j] << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}