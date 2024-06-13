#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <limits.h>

// Comparator function for qsort
int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int minMovesToSeat(int* seats, int seatsSize, int* students, int studentsSize) {
    int moves = 0; // Number of moves made

    qsort(seats, seatsSize, sizeof(int), cmp);
    qsort(students, studentsSize, sizeof(int), cmp);

    for (int i = 0; i < seatsSize; i++) {
        moves += abs(seats[i] - students[i]);
    }

    return moves;
}