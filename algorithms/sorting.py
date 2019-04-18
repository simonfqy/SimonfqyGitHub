'''
Related to:
https://github.com/simonfqy/SimonfqyGitHub/blob/c1ad34cfc44992d13c3f57c682915667268e4d4d/lintcode/easy/464_sort_integers_ii.py#L6
'''

def quick_sort(A, start, end):
    if start >= end:
        return
    left, right = start, end
    pivot = A[(start + end) // 2]
    while left <= right:
        # The A[left] < pivot and A[right] > pivot conditions in the following two if statements
        # cannot be changed to <= or >=.
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
            
    quick_sort(A, start, right)
    quick_sort(A, left, end)
    
   
def merge_sort(A, start, end, temp):
    # Note that both start and end are inclusive indices; temp is an array with same length
    # as A that is passed as a parameter, used to temporarily store the sorted subarray.
    if start >= end:
        return
    left_end = (start + end) // 2
    merge_sort(A, start, left_end, temp)
    merge_sort(A, left_end + 1, end, temp)
    merge(A, start, end, temp)
    
    
def merge(A, start, end, temp):
    left_end = (start + end) // 2
    temp_index = start
    right_index = left_end + 1
    left_index = start
    
    while left_index <= left_end and right_index <= end:
        if A[left_index] <= A[right_index]:
            temp[temp_index] = A[left_index]
            left_index += 1
        else:
            temp[temp_index] = A[right_index]
            right_index += 1
        temp_index += 1
        
    while left_index <= left_end:
        temp[temp_index] = A[left_index]
        temp_index += 1
        left_index += 1
        
    while right_index <= end:
        temp[temp_index] = A[right_index]
        temp_index += 1
        right_index += 1
    
    for i in range(start, end + 1):
        A[i] = temp[i]
    
    
    
    
    
    
    
    
    
    
    
