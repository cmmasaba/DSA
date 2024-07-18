"""Insertion sort program implemented using Python"""

def insertion_sort(array: list):
    """Sorts the elements of an array.
    
    @param array: a list of elements
    """
    key: int = 0

    for i in range(1, len(array)):
        key = array[i]
        j:int = i - 1

        while j>= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def print_array(array: list):
    """Prints the elements of an array.

    @param array: a list of elements
    """
    for item in array:
        print(item, end=" ")
    print()

def main():
    print("This program sorts an array in ascending order using"
          " Insertion Sort algorithm.\n")
    array = input("Enter the elements of the array: ")
    print()
    array = list(map(int, array.split()))
    print(f"The unsorted array is:")
    print_array(array)
    insertion_sort(array)
    print(f"The sorted array is:")
    print_array(array)

if __name__ == "__main__":
    main()