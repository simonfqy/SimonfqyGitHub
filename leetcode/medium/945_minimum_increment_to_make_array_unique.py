"""Link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/solution/
   I came up with this solution, except that I didn't realize unplaced_elem could be implemented by a list instead of a dict. Only
   after reading the solution did I realize this, and now it is within the time limit.
   TAKEAWAY: use queue or stack (list or deque) wherever needed. Restrain the use of dictionary. 
"""
from collections import Counter
class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        element_set = set(A)
        element_counts = Counter(A)
        unplaced_elem = []
        current_elem = min(element_set)
        total_increment = 0
        while True:
            if len(element_set) == 0:
                break
            if current_elem in element_set:
                # Only deal with duplicate ones.
                if element_counts[current_elem] > 1:
                    unplaced_elem.extend([current_elem]*(element_counts[current_elem] - 1))
                else:
                    element_set.remove(current_elem)
            elif len(unplaced_elem) > 0:
                # Place it here.
                smallest_unplaced_elem = unplaced_elem.pop(0)
                total_increment += (current_elem - smallest_unplaced_elem) 
                if len(unplaced_elem) == 0 or unplaced_elem[0] != smallest_unplaced_elem:
                    # Already placed.
                    element_set.remove(smallest_unplaced_elem)                
            
            current_elem += 1
        
        return total_increment

      
"""Second solution:
   From the official solution. It uses sorting to make the array ordered and has some desirable properties. It then uses the number
   of inserted elements in the 'gaps' between elements in A to calculate the result. Interestingly, it only records the number of
   elements to find a place, stored in 'taken' and 'give' variables. Their values are reflected in the variable 'ans'.
   It is shorter and more efficient than the first solution."""      

 class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        A.append(100000)
        ans = taken = 0
        
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i-1] - 1)
                ans += A[i-1]*give + (give+1)*give/2
                taken -= give
        return int(ans)
