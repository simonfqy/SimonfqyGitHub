'''
Link: https://www.lintcode.com/problem/remove-duplicate-numbers-in-array/description
'''

# My own solution based on the hint in Jiuzhang.com. Uses set.
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        num_set = set()
        right = 0
        for ind in range(len(nums)):
            right = max(right, ind)
            while nums[ind] in num_set and right < len(nums) - 1:
                right += 1
                nums[ind], nums[right] = nums[right], nums[ind]
            num_set.add(nums[ind])
            if right >= len(nums):
                break
                
        return len(num_set)
