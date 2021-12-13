'''
Link: https://www.lintcode.com/problem/362
'''

# My own solution. Uses a queue and has O(n) time complexity and O(k) space complexity. The solution is similar to 
# https://github.com/simonfqy/SimonfqyGitHub/blob/c6a67e9fe0e746390396ee2db18f7bb809cefe32/lintcode/medium/621_maximum_subarray_v.py#L41.
from collections import deque
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        results = []
        # Each element: (index, value)
        queue = deque()
        for right in range(n):
            if right >= k:
                # Pop the earlier element(s). Note that the only possible earlier element is nums[right - k], so we can reduce this 2-level indentation
                # to 1-level, and make it an if statement rather than while loop. 
                # Why elements before nums[right - k] will not appear in the front of the queue? Because if queue[0][0] is right - k - 1, it would have
                # been popped when right == right - 1. How about queue[0][0] being right - k and queue[1][0] being right - k - 1? It is also impossible, 
                # because it would have been popped when nums[right - k], which is larger than nums[right - k - 1], was added to the queue.
                while queue and queue[0][0] <= right - k:
                    queue.popleft()
            # Add the right element. Pop the elements which are earlier and smaller, since they won't appear in the result anyways.
            # This popping operation will help maintain the order, making sure that the largest element is always at the left end of the queue.
            while queue and queue[-1][1] <= nums[right]:
                queue.pop()
            queue.append((right, nums[right]))
            if right >= k - 1:
                results.append(queue[0][1])
        return results
    
    # Slight variant with the de-que operation changed from while loop to if statement.
    def maxSlidingWindow2(self, nums, k):
        n = len(nums)
        results = []
        # Each element: (index, value)
        queue = deque()
        for right in range(n):
            # Explained above. The only possible earlier element is nums[right - k] at this point.
            if right >= k and queue and queue[0][0] <= right - k:
                queue.popleft()            
            while queue and queue[-1][1] <= nums[right]:
                queue.pop()
            queue.append((right, nums[right]))
            if right >= k - 1:
                results.append(queue[0][1])
        return results
      
      
# My own solution. Uses Python heapq, has time complexity O(nlogn) and space complexity O(n).
# Time to execute is much longer than the deque solution.
import heapq
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        results = []
        # Each element: (-value, index)
        heap = []
        for i, num in enumerate(nums):
            if i >= k:
                # Pop the left element(s).
                while heap and heap[0][1] <= i - k:
                    heapq.heappop(heap)
            # Add to the heap.
            heapq.heappush(heap, (-num, i))
            if i >= k - 1:
                results.append(-heap[0][0])

        return results
    
    
