'''
Link: https://www.lintcode.com/problem/603/
'''


# My own solution. Has O(n^2) time complexity. Should be correct, but causes time limit exceeded exception.
class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        if n < 2:
            return []
        nums_list = sorted(list(nums))
        subsets_at_each_ind = [[set([nums_list[0]])]]        
        max_subset_size = 1
        max_subset = [nums_list[0]]
        for i in range(1, n):
            end_num = nums_list[i]
            subsets_at_curr_ind = []
            nums_we_should_not_visit = set()
            for j in range(i - 1, -1, -1):
                curr_num = nums_list[j]
                if curr_num > end_num // 2 or end_num % curr_num != 0:
                    continue
                if curr_num in nums_we_should_not_visit:
                    continue
                for subset in subsets_at_each_ind[j]:
                    updated_subset = subset | {end_num}
                    subsets_at_curr_ind.append(updated_subset)
                    if len(updated_subset) > max_subset_size:
                        max_subset_size = len(updated_subset)
                        max_subset = sorted(list(updated_subset))
                    nums_we_should_not_visit |= subset
            subsets_at_each_ind.append(subsets_at_curr_ind)          

        return max_subset

        
# My own implementation based on the instruction from jiuzhang.com. It is an optimization from the solution above, now we calculator factors of
# each number instead of going through each number smaller than nums_list[i]. This reduces the time complexity to O(n ^ 3/2). But among the solutions,
# this one is relatively slow and memory-intensive.
class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        if n < 2:
            return []
        nums_list = sorted(list(nums))
        subsets_after_each_num = {nums_list[0]: [set([nums_list[0]])]}        
        max_subset_size = 1
        max_subset = [nums_list[0]]
        for i in range(1, n):
            end_num = nums_list[i]
            subsets_after_curr_num = []
            nums_we_should_not_visit = set()
            factors = self.get_factors(end_num)
            for factor in factors:
                if factor not in subsets_after_each_num:
                    continue
                if factor in nums_we_should_not_visit:
                    continue
                for subset in subsets_after_each_num[factor]:
                    updated_subset = subset | {end_num}
                    subsets_after_curr_num.append(updated_subset)
                    if len(updated_subset) > max_subset_size:
                        max_subset_size = len(updated_subset)
                        max_subset = list(updated_subset)
                    nums_we_should_not_visit |= subset            
            subsets_after_each_num[end_num] = subsets_after_curr_num          

        return sorted(max_subset)

    def get_factors(self, num):
        sqrt = int(num ** 0.5)
        factors = []
        for i in range(1, sqrt + 1):
            if num % i != 0:
                continue
            factors.append(i)
            if num // i != i:
                factors.append(num // i)
        factors.sort(reverse=True)
        return factors
                

        
