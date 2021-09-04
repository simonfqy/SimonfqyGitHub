# Link: https://www.lintcode.com/problem/90/

# My own solution. Uses recursion.
class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        if k <= 0 or len(A) <= 0:
            return []
        combinations = []
        for i in range(len(A)):
            curr_val = A[i]
            if curr_val == target and k == 1:
                combinations.append([curr_val])
                break 
            possible_complements = self.kSumII(A[i + 1:], k - 1, target - curr_val)
            for complement in possible_complements:
                if complement:
                    combinations.append([curr_val] + complement)
        return combinations
    
    
# Another recursive solution from jiuzhang.com. Very similar to my solution above.
# It uses a semi-global variable "subsets" to contain all the satisfying results.
class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        subsets = []
        self.dfs(A, 0, k, target, [], subsets)
        return subsets

    def dfs(self, A, index, k, target, subset, subsets):
        if k == 0 and target == 0:
            subsets.append(subset)
            return
        if k == 0 or target <= 0:
            return
        for i in range(index, len(A)):
            curr_subset = subset + [A[i]]            
            self.dfs(A, i + 1, k - 1, target - A[i], curr_subset, subsets)
