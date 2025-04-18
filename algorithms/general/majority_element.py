"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than
⌊n / 2⌋ times. You may assume that the majority element 
always exists in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        for item in set(nums):                  # Iterate over the distinct set of elements in the list
            if nums.count(item) > len(nums)//2: # Return the element that occurs more than n/2 times
                return item