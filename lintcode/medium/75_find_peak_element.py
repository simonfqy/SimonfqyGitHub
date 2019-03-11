'''
Link: https://www.lintcode.com/problem/find-peak-element/description
'''

# I wrote this solution by myself.
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid + 1] > A[mid]:
                start = mid
            else:
                end = mid
        if A[start] < A[end]:
            return end
        else:
            return start
            
# This is the solution provided by Jiuzhang.com.         
class Solution:
  #@param A: An integers list.
  #@return: return any of peek positions.
  def findPeak(self, A):
      # write your code here
      start, end = 1, len(A) - 2
      while start + 1 <  end:
          mid = (start + end) // 2
          if A[mid] < A[mid - 1]:
              end = mid
          elif A[mid] < A[mid + 1]:
              start = mid
          else:
              end = mid

      if A[start] < A[end]:
          return end
      else:
          return start
