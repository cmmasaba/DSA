"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 
121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    x_str = str(x)

    for i in range(len(x_str)//2):
        if x_str[i] != x_str[len(x_str) - 1 - i]:
            return False
    return True

print(f"Is 121 palindrome: {is_palindrome(121)}")
print(f"Is -121 palindrome: {is_palindrome(-121)}")
print(f"Is 10 palindrome: {is_palindrome(10)}")
