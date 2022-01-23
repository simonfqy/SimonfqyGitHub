'''
Link: https://www.lintcode.com/problem/545/
'''

# My own solution. Uses binary search to find the position to add the new element. The time complexity of
# each add() is O(n) where n is the size of the self.top_k list. 
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.k = k
        self.top_k = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        if len(self.top_k) > 0:
            if len(self.top_k) == self.k and self.top_k[-1] >= num:
                return
            first_smaller_num_ind = self.get_first_smaller_num_ind(self.top_k, num, 0, len(self.top_k) - 1)
            self.top_k = self.top_k[:first_smaller_num_ind] + [num] + self.top_k[first_smaller_num_ind:]
            if len(self.top_k) > self.k:
                self.top_k.pop()
        elif self.k > 0:
            self.top_k.append(num)
    
    def get_first_smaller_num_ind(self, top_k, num, start, end):
        left, right = start, end
        while left + 1 < right:
            mid = (left + right) // 2
            if top_k[mid] < num:
                right = mid
            else:
                left = mid
        if top_k[left] <= num:
            return left
        if top_k[right] <= num:
            return right
        return len(top_k) 

    """
    @return: Top k element
    """
    def topk(self):
        return self.top_k

    
# My own solution. Using a heap to keep the order, and keep a local list of top k elements. The optimization 
# introduced by maintaining self.existing_top_k_bar and self.update_required variables don't seem to have much effect.
# The add() function has O(logn) time complexity, while topk() function has O(klogn) time complexity.
import heapq
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.k = k
        self.heap = []
        self.existing_top_k_bar = float('-inf')
        self.update_required = True
        self.top_k = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        heap_size = len(self.heap)
        heapq.heappush(self.heap, -num)
        if heap_size < self.k or num > self.existing_top_k_bar:
            self.update_required = True

    """
    @return: Top k element
    """
    def topk(self):
        if not self.update_required:
            return self.top_k
        self.top_k = []
        while len(self.top_k) < self.k and len(self.heap) > 0:
            self.top_k.append(-heapq.heappop(self.heap))
        if len(self.top_k) == self.k:
            self.existing_top_k_bar = self.top_k[-1] 
        for element in self.top_k:
            heapq.heappush(self.heap, -element)
        self.update_required = False
        return self.top_k
    
    
# This solution is based on the answers from jiuzhang.com. We're only keeping a heap with size k in this way,
# so the time complexity for add() is O(logk), that of topk() function is O(klogk).
import heapq
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.k = k
        self.top_k = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        if len(self.top_k) < self.k or num > self.top_k[0]:
            heapq.heappush(self.top_k, num)
        if len(self.top_k) > self.k:
            heapq.heappop(self.top_k)

    """
    @return: Top k element
    """
    def topk(self):
        results = []
        while len(self.top_k) > 0:
            results.append(heapq.heappop(self.top_k))
        for element in results:
            heapq.heappush(self.top_k, element)
        return results[::-1]   

    
# This is a solution from a student of jiuzhang.com. I like this solution for it being succinct. But its performance is not as
# good as the one above.
from heapq import heappush, heappushpop
class Solution:
    
    def __init__(self, k):
        
        self.h = []
        self.k = k 
        
    def add(self, num):        
        h, k = self.h, self.k
        
        if len(h) < k:
            heappush(h, num)
        elif num > h[0]:
            heappushpop(h, num)
        
    def topk(self):        
        self.h.sort()
        return self.h[::-1]
