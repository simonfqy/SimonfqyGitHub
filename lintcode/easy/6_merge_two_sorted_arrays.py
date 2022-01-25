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
      
      
# Based on a solution from a student on jiuzhang.com. It is optimized for the case where one array (A) is very large while the other (B)
# is very small. Here we have O(mlogn) time complexity, where m < n, m is the size of B and n is the size of A. 
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # Enforce that A is the larger array.
        if len(A) < len(B):
            A, B = B, A
        A_ind = 0
        merged_array = []
        for i in range(len(B)):
            b_element_pos_in_A = self.get_pos(A, B[i])
            while A_ind < b_element_pos_in_A:
                merged_array.append(A[A_ind])
                A_ind += 1
            merged_array.append(B[i])
        # There could be remaining elements in A. Add them to the merged array.
        merged_array.extend(A[A_ind:])
        return merged_array
        
    # Get the position of target if it were to be inserted into A. Here if there are ties, we require that target to be inserted after
    # all ties in A. This way it is consistent with the order of adding members of A before B in the for-loop of the parent function.
    def get_pos(self, A, target):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] <= target:
                left = mid
            else:
                right = mid        
        if A[left] > target:
            return left   
        if A[right] > target:
            return right     
        return right + 1
    
    
    
