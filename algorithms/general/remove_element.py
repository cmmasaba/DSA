"""
Given an integer array nums and an integer val, remove all occurrences of val in nums
in-place. The order of the elements may be changed. Then return the number of elements
in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which
are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            if nums[start] == val and nums[end] != val:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            elif nums[start] == val and nums[end] == val:
                end -= 1
            else:
                start += 1
        return len(nums) - nums.count(val)
