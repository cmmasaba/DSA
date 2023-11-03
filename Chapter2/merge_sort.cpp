/*MERGE SORT ALGORITHM*/

#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int> &vec, int lower_bound, int midpoint, int upper_bound)
{
    int left = midpoint - lower_bound + 1;
    int right = upper_bound - midpoint;
    vector<int> left_vector(left, 0);
    vector<int> right_vector(right, 0);

    for (int i = 0; i < left; i++)
        left_vector[i] = vec[i];
    for (int i = 0; i < right; i++)
        right_vector[i] = vec[i];

    int i = 0, j = 0, k = 0;
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

void merge_sort(vector<int> &vec, int lower_bound, int upper_bound)
{
    if (lower_bound >= upper_bound)
        return;
    
    int midpoint = (lower_bound + upper_bound) / 2;

    merge_sort(vec, lower_bound, midpoint);
    merge_sort(vec, midpoint + 1, upper_bound);
    merge(vec, lower_bound, midpoint, upper_bound);
}