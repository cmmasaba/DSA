/**
 * A program implementing the insertion sort algorithm
 * in a recursive manner
*/

#include <iostream>
#include <vector>

using namespace std;

void print_vector(vector<int> &vec)
{
    for(int i : vec){
        cout << i << " ";
    }
    cout << endl;
    return;
}

void read_vector(vector<int> &vec)
{
    int num = 0;

    while(cin >> num){
        vec.push_back(num);
    }
    if(cin.eof()){
        cin.clear();
    }
    return;
}

void insertion_sort(vector<int> &vec, int size)
{
    if ( size <= 1 )
        return;
    
    insertion_sort(vec, size - 1);
    int key = vec[size - 1];
    int index = size - 2;
    while (index >= 0 && vec[index] > key)
    {
        vec[index + 1] = vec[index];
        index--;
    }
    vec[index + 1] = key;
    return;
}

int main(void){
    try{
        vector<int> values;

        cout << "This program implements insertion sort in ascending order.\n"
             << "Input is an array of integers, output is the sorted array." << endl;
        cout << "Enter the elements of the array at the next prompt:\n";
        
        read_vector(values);;
        cout << "The unsorted vector: ";
        print_vector(values);
        cout << endl;
        
        insertion_sort(values, values.size());
        cout << "The sorted array in ascending order: ";
        print_vector(values);
        cout << endl;
    } catch ( exception &e ) {
        cout << "Error: " << e.what() << endl;
    } catch (...) {
        cout << "Unkown error encountered!!!";
    }
    return 0;
}