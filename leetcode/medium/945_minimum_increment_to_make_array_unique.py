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
