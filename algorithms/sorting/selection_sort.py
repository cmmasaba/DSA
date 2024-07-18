""""SELECTION SORT"""


def print_array(array: list):
    """Prints the elements of a list.
    
    @param array: a list with elements."""
    for item in array:
        print(item, end=" ")
    print()


def selection_sort(array: list):
    """Selection sort algorithm in ascending order.
    
    @param array: a list with the elemtns to be sorted
    """
    for i in range(0, len(array) - 1):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]


def main():
    """The driver program."""
    print("\tA program that does selection sort in ascending order.\n"
          "\tEnter the values of the array at the prompt, separated by space.")
    values = list(map(int, input("Enter the elements of the array: ").split()))

    print("The unsorted array is: ")
    print_array(values)
    selection_sort(values)
    print("The sorted array is: ")
    print_array(values)


if __name__ == "__main__":
    main()