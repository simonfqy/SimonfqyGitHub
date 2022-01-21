'''
Link: https://www.lintcode.com/problem/363/
'''

# My implementation of the solution from jiuzhang.com. 每个位置上的盛水数目 = min(左侧最高，右侧最高) - 当前高度
# 从左到右扫描一边数组，获得每个位置往左这一段的最大值，及每个位置向右的最大值。 然后最后再扫描一次数组，计算每个位置上的盛水数目。
# 时间复杂度 O(n)，空间复杂度 O(n)
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        total_volume = 0
        n = len(heights)
        left_max, right_max = 0, 0
        left_max_list, right_max_list = [0] * n, [0] * n
        for i in range(n):
            left_max = max(left_max, heights[i])
            left_max_list[i] = left_max
            right_max = max(right_max, heights[n - 1 - i])
            right_max_list[n - 1 - i] = right_max

        for i in range(n):
            total_volume += min(left_max_list[i], right_max_list[i]) - heights[i]
        return total_volume
      
      
