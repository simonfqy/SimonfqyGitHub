'''
Link: https://www.lintcode.com/problem/3sum-closest/description
'''

# My own solution.
import math
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 3:
            return None
        min_diff = math.inf
        numbers.sort()
        opt_summ = 0
        for i in range(len(numbers) - 2):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                summ = numbers[i] + numbers[left] + numbers[right]
                abs_diff = abs(target - summ)
                if abs_diff == 0:
                    return summ
                if abs_diff < min_diff:
                    opt_summ = summ
                    min_diff = abs_diff
                if summ > target:
                    right -= 1
                else:
                    left += 1
        return opt_summ
