'''
Link: https://www.lintcode.com/problem/4sum/description
'''

# My own solution. Uses 2 running indices and 2 pointers.
class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        results = []
        if len(numbers) < 4:
            return results
        numbers.sort()
        for i in range(len(numbers) - 3):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(len(numbers) - 1, 2, -1):
                if j < len(numbers) - 1 and numbers[j] == numbers[j + 1]:
                    continue
                left, right = i + 1, j - 1
                while left < right:
                    summ = numbers[i] + numbers[left] + numbers[right] + numbers[j]
                    if summ == target:
                        new_list = [numbers[i], numbers[left], numbers[right], numbers[j]]
                        results.append(new_list)
                        left += 1
                        right -= 1
                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1
                    elif summ < target:
                        left += 1
                    else:
                        right -= 1
        return results
