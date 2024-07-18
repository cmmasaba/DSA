/*MERGE SORT ALGORITHM*/

#include <iostream>
#include <vector>

using namespace std;

/**
 * print_vector -  prints the elements of a vector to stdout.
 * @vec: a vector to be printed.
 * 
 * return: void.
*/
void print_vector( const vector<int> &vec )
{
    for(int i : vec)
    {
        cout << i << " ";
    }

    cout << endl;
    return;
}

/**
 * read_vector - read integers from stdin and store them in a vector.
 * @vec: the vector to store elements inside.
 * 
 * return: void.
*/
void read_vector( vector<int> &vec )
{
    int num = 0;

    while(cin >> num)
    {
        vec.push_back(num);
    }

    if(cin.eof())
    {
        cin.clear();
    }
    return;
}

/**
 * merge - does the merge operation on two subarrays
 * @vec: the main array of elements
 * @lower_bound: the index of the first element in the subarray
 * @midpoint: the index of the mid element in the subarray
 * @upper_bound: the index of the last element in the subarray
*/
void merge(vector<int> &vec, int lower_bound, int midpoint, int upper_bound)
{
    int left = (midpoint - lower_bound) + 1;
    int right = upper_bound - midpoint;
    vector<int> left_vector(left, 0);
    vector<int> right_vector(right, 0);

    for (int i = 0; i < left; i++)
        left_vector[i] = vec[lower_bound + i];
    for (int i = 0; i < right; i++)
        right_vector[i] = vec[midpoint + i + 1];

    int i = 0, j = 0, k = lower_bound;
    while ( i < left && j < right )
    {
        if (left_vector[i] <= right_vector[j])
        {
            vec[k] = left_vector[i];
            i++;
        }
        else
        {
            vec[k] = right_vector[j];
            j++;
        }
        k++;
    }

    while ( i < left )
    {
        vec[k] = left_vector[i];
        i++;
        k++;
    }

    while ( j < right )
    {
        vec[k] = right_vector[j];
        j++;
        k++;
    }
}

/**
 * merge_sort - recursively sort an array of elements using divide and conquer
 * @vec: the array of elements
 * @lower_bound: the index of the fisrt element
 * @upper_bound: the index of the last element
 * 
 * Return: void
*/
void merge_sort(vector<int> &vec, int lower_bound, int upper_bound)
{
    if (lower_bound >= upper_bound)
        return;
    
    int midpoint = (lower_bound + upper_bound) / 2;

    merge_sort(vec, lower_bound, midpoint);
    merge_sort(vec, midpoint + 1, upper_bound);
    merge(vec, lower_bound, midpoint, upper_bound);
}

/**
 * The driver program
 * 
 * Return: 0 on success
*/
int main( void )
{
    try
    {
        cout << "This program performs merge sort on an array of elements." 
             << "Enter the array elemts at the prompt:" << endl;

        vector<int> values;
        read_vector(values);
        cout << "The unsorted array: ";
        print_vector(values);
        cout << endl;

        merge_sort(values, 0, values.size() - 1);
        cout << "The sorted array: ";
        print_vector(values);
        cout << endl;
    }
    catch(const std::exception& e)
    {
        cerr << e.what() << endl;
    }
    catch(...)
    {
        cerr << "Unknown exception occurred!!!" << endl;
    }
}