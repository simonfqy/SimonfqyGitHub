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
            
        
# Slightly converted from the solution provided by students of jiuzhang.com. Uses quickSelect algorithm to make nums[:k]
# contain the k largest elements of nums array. Then sort that sublist reversely (in descending order) and return it.
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        self.quick_select(nums, 0, len(nums) - 1, k - 1)
        top_k = nums[:k]
        top_k.sort(reverse=True)
        return top_k

    def quick_select(self, nums, start, end, ind):
        if start == end:
            return
        left, right = start, end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        if left <= ind:
            self.quick_select(nums, left, end, ind)
            return
        if right >= ind:
            self.quick_select(nums, start, right, ind)
            
            
# A solution from jiuzhang.com. Uses custom-implemented quick sort with slight optimization.
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        self.quick_sort(nums, 0, len(nums) - 1, k - 1)
        return nums[:k]
        
    def quick_sort(self, nums, start, end, ind):
        # Slight optimization: no need to order the elements after ind, we only care about nums[:ind + 1].
        if start >= ind:
            return
        if start >= end:
            return
        left, right = start, end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        self.quick_sort(nums, start, right, ind)
        self.quick_sort(nums, left, end, ind)
            
