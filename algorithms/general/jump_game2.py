"""
You are given a 0-indexed array of integers nums of length n.
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward
jump from index i. In other words, if you are at nums[i], you can
jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test
cases are generated such that you can reach nums[n - 1].

============================================================================================

Use a Greedy algorithm to solve.
At each iteration we want to make a jump that will take us farthes possible.
`jumps` counts the number of jumps made
`currentReach` counts how far the current number of jumps can get us
`maxReachNext` counts farthest we can get if we made a jump from or before the current index.
When currentReach equals n-1, return the number of jumps in that iteration.
"""

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0                                           # Count the number of jumps
        currentReach = 0                                    # Keep track of how far the current number of jumps can get
        maxReachNext = 0                                    # The furthest index we can reach with the current jump

        for i in range(len(nums) - 1):
            maxReachNext = max(maxReachNext, i + nums[i])

            if i == currentReach:                           # We have reached the limit of the current number of jumps
                jumps += 1
                currentReach = maxReachNext                 # Update the new furthest reach
            
            if currentReach == len(nums) - 1:
                break
        
        return jumps