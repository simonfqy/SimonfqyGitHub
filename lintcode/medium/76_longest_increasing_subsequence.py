'''
Link: https://www.lintcode.com/problem/76/
'''


# Solution from jiuzhang.com. DP, has O(n^2) time complexity.
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        n = len(nums)
        # dp[i] is the length of the LIS ending at nums[i].
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
                
        return max(dp)
   

# Instructed by jiuzhang.com, implemented by myself. It is basically the solution above, with the added functionality of printing the longest subsequence.
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0    
        n = len(nums)
        # dp[i] represents the length of LIS ending at nums[i]
        dp = [1] * n
        ind_to_prev_in_lis = [-1] * n
        longest = 1
        last = -1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    ind_to_prev_in_lis[i] = j
                    last = i
                    longest = max(longest, dp[i])
        path = []
        while last != -1:
            path.append(nums[last])
            last = ind_to_prev_in_lis[last]
        print(path[::-1])
        return longest

        
# Instructed by jiuzhang.com, implemented by myself. DP with binary search, has O(nlogn) time complexity.
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0    
        # Each element lis_len_to_smallest_ending_num[j] is the smallest ending number of any LIS with length j.
        # This array is monotonically increasing.
        # We can initialize it with float('-inf') only, no second element required.
        lis_len_to_smallest_ending_num = [float('-inf'), nums[0]]
        for i, num in enumerate(nums):
            # We need to find the last element in lis_len_to_smallest_ending_num array which is smaller than nums[i].
            last_smaller_element_ind = self.get_last_smaller_element_ind(lis_len_to_smallest_ending_num, num)
            ind_to_overwrite = last_smaller_element_ind + 1
            if len(lis_len_to_smallest_ending_num) == ind_to_overwrite:
                lis_len_to_smallest_ending_num.append(float('inf'))
            # Update the element after the last_smaller_element_ind in the array if nums[i] is smaller than it. 
            lis_len_to_smallest_ending_num[ind_to_overwrite] = min(lis_len_to_smallest_ending_num[ind_to_overwrite], num)            
        return len(lis_len_to_smallest_ending_num) - 1
    
    def get_last_smaller_element_ind(self, array, num):
        left, right = 0, len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] < num:
                left = mid
            else:
                right = mid
        if array[right] < num:
            return right
        if array[left] < num:
            return left
        return left - 1

    
