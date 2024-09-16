"""Algorithm to find permuations of a given string.
The runtime of the algorithm is O(n!)
"""

def heap_permutation(array: list, length: int):
    if length <= 1:
        yield "".join(array)
    else:
        yield from heap_permutation(array, length - 1)

        for i in range(length - 1):
            if length%2 == 0:
                array[i], array[length - 1] = array[length - 1], array[i]
            else:
                array[0], array[length - 1] = array[length - 1], array[0]

            yield from heap_permutation(array, length - 1)
