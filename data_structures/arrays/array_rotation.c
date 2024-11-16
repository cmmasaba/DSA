/**
 * Hackerank problem:
 * Runtime: O(N) time and O(N) space
 */

#include <stdio.h>
#include <stdlib.h>


/**
 * leftRotate: perform left rotations on an array
 * @num_rotations: the number of rotations to perform
 * @array_size: the size of the array
 * @array: the array to rotate
 * 
 * Returns:
 * A new array which is the original array rotated the number of times
 * specified.
 */
int* leftRotate(int num_rotations, int array_size, int *array) {
    int *new_arr = malloc(array_size * sizeof(int));

    if (num_rotations == array_size) {
        new_arr = array;
        return new_arr;
    }

    // Copy the first num_rotations elements to the back of new_arr
    for (int i = 0; i < num_rotations; i++ ) {
        new_arr[array_size - num_rotations + i] = array[i];
    }

    // Copy the last array_size - num_rotations elements to the front of new_arr
    for (int i = 0; i < array_size - num_rotations; i++) {
        new_arr[i] = array[num_rotations + i];
    }

    return new_arr;
}

/**
 * rightRotate: perform right rotations on an array
 * @num_rotations: the number of rotations to perform
 * @array_size: the size of the array
 * @array: the array to rotate
 * 
 * Returns:
 * A new array which is the original array rotated the number of times
 * specified.
 */
int* rightRotate(int num_rotations, int array_size, int *array) {
    int *new_arr = malloc(array_size * sizeof(int));

    if (num_rotations == array_size) {
        new_arr = array;
        return new_arr;
    }

    // Copy the last num_rotations elements to the front of new_arr
    for (int i = 0; i < num_rotations; i++ ) {
        new_arr[i] = array[array_size - num_rotations + i];
    }

    // Copy the first array_size - num_rotations elements to the back of new_arr
    for (int i = 0; i < array_size - num_rotations; i++) {
        new_arr[num_rotations + i] = array[i];
    }

    return new_arr;
}


int main (void) {
    int array[14] = {98, 67, 35, 1, 74, 79, 7, 26, 54, 63, 24, 17, 32, 81};
    int *left_result = leftRotate(7, 14, array);
    int *right_result = rightRotate(7, 14, array);

    printf("Left rotation: [");
    for (int i = 0; i < 14; i++) {
        printf("%d", left_result[i]);
        if (i != 14 - 1)
            printf(", ");
    }
    printf("]\n");

    printf("Right rotation: [");
    for (int i = 0; i < 14; i++) {
        printf("%d", right_result[i]);
        if (i != 14 - 1)
            printf(", ");
    }
    printf("]\n");

    free(left_result);
    free(right_result);
    return 0;
}