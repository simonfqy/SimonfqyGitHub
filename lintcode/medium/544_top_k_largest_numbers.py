'''
https://www.lintcode.com/problem/544
'''

# My own solution. Uses heap. Time complexity should be O(nlogn), where n is the length of nums.
import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        negative_nums = []
        for num in nums:
            heapq.heappush(negative_nums, -num)
        results = []
        while len(results) < k:
            results.append(-heapq.heappop(negative_nums))
        return results
    
            
# My own, simple solution using Python sort function.
import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        nums.sort()
        top_k = nums[len(nums) - k:]
        top_k.reverse()
        return top_k
            
