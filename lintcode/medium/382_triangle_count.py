'''
Link: https://www.lintcode.com/problem/triangle-count/description
'''

# I did not come up with this solution.
class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        count = 0
        if not S or len(S) < 3:
            return count
        S.sort()
        for i in range(2, len(S)):
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    # This line is the key point. All elements between left and right pointers would be fine
                    # when combined with S[right] and S[left]. Thus right pointer can decrease without leaving
                    # unaccounted solutions.
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
