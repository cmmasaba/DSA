"""
You are given an integer array nums. You are initially positioned
at the array's first index, and each element in the array represents
your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Initialize the furthest index reachable to 0 at the start of the program, call it maxReach
Iterate over all the elements of the array
At each iteration, check if index i is bigger than maxReach and return False if true
Else update maxReach to be maximum between the maxReach and the current index + the value there
If you reach the end of the loop w/out returning False, return True.
"""

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        """
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False
            
            maxReach = max(maxReach, i + nums[i])
        
        return True