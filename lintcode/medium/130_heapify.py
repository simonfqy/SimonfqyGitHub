'''
Link: https://www.lintcode.com/problem/heapify/description
'''

# This solution is based on the teachings from jiuzhang.com. Siftup, time complexity is O(nlogn), where
# n is the number of nodes.
# When implementing it myself for the first time, I made a mistake: I let i traverse from largest to 0,
# which caused problem. In fact, the siftup operation should traverse each node from root to leaf, so that 
# no misalignment will be left out, they are all taken care of in the traversal from root to leaf.
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A)):
            self.siftup(A, i)
            
    def siftup(self, A, i):
        while i > 0:
            father_ind = i // 2
            if i % 2 == 0:
                father_ind -= 1
            if A[father_ind] <= A[i]:
                break
            A[father_ind], A[i] = A[i], A[father_ind]
            i = father_ind

            
# Similarly, sifting down, but doing so from leaf to root. O(n) time complexity.            
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A)-1, -1, -1):
            self.siftdown(A, i)
            
    def siftdown(self, A, i):
        while i <= (len(A) - 2) // 2:
            son_ind = i * 2 + 1
            if len(A) - 1 >= i * 2 + 2 and A[son_ind] > A[i * 2 + 2]:
                son_ind = i * 2 + 2
            if A[son_ind] >= A[i]:
                break
            A[son_ind], A[i] = A[i], A[son_ind]
            i = son_ind
