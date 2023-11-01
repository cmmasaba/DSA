/**
 * SELECTION SORT ALGORITHM
*/

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
 * selection_sort - sorts a vector of elements using selection sort.
 * @vec: the vector with elements.
 * 
 * return: void.
*/
void selection_sort(vector<int> vec)
{
    int min = 0, temp = 0;

    for (int i = 0; i < vec.size() - 2; i++)
    {
        min = i;
        for (int j = i++; j < vec.size() - 1; j++)
            if (vec[j] < vec[min])
                min = j;

        temp = vec[i];
        vec[i] = vec[min];
        vec[min] = temp;
    }
}

/**
 * main - driver program
 * Prints a descriptive message to stdout
 * Prints the unsorted and sorted vectors
 * 
 * return: 0 on success
*/
int main( void ){
    try
    {
        vector<int> values;

        cout << "This program implements selection sort in ascending order.\n"
             << "Input is an array of integers, output is the sorted array." << endl;
        cout << "Enter the elements of the array at the next prompt:\n";
        
        read_vector(values);;
        cout << "The unsorted vector: ";
        print_vector(values);
        cout << endl;
        
        selection_sort(values);
        cout << "The sorted array in ascending order: ";
        print_vector(values);
        cout << endl;

        return 0;
    } 
    catch ( const exception &e )
    {
        cerr << "Error: " << e.what() << endl;
        return -1;
    } 
    catch (...)
    {
        cerr << "Unkown error encountered!!!";
        return -1;
    }
}
