/*BINARY SEARCH ALGORITHM*/

#include <iostream>
#include <vector>

using namespace std;

/**
 * binary_search - performs recursive binary search on a sorted array
 * @vec: the sorted array of integer elements
 * @value: the value to search for in the array
 * @lower_bound: the lower bound of the array
 * @upper_bound: the upper bound of the array
 * 
 * Return: the index of the element if it is present in the array
 *         otherwise it returns -1
*/
int binary_search(const vector<int> &vec, int value, int lower_bound, int upper_bound)
{
    if (lower_bound > upper_bound)
        return -1;
    
    int midpoint = (lower_bound + upper_bound) / 2;
    
    if (vec[midpoint] < value)
        binary_search(vec, value, midpoint + 1, upper_bound);
    else if (vec[midpoint] > value)
        binary_search(vec, value, lower_bound, midpoint - 1);
    else if (vec[midpoint] == value)
        return midpoint;
}

/**
 * The driver program
 * 
 * Return: 0 on success
*/
int main(void)
{
    try
    {
        cout << "This program performs binary search on an already sorted"
             << " array of integer elements.\n";
        vector<int> values{12, 13, 14, 16, 18, 19, 22, 24, 26};
        int value = 18;

        int index = binary_search(values, value, 0, values.size() - 1);
        if (index == -1)
            cout << "The value " << value << " is not present in the array.\n";
        else
            cout << "The value " << value << " is at index " << index
                 << " in the array.\n";

        return 0;
    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
        return -1;
    }
    catch(...)
    {
        cerr << "Unknown exception occurred!!!\n";
        return -1;
    }
}