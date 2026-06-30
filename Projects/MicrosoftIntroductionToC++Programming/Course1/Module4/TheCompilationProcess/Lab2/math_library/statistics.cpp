#include "statistics.h"
double average(double values[], int count) {
    if (count <= 0) return 0;   
    double sum = 0;
    for (int i = 0; i < count; i++) {
        sum += values[i];
    }
    return sum / count;
}
double minimum(double values[], int count) {
    if (count <= 0) return 0;
    double min = values[0];
    for (int i = 1; i < count; i++) {
        if (values[i] < min) {
            min = values[i];
        }
    }
    return min;
}
double maximum(double values[], int count) {
    if (count <= 0) return 0;   
    double max = values[0];
    for (int i = 1; i < count; i++) {
        if (values[i] > max) {
            max = values[i];
        }
    }
    return max;
}