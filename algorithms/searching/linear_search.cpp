/**
 * A linear search program
*/

#include <iostream>
#include <vector>

using namespace std;

/**
 * linear_search -  searches for a value in an array
 * @vec: the array to search i
 * @value: the value to search for in the array
 * 
 * return: the index of the value in the array on success
 *         -1 if the element is not in the array
*/
int linear_search(const vector<int> &vec, int value)
{
    for(int i = 0; i < vec.size(); i++)
        if (vec[i] == value)
            return i;
    return -1;
}

/**
 * The driver program
 * 
 * return: 0 on success
*/
int main(void)
{
    try
    {
        vector<int> values = {12, 11, 23, 43, 56, 98, 34};
        int num = 23;

        int index = linear_search(values, num);
        if (index > 0)
        {
            cout << num << " is at index " << index << " in the array.\n";
        }
        else
        {
            cout << num << " is not in the array.\n";
        }
        return 0;
    }
    catch( const exception& e )
    {
        cerr << e.what() << '\n';
        return -1;
    }
    catch(...)
    {
        cerr << "Unknown error occurred!!!.\n";
        return -1;
    }
}