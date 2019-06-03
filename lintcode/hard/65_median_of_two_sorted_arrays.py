'''
Link: https://www.lintcode.com/problem/median-of-two-sorted-arrays/description
'''

# My own solution, long and tedious, yet not correct. Has bugs.
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        if A is None or B is None:
            return None
        m, n = len(A), len(B)
        return self.find_element_of_sorted_arrays(A, B, 0, m - 1, 0, n - 1, \
            (m + n + 1) / 2)
            
    def find_element_of_sorted_arrays(self, A, B, a_start, a_end, b_start, b_end, target_num_order):
        if target_num_order == 1:
            return min(A[a_start], B[b_start])
        if target_num_order == a_end - a_start + b_end - b_start + 2:
            return max(A[a_end], B[b_end])
        if a_start > a_end:
            return self.get_designated_element(B, b_start, target_num_order)
        if b_start > b_end:
            return self.get_designated_element(A, a_start, target_num_order)
        
        a_mid = (a_start + a_end) // 2
        b_mid = (b_start + b_end) // 2
        if target_num_order <= a_mid + b_mid + 2:
            in_first_half = True
        else:
            in_first_half = False
        if A[a_mid] > B[b_mid]:
            if in_first_half:
                return self.find_element_of_sorted_arrays(A, B, a_start, a_mid, b_start, b_end, target_num_order)
            # not in first half. Remove the first half of B.
            num_to_remove = b_mid - b_start + 1
            new_target_order = target_num_order - num_to_remove
            return self.find_element_of_sorted_arrays(A, B, a_start, a_end, b_mid + 1, b_end, new_target_order)
        elif A[a_mid] < B[b_mid]:
            if in_first_half:
                # Remove the second half of B.
                return self.find_element_of_sorted_arrays(A, B, a_start, a_end, b_start, b_mid, target_num_order)
            # Remove the first half of A.
            num_to_remove = a_mid - a_start + 1
            new_target_order = target_num_order - num_to_remove
            return self.find_element_of_sorted_arrays(A, B, a_mid + 1, a_end, b_start, b_end, new_target_order)
        else:
            if in_first_half:
                # Remove the second half of both.
                return self.find_element_of_sorted_arrays(A, B, a_start, a_mid, b_start, b_mid, target_num_order)
            # Remove the first half of both.
            num_to_remove = a_mid + b_mid - a_start - b_start + 2
            new_target_order = target_num_order - num_to_remove
            return self.find_element_of_sorted_arrays(A, B, a_mid + 1, a_end, b_mid + 1, b_end, new_target_order)
            
        
            
    def get_designated_element(self, array, start, target_num_order):
        get_avg = False
        if target_num_order != int(target_num_order):
            # Need to get the average of adjacent values.
            get_avg = True
        if not get_avg:
            return array[start + target_num_order - 1]
        prev_ind = start + int(target_num_order) - 1
        avg_val = (array[prev_ind] + array[prev_ind + 1]) / 2
        return avg_val    
