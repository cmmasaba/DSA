"""Algorithm to find permuations of a given string.
The runtime of the algorithm is O(n^2 * n!)
"""

def find_permutation(string: str):
    permutation(string, prefix="")

def permutation(string: str, prefix: str):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(0, len(string)):
            rem = string[0:i] + string[i+1:]
            permutation(rem, prefix + string[i])

find_permutation('cmk')