/**
 * A program implementing the insertion sort algorithm
 * in descending order
*/

#include <iostream>
#include <vector>

using namespace std;

void print_vector( const vector<int> &vec )
{
    for(int i : vec)
    {
        cout << i << " ";
    }

    cout << endl;
    return;
}

void read_vector( vector<int> &vec )
{
    int num = 0;

    while(cin >> num)
        vec.push_back(num);
    
    if(cin.eof())
        cin.clear();

    return;
}

void insertion_sort_descending( vector<int> &vec )
{
    int key = 0, j = 0;

    for(int i = 1; i < vec.size(); i++)
    {
        key = vec[i];
        j = i - 1;
        while(j >= 0 and vec[j] < key)
        {
            vec[j+1] = vec[j];
            j--;
        }
        vec[j+1] = key;
    }
    
    return;
}

int main( void ){
    try
    {
        vector<int> values;

        cout << "This program implements insertion sort in descending order.\n"
             << "Input is an array of integers, output is the sorted array." << endl;
        cout << "Enter the elements of the array at the next prompt:\n";
        
        read_vector(values);;
        cout << "The unsorted vector: ";
        print_vector(values);
        cout << endl;
        
        insertion_sort_descending(values);
        cout << "The sorted array in descending order: ";
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