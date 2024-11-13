"""
Write a method that replaces all spaces in a string with %20. 
You may assume that the string has sufficient space at the end 
to hold the additional characters, and that you are given the 
"true length" of the string.

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
    spaces_count = 0
    # Count the number of spaces
    for i in range(length - 1, -1, -1):
        if string[i] == ' ':
            spaces_count += 1

    index = length + spaces_count * 2
    # Replace spaces with %20
    for i in range(length - 1, -1, -1):
        if str_list[i] == " ":
            str_list[index - 1] = '0'
            str_list[index - 2] = '2'
            str_list[index - 3] = '%'
            index -= 3
        else:
            str_list[index - 1] = str_list[i]
            index -= 1

    return "".join(str_list)