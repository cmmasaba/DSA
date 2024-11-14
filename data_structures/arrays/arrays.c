/**
 * An array is a set of ordered data items.
 * The first element of an array is indexed 0, and the last element is indexed
 * the number of elements in the arrat minus one.
 * Integers and integer ecpressions can be used to index an array.
 * 
 * Declaring array is done by stating the type of elements to store in the array,
 * and the maximum number of elements that can be stored in the array.
 * C does not do type-checking of array subscripts. Using an index outside the
 * bounds can cause overwriting a memory location.
 * You can declare an array without specifying the number of elements. However 
 * you must provide the initialization elements.
 */

#include <stdio.h>

int main (void)
{
    /*
    // Declare an array of type integer with size 10 an initialize it to 0
    int values[10] = {0};
    int index = 0;
    
    values[0] = 197;
    values[2] = -100;
    values[5] = 350;
    values[3] = values[0] + values[5];
    values[9] = values[5] / 10;
    --values[2];

    for ( index = 0; index < 10; ++index )
        printf("values[%i] = %i\n", index, values[index]);
    

    // Array of counters
    int i, response;
    // Declare an array an initialize it to 0
    int ratingCounter[11] = {0};
    
    printf("Enter your responses\n");

    for ( i = 1; i <= 20; ++i ) {
        scanf("%i", &response);

        if ( response < 0 || response > 10 )
            printf("Bad response: %i\n", response);
        else
            ++ratingCounter[response];
    }

    printf("\n\nRating    Number of responses\n");
    printf("------    -------------------\n");

    for (i = 1; i <= 10; ++i)
        printf("%4i%14i\n", i, ratingCounter[i]);
    

    // Character Arrays
    char word [] = {'A', 'r', 'r', 'a', 'y'};

    for ( int i = 0; i < 5; i++ ) 
        printf("%c", word[i]);
    printf("\n");
    */
    const char baseDigits[] = {
        '0', '1', '2', '3', '4', '5', '6',
        '7', '8', '9', 'A', 'B', 'C', 'D',
        'E', 'F'
    };
    int convertedNumber[64];
    long int numberToConvert;
    int nextDigit, base, index = 0;

    // Get the number
    printf("Enter the number to be converted: ");
    scanf("%ld", &numberToConvert);
    printf("Base to convert the number to: ");
    scanf("%i", &base);

    // Convert the number to the base
    do {
        convertedNumber[index] = numberToConvert % base;
        ++index;
        numberToConvert = numberToConvert / base;
    } while ( numberToConvert != 0 );
    
    // Display results
    printf("Converted number: ");
    for ( --index; index >= 0; --index ) {
        nextDigit = convertedNumber[index];
        printf("%c", baseDigits[nextDigit]);
    }
    printf("\n");

    return 0;
}