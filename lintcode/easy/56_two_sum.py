'''
Link: https://www.lintcode.com/problem/two-sum/description
'''

# My own solution, influenced by Jiuzhang.com. Uses two pointers.
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        num_to_ind_list = dict()
        for ind, num in enumerate(numbers):
            if num not in num_to_ind_list:
                num_to_ind_list[num] = []
            num_to_ind_list[num].append(ind)
        numbers.sort()
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                first, last = num_to_ind_list[numbers[left]][0], num_to_ind_list[numbers[right]][-1]
                if first > last:
                    first, last = last, first
                return [first, last]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

# Inspired by the solution given in Jiuzhang.com. Uses hashing and takes O(n) time.
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        num_to_ind_list = dict()
        for ind, num in enumerate(numbers):
            if target - num in num_to_ind_list:
                return [num_to_ind_list[target - num][0], ind]
            if num not in num_to_ind_list:
                num_to_ind_list[num] = []
            num_to_ind_list[num].append(ind)
