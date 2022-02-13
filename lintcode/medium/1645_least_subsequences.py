'''
Link: https://www.lintcode.com/problem/1645
'''


# Solution from jiuzhang.com. Uses dynamic programming. Has O(n^2) time complexity.
class Solution:
    """
    @param arrayIn: The original array.
    @return: Count the minimum number of subarrays.
    """
    def LeastSubsequences(self, arrayIn):
        n = len(arrayIn)
        if n <= 1:
            return n
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if arrayIn[j] > arrayIn[i]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

                
# Solution from a student on jiuzhang.com. Uses binary search on a monotonically increasing array of tail elements of each descending subsequence.
# The number of tail elements in this array is the (least) number of decreasing subsequences. Directly uses the bisect library in Python. The bisect() function
# has this property: The returned insertion point i partitions the array a into two halves so that all(val <= x for val in a[lo : i]) for the left side 
# and all(val > x for val in a[i : hi]) for the right side.
import bisect
class Solution:
    
    def LeastSubsequences(self, nums):
        
        tails = []        
        for num in nums:
            i = bisect.bisect(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
        
        return len(tails)
                
