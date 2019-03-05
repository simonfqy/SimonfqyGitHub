'''
Link: https://www.lintcode.com/problem/first-bad-version/description
The implementation is based on the binary search template.
'''

#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        start = 1
        end = n
        
        while start + 1 < end:
            mid = (start + end) // 2
            if SVNRepo.isBadVersion(mid):
                # Go to those before it.
                end = mid
            else:
                start = mid
        
        if SVNRepo.isBadVersion(start):
            return start
        return end
