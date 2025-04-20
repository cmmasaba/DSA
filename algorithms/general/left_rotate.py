"""
Given an integer array nums, rotate the array to the left by k steps, where k is non-negative
"""
class Solution(object):
    def reverse(self, nums, start, end):
        """
        :type nums: List[int]
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # Handle cases when k > n
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

if __name__ == "__main__":
    soln = Solution()
    s = [1, 2, 3, 4, 5, 6, 7]
    soln.rotate(s, 3)
    print(s)
