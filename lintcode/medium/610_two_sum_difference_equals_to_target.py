'''
Link: https://www.lintcode.com/problem/two-sum-difference-equals-to-target/description
'''

# My own solution.
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        num_to_ind = dict()
        for i, num in enumerate(nums):
            if num - target in num_to_ind:
                return [num_to_ind[num - target] + 1, i + 1]
            if num + target in num_to_ind:
                return [num_to_ind[num + target] + 1, i + 1]
            num_to_ind[num] = i

            
# Almost copied from Jiuzhang.com. This solution uses double pointers and sorting.            
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        nums_tuple_list = [(num, ind) for ind, num in enumerate(nums)]
        n = len(nums)
        target = abs(target)
        # Notice the sorting here. It is required. Similar syntax can also be used in sorted().
        nums_tuple_list.sort(key = lambda x : x[0])
        j = 0
        for i in range(n):
            if i == j and i < n - 1:
                j += 1
            while j < n - 1 and nums_tuple_list[j][0] - nums_tuple_list[i][0] < target:
                j += 1
            if nums_tuple_list[j][0] - nums_tuple_list[i][0] == target:
                small, big = nums_tuple_list[i][1], nums_tuple_list[j][1]
                if small > big:
                    big, small = small, big
                return [small + 1, big + 1]
