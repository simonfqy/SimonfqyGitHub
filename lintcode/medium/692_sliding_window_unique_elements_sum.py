'''
Link: https://www.lintcode.com/problem/692
'''

# My own solution, using two pointers. Has O(n) time complexity.
from collections import defaultdict
class Solution:
    """
    @param nums: the given array
    @param k: the window size
    @return: the sum of the count of unique elements in each window
    """
    def slidingWindowUniqueElementsSum(self, nums, k):
        n = len(nums)
        num_to_occurrence = defaultdict(int)
        left = 0
        unique_element_count = 0
        total_count = 0
        for right in range(n):
            new_num = nums[right]
            num_to_occurrence[new_num] += 1
            if num_to_occurrence[new_num] == 1:
                unique_element_count += 1
            elif num_to_occurrence[new_num] == 2:
                unique_element_count -= 1
            if right >= k:
                removed_num = nums[left]
                left += 1
                num_to_occurrence[removed_num] -= 1
                if num_to_occurrence[removed_num] == 0:
                    unique_element_count -= 1
                elif num_to_occurrence[removed_num] == 1:
                    unique_element_count += 1
            if right >= k - 1 or right == n - 1:
                total_count += unique_element_count        
        return total_count
