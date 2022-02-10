'''
Link: https://www.lintcode.com/problem/1093
'''


# My own solution, uses DP. Has O(n^2) time complexity. 
class Solution:
    """
    @param nums: an array
    @return: the number of longest increasing subsequence
    """
    def findNumberOfLIS(self, nums):
        n = len(nums)
        length_and_count_of_LIS_ending_at_i = [(1, 1)] * n
        max_counter = 0
        max_LIS_len = 1
        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if length_and_count_of_LIS_ending_at_i[i][0] < length_and_count_of_LIS_ending_at_i[j][0] + 1:
                    length, count = length_and_count_of_LIS_ending_at_i[j]
                    length_and_count_of_LIS_ending_at_i[i] = (length + 1, count)
                    max_LIS_len = max(max_LIS_len, length + 1)
                elif length_and_count_of_LIS_ending_at_i[i][0] == length_and_count_of_LIS_ending_at_i[j][0] + 1:
                    curr_len, curr_count = length_and_count_of_LIS_ending_at_i[i]
                    _, component_count = length_and_count_of_LIS_ending_at_i[j]
                    length_and_count_of_LIS_ending_at_i[i] = (curr_len, curr_count + component_count)
        for i in range(n):
            if length_and_count_of_LIS_ending_at_i[i][0] == max_LIS_len:
                max_counter += length_and_count_of_LIS_ending_at_i[i][1]
                    
        return max_counter

