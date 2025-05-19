"""
Given an array of integers citations where citations[i] is the number of
citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined
as the maximum value of h such that the given researcher has published at least
h papers that have each been cited at least h time.

Sorting the array in ascending order enables us to quickly determine how many
papers have at least a certain number of citations. For example, given an index
i, all papers from index i to the end of the array have at least 
citations[i] citations.

Consider iterating through the sorted citation array. For each paper at index i
(from the beginning to the end), the number of papers with at least citations[i]
citations is n - i (where n is the total number of papers). We are looking for
the largest index i such that citations[i] >= n - i. If this condition holds, it
means there are n - i papers with at least citations[i] citations, and since
citations[i] is greater than or equal to the count (n - i), we have found the h-index
"""

def h_index_brute_force(citations):
    citations.sort()

    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    
    return 0

# Example usage:
citations1 = [3, 0, 6, 1, 5]
print(f"The h-index for {citations1} is: {h_index_brute_force(citations1)}")

citations2 = [1, 3, 1]
print(f"The h-index for {citations2} is: {h_index_brute_force(citations2)}")

citations3 = [0]
print(f"The h-index for {citations3} is: {h_index_brute_force(citations3)}")