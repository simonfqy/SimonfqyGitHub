'''
Link: https://www.lintcode.com/problem/3sum/description
'''

# My own solution. Uses a running index and two pointers.
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        output_list = []
        if not numbers or len(numbers) < 3:
            return output_list
        numbers.sort()
        i = 0
        while i < len(numbers) - 2:
            left, right = i + 1, len(numbers) - 1
            while left < right:
                if numbers[left] + numbers[right] + numbers[i] == 0:
                    new_list = [numbers[i], numbers[left], numbers[right]]
                    output_list.append(new_list)
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                    
                elif numbers[left] + numbers[right] + numbers[i] > 0:
                    right -= 1
                else:
                    left += 1
            i += 1
            while i < len(numbers) - 2 and numbers[i] == numbers[i - 1]:
                i += 1
                
        return output_list
