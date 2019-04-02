'''
Link: https://www.lintcode.com/problem/remove-duplicate-numbers-in-array/description
It is in the section of two-pointer problems.
'''

# My own solution based on the hint in Jiuzhang.com. Uses set.
# It is unnecessarily complicated since it introduces the right pointer, which is not really needed.
# It is also prone to error because we need to consider the value of right pointer very carefully. 
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

    
# This is the solution given in Jiuzhang.com. Similar in idea but much simpler.
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        num_set = set()
        length = 0
        for num in nums:
            if num not in num_set:
                num_set.add(num)
                nums[length] = num
                length += 1
                
        return length
    
# My own solution given Jiuzhang's hint. Two pointers
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if len(nums) < 1:
            return 0
        fast = slow = 0
        nums.sort()
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
                continue
            # Now the two pointers point to different values.
            slow += 1
            nums[slow] = nums[fast]
        return slow + 1

# The solution given in Jiuzhang.com. Better than mine.    
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        n = len(nums)
        if n <= 0:
            return 0
        nums.sort()
        left = 1
        for i in range(1, n):
            # This if block captures the pattern that only those edge elements are unique values.
            if nums[i] != nums[i - 1]:
                nums[left] = nums[i]
                left += 1
        return left
