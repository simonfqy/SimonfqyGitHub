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
      
      
# Another solution from jiuzhang.com. 每个位置上的盛水数目 = min(左侧最高，右侧最高) - 当前高度
# It is an optimization of the solution above.
# 时间复杂度 O(n)，空间复杂度 O(1)
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        total_volume = 0
        n = len(heights)
        left_max, right_max = 0, 0
        left, right = 0, n - 1        
        while left <= right:
            # Right_max could become even larger as the right pointer moves leftward, but it is irrelevant: the water
            # volume only depends on the minimum, in this case, left_max. Similar for the else block.
            if left_max < right_max:
                left_max = max(left_max, heights[left])
                total_volume += left_max - heights[left]
                left += 1
            else:            
                right_max = max(right_max, heights[right])
                total_volume += right_max - heights[right]
                right -= 1
            
        return total_volume
    
    
# Solution from a student on jiuzhang.com. Maintains a stack of indices corresponding to monitonically decreasing height, which are basically candidate left banks.
# 时间复杂度 O(n)，空间复杂度 O(n). The advantage is that it does not require knowing the entire input list; data stream is fine.
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        total_volume = 0
        candidate_left_banks = []
        for i, height in enumerate(heights):
            while candidate_left_banks and height >= heights[candidate_left_banks[-1]]:
                ground = heights[candidate_left_banks.pop()]
                if not candidate_left_banks:
                    continue
                left_bank_ind = candidate_left_banks[-1]
                water_line = min(heights[left_bank_ind], height)
                total_volume += (water_line - ground) * (i - left_bank_ind - 1)
            candidate_left_banks.append(i)
            
        return total_volume
    
    
