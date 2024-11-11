"""
Write a method that replaces all spaces in a string with %20. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true length" of the string.
"""

def urlify(string: str, length: int):
    """Replaces all spaces in the string with %20.

    Args:
        string: the string.
        length: the true length of the string.
    Returns:
        A new string with the spaces replaced.
    """
    str_list = list(string)
    spaces_count = str_list.count(" ")

    for i in range(spaces_count):
        idx = str_list.index(" ")
        str_list[idx] = "%20"

    return "".join(str_list)
