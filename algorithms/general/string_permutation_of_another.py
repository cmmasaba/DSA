from string_permutation import heap_permutation


# Very naive approach
def check_two_strings(string1: str, string2) -> bool:
    """Check if string1 is a permutation of string2.

    Args:
        string1: the string to check
        string2: the original string
    Returns:
        True if string1 is permutation of string2, otherwise False.
    """
    if len(string1) > len(string2) or not string1:
        # string1 cannot be a permutation of string2 if it is longer than string2, or it's an empty string
        return False
    
    # Get string2 permutations and check if string1 is among the permuted strings.
    str2_permutations = {string for string in heap_permutation(list(string2), len(list(string2)))}
    if string1 in str2_permutations:
        return True
    else:
        return False

# An efficient approach

def permuted(string1: str, string2: str):
    """Check if one string is a permutation of the other string.

    Runtime of O(N).
    Assumptions: ASCII character set, case sensitive, whitespace is significant.
    Args:
        string1: the string to check
        string2: the original string
    Returns:
        True if string1 is permutation of string2, otherwise False.
    """

    if len(string1) != len(string2):
        return False
    
    letters = [0 for i in range(128)]

    for char in string1:
        letters[ord(char)] += 1
    
    for char in string2:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False
    
    return True