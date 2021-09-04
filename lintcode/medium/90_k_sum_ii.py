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
