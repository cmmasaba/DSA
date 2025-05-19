
class Solution:
    def search_array(self, nums, val):
        for i in range(len(nums)//2 + 1):
            if nums[i] == val:
                return i
            elif nums[len(nums) - 1 - i] == val:
                return len(nums) - 1 - i
        
        return -1
    

soln = Solution()

input1 = [1, 3, 5]

""" input2 = [4, 5, 6, 7, 0, 1, 2]

input3 = [1]

input4 = [0, 1, 2, 3, 4, 5, 6, 7] """

print(f"In {input1}, integer 0 is at index {soln.search_array(input1, 3)}")
""" print(f"In {input2}, integer 3 is at index {soln.search_array(input2, 3)}")
print(f"In {input3}, integer 0 is at index {soln.search_array(input3, 0)}")
print(f"In {input4}, integer 2 is at index {soln.search_array(input4, 2)}") """