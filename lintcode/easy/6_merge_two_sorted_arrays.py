'''
Link: https://www.lintcode.com/problem/6/
'''

# My own solution. It is largely copying from
# https://github.com/simonfqy/SimonfqyGitHub/blob/37fb38b02036f0a14fd39217548f5512596bcf9f/lintcode/medium/104_merge_K_sorted_lists.py#L188
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        A_ind, B_ind = 0, 0
        A_len, B_len = len(A), len(B)
        result = []
        while A_ind <= A_len - 1 and B_ind <= B_len - 1:
            if A[A_ind] < B[B_ind]:
                result.append(A[A_ind])
                A_ind += 1
            else:
                result.append(B[B_ind])
                B_ind += 1
        if A_ind <= A_len - 1:
            result += A[A_ind:]
        if B_ind <= B_len - 1:
            result += B[B_ind:]
        return result
      
      
