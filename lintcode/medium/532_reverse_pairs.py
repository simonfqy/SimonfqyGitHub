'''
Link: https://www.lintcode.com/problem/532/
'''

# Solution based on https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-66994/gui-bing-p-1387f/.
# Uses merge sort. Very similar to 
# https://github.com/simonfqy/SimonfqyGitHub/blob/aef5ea95dea6adea04df8cf9cf4479349eaaff58/lintcode/hard/1297_count_of_smaller_numbers_after_self.py#L7.
class Solution:
    """
    @param a: an array
    @return: total of reverse pairs
    """
    def reverse_pairs(self, a: List[int]) -> int:
        n = len(a)
        self.temp = [0] * n
        self.count = 0
        self.sort(a, 0, n - 1)
        return self.count
    
    def sort(self, a, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.sort(a, start, mid)
        self.sort(a, mid + 1, end)
        self.merge(a, start, end)

    def merge(self, a, start, end):
        self.temp[start : end + 1] = a[start : end + 1]

        left_ind = start
        left_end = (start + end) // 2
        right_ind = left_end + 1
        merged_list_ind = start

        while left_ind <= left_end and right_ind <= end:
            if self.temp[left_ind] <= self.temp[right_ind]:
                a[merged_list_ind] = self.temp[left_ind]
                self.count += right_ind - left_end - 1
                left_ind += 1
            else:
                a[merged_list_ind] = self.temp[right_ind]
                right_ind += 1
            merged_list_ind += 1

        if left_ind <= left_end:
            self.count += (left_end - left_ind + 1) * (end - left_end)
            a[merged_list_ind : end + 1] = self.temp[left_ind : left_end + 1]

        if right_ind <= end:
            a[merged_list_ind : end + 1] = self.temp[right_ind : end + 1]
            
            
