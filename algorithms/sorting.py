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
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right] < pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
            
    quick_sort(A, start, right)
    quick_sort(A, left, end)
