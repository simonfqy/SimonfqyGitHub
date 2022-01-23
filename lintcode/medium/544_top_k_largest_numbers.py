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
    
    # This is the same implementation as the quickSelect algorithm, but here we don't let it return any value. It is just
    # used for rearranging the nums list, such that nums[start : ind + 1] elements are all no smaller than nums[ind + 1:].
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
        # Here, left is greater than right.
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
        
            
# Another solution from a student on jiuzhang.com. It uses another implementation to move elements as part of the quickSelect
# or quickSort algorithm. 
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        if k < 1 or not nums:
            return []
        start, end = 0, len(nums) - 1
        index = self.partition(nums, start, end)
        target_ind = k - 1
        while index != target_ind:
            if index > target_ind:
                # Have to contain +1 and -1, otherwise we'll enter infinite loop.
                end = index - 1
            else:
                start = index + 1
            index = self.partition(nums, start, end)
        top_k = nums[: target_ind + 1]
        top_k.sort(reverse=True)
        return top_k
    
    # This function returns index, which is the dividing point such that nums[start : index + 1] are no smaller than
    # nums[index]. It is a component of the quickSelect or quickSort algorithm.
    def partition(self, nums, start, end):
        if start == end:
            return start
        index = start
        # This for loop makes sure that elements in nums[start : index] are all greater than or equal to nums[end]
        for i in range(start, end):
            if nums[i] < nums[end]:
                continue
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
        # This moves the nums[end] to the position of nums[index], so that nums[start : index + 1] contain all the
        # elements no smaller than the original nums[end].
        nums[index], nums[end] = nums[end], nums[index]
        return index
