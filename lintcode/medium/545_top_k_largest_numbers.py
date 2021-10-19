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
