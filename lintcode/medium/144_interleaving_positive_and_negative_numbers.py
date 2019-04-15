'''
Link: https://www.lintcode.com/problem/interleaving-positive-and-negative-numbers/description
'''

# This is my own solution.
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        if len(A) < 2:
            return
        num_neg, num_pos = 0, 0
        for num in A:
            if num < 0:
                num_neg += 1
            else:
                num_pos += 1
        if num_neg >= num_pos:        
            negative, positive = 0, 1
        else:
            negative, positive = 1, 0
        while negative < len(A) and positive < len(A):
            while negative < len(A) and A[negative] < 0:
                negative += 2
            while positive < len(A) and A[positive] > 0:
                positive += 2
            if negative < len(A) and positive < len(A):
                A[negative], A[positive] = A[positive], A[negative]
                positive += 2
                negative += 2
        return
