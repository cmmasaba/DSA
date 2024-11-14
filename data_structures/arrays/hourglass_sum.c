/**
 * HackerRank problem: https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true
*/

#include <stdio.h>

int hourglassSum(int arr_rows, int arr_columns, int** arr) {
    int current_sum = 0, max_result = 0;
    
    for ( int i = 0; i < 4; ++i ) {
        for ( int j = 0; j < 4; ++j ){
            current_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + 
                           arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]);
            if ( i == 0 && j == 0 )
                max_result = current_sum;
            else
                if ( current_sum > max_result )
                    max_result = current_sum;
        }
    }
    
    return max_result;
}

int main (void) {
    // Example input array
    int array[6][6] = {
        {-9, -9, -9, 1, 1, 1},
        {0, -9, 0, 4, 3, 2},
        {-9, -9, -9, 1, 2, 3},
        {0, 0, 8, 6, 6, 0},
        {0, 0, 0, -2, 0, 0},
        {0, 0, 1, 2, 4, 0}
    };

    int result = hourglassSum(6, 6, array);
    printf("The largest hourglass sum is %d", result);

    return 0;
}