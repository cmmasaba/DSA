/**
 * INSERTION SORT ALGORITHM
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
void print_vector(vector<int> &vec){
    for(int i : vec){
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
void read_vector(vector<int> &vec){
    int num = 0;

    while(cin >> num){
        vec.push_back(num);
    }
    if(cin.eof()){
        cin.clear();
    }
    return;
}

/**
 * insertion_sort_ascending - sorts a vector in ascending order using
 *                            insertion sort algorithm.
 * @vec: the vector to be sorted.
 * 
 * return: void.
*/
void insertion_sort_ascending(vector<int> &vec){
    int key = 0, j = 0;

    for(int i = 1; i < vec.size(); i++){
        key = vec[i];
        j = i - 1;
        while(j >= 0 and vec[j] > key){
            vec[j+1] = vec[j];
            j--;
        }
        vec[j+1] = key;
    }
    
    return;
}

/**
 * main - driver program
 * Prints a descriptive message to stdout
 * Prints the unsorted and sorted vectors
 * 
 * return: 0 on success
*/
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
        
        insertion_sort_ascending(values);
        cout << "The sorted array in ascending order: ";
        print_vector(values);
        cout << endl;

        return 0;
    } catch ( exception &e ) {
        cout << "Error: " << e.what() << endl;
        return -1;
    } catch (...) {
        cout << "Unkown error encountered!!!";
        return -1;
    }
}