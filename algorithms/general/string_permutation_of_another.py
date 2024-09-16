from string_permutation import heap_permutation

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
    

print(f"Is ins a permutation of Collins? {check_two_strings("ins", "Collins")}")
