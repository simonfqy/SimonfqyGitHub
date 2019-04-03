'''
Link: https://www.lintcode.com/problem/sort-integers-ii/description
'''

# This is copied from the teachings of Jiuzhang.com. Other versions of quick sort do exist.
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        self.quick_sort(A, 0, len(A) - 1)
        
        
    def quick_sort(self, A, start, end):
        if start >= end:
            return
        pivot = A[(start + end) // 2]
        left, right = start, end
        
        # Here we need to have left <= right in this while block. Because if we do not,
        # we would cause overlapping portions in left and right sorted subarrays, and stackoverflow.
        while left <= right:
            # If an array is composed of the same values, then it would undergo O(n) swaps and result
            # in two sorted subarrays with similar size. The swapping seems to be unnecessary, but if
            # we avoid swapping by setting the conditions to be A[left] <= pivot and A[right] >= pivot,
            # it would result in left == right + 1, and right unchanged. Thus it would cause stack overflow
            # error. So we must set the conditions to be A[left] < pivot and A[right] > pivot, at the
            # expense of 'unnecessary' swaps.
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
                
        self.quick_sort(A, start, right)
        self.quick_sort(A, left, end)
        

# Also copied from the teachings of Jiuzhang.com. Uses merge sort.       
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        temp = [0] * len(A)
        # Pass the temp array as a parameter to avoid claiming new space in each invocation of merge_sort().
        self.merge_sort(A, 0, len(A) - 1, temp)
        
    
    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return
        left_end = (start + end) // 2
        self.merge_sort(A, start, left_end, temp)
        self.merge_sort(A, left_end + 1, end, temp)
        self.merge(A, start, end, temp)
        
    
    def merge(self, A, start, end, temp):
        left_end = (start + end) // 2
        temp_ind = start
        left_index = start
        right_index = left_end + 1
        
        while left_index <= left_end and right_index <= end:
            if A[left_index] <= A[right_index]:
                temp[temp_ind] = A[left_index]
                left_index += 1
            else:
                temp[temp_ind] = A[right_index]
                right_index += 1
            temp_ind += 1
            
        while left_index <= left_end:
            temp[temp_ind] = A[left_index]
            temp_ind += 1
            left_index += 1
            
        while right_index <= end:
            temp[temp_ind] = A[right_index]
            temp_ind += 1
            right_index += 1
            
        for i in range(start, end + 1):
            # Copy the values from temp array to the original array.
            A[i] = temp[i]
