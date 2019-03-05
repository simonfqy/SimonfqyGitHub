'''
Link: https://www.lintcode.com/problem/find-k-closest-elements/description
'''

# I wrote this solution based on the idea taught in Jiuzhang online course. Did not refer to their solution.
import math
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        output_list = []
        if k <= 0 or A is None or not len(A):
            return output_list
        ind_closest = self.get_closest_ind(A, target)
        output_list.append(A[ind_closest])
        left = ind_closest
        right = ind_closest
        
        while len(output_list) < k:
            left_value = math.inf
            right_value = math.inf
            if left > 0:
                left_value = A[left - 1]
            if right < len(A) - 1:
                right_value = A[right + 1]
            if abs(left_value - target) <= abs(right_value - target):
                # Choose the left pointer at this point.
                left -= 1
                output_list.append(left_value)
            else:
                right += 1
                output_list.append(right_value)
        return output_list
            

    def get_closest_ind(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            elif A[mid] == target:
                end = mid
                return mid
            if A[mid] > target:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        if abs(A[start] - target) <= abs(A[end] - target):
            return start
        else:
            return end
