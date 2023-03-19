'''
Link: https://www.lintcode.com/problem/1297/
'''

# Solution learned from https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-66994/gui-bing-p-1387f/.
# It uses merge sort.
class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def countSmaller(self, nums):
        n = len(nums)
        self.smaller_counts = [0] * n
        self.temp = [(0, 0) for _ in range(n)]
        num_pairs = [(nums[i], i) for i in range(n)]
        self.sort(num_pairs, 0, n - 1)
        return self.smaller_counts

    def sort(self, num_pairs, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.sort(num_pairs, start, mid)
        self.sort(num_pairs, mid + 1, end)
        self.merge(num_pairs, start, end)

    def merge(self, num_pairs, start, end):
        self.temp[start : end + 1] = num_pairs[start : end + 1]
        
        left_end = (start + end) // 2
        num_pairs_ind = start
        left_ind = start
        right_ind = left_end + 1

        while left_ind <= left_end and right_ind <= end:
            if self.temp[left_ind][0] <= self.temp[right_ind][0]:
                num_pairs[num_pairs_ind] = self.temp[left_ind]            
                original_ind = self.temp[left_ind][1]
                self.smaller_counts[original_ind] += right_ind - left_end - 1
                left_ind += 1
            else:
                num_pairs[num_pairs_ind] = self.temp[right_ind]
                right_ind += 1
            num_pairs_ind += 1

        while left_ind <= left_end:
            num_pairs[num_pairs_ind] = self.temp[left_ind]
            original_ind = self.temp[left_ind][1]
            self.smaller_counts[original_ind] += end - left_end
            left_ind += 1
            num_pairs_ind += 1

        while right_ind <= end:
            num_pairs[num_pairs_ind] = self.temp[right_ind]
            right_ind += 1
            num_pairs_ind += 1
            
            
