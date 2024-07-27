"""This algorithm determines if a string has all unique characters
Assumptions:
    the character set is ASCII
Time complexity: O(n)
Space complexity: O(1)
"""

def IsUnique(string: str) -> bool:
    if (len(string) > 128):
        # The string can't be unique if it has more than 128 characters
        return False
    char_set = [False for i in range(128)]
    for i in range(len(string)):
        index = ord(string[i])
        if char_set[index]:
            # This character already exists
            return False
        char_set[index] = True
        
    return True

print(f"Is `collins` unique? {IsUnique("collins")}")
print(f"Is `cat` unique? {IsUnique("cat")}")
print(f"Is `drive` unique? {IsUnique("drive")}")
print(f"Is `meet` unique? {IsUnique("meet")}")