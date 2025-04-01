"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List

def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
            return ""

    prefix = strs[0]

    for item in strs[1:]:
        length = len(prefix) if len(prefix) < len(item) else len(item)
        for i in range(length):
            if prefix[i] != item[i]:
                prefix = prefix[:i]
                break
        prefix = prefix[:length]
        if not prefix:
            return ""
    return prefix

if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(f"Longest common prefix for {strs} is {longest_common_prefix(strs)}")

    strs = ["dog", "cat", "racecar"]
    print(f"Longest common prefix for {strs} is {longest_common_prefix(strs)}")
