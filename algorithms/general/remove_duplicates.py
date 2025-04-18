"""
Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return
the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted,
you need to do the following things:

- Change the array nums such that the first k elements of nums contain the
unique elements in the order they were present in nums initially. The
remaining elements of nums are not important as well as the size of nums.
- Return k.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        idx = 1
        unique_count = 1

        while idx < len(nums):
            if nums[idx] != nums[idx - 1]:
                nums[unique_count] = nums[idx]
                unique_count += 1
            idx += 1
        
        return unique_count