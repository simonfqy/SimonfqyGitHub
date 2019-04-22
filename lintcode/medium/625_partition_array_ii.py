'''
Link: https://www.lintcode.com/problem/partition-array-ii/description
'''

# I did not completely come up with this solution correctly. I had to refer to the sort colors problem solution.
class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums, low, high):
        # write your code here
        if nums is None or len(nums) <= 1:
            return
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            # The whole if-else block only traverses 1 step per iteration of the while loop.
            if nums[mid] < low:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                # Naturally, move the middle pointer forward. 
                mid += 1
            elif nums[mid] > high:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
            else:
                mid += 1
        return
