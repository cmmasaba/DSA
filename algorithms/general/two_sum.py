"""
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List

def two_sum(nums: List[int], target: int):
    nums_map = {}
    for i, num in enumerate(nums):
        remainder = target - num
        if remainder in nums_map:           # Check if the remainder is already in the nums_map and return the two complementary indices
            return [nums_map[remainder], i]
        nums_map[num] = i                   # Store the key-value of num and its index

    return []                               # No numbers found


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    sum_indices = two_sum(nums, 9)
    print(f"List: {nums}, Target: 9, Indices: {sum_indices}")

    nums = [3, 2, 4]
    sum_indices = two_sum(nums, 6)
    print(f"List: {nums}, Target: 6, Indices: {sum_indices}")

    nums = [3, 3]
    sum_indices = two_sum(nums, 6)
    print(f"List: {nums}, Target: 6, Indices: {sum_indices}")
