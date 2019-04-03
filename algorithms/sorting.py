'''
Related to:
https://github.com/simonfqy/SimonfqyGitHub/blob/c1ad34cfc44992d13c3f57c682915667268e4d4d/lintcode/easy/464_sort_integers_ii.py#L6
'''

def quick_sort(A, start, end):
    if start >= end:
        return
    left, right = start, end
    if left <= right:
        
