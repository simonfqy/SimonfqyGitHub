'''
https://www.lintcode.com/problem/1262
'''


# My own solution. Has O(n) time complexity, where n is the size of input array.
from typing import (
    List,
)

class Solution:
    """
    @param data: an array of integers
    @return: whether it is a valid utf-8 encoding
    """
    def valid_utf8(self, data: List[int]) -> bool:
        start = 0
        n = len(data)
        if n <= 0:
            return False
        while start < n:
            num = data[start]
            prefix_one_count = self.get_prefixing_ones_count(num)
            if prefix_one_count == 0:
                start += 1
                continue
            if prefix_one_count == 1:
                return False
            if prefix_one_count >= 5:
                return False
            for ind in range(start + 1, start + prefix_one_count):
                if data[ind] >> 6 != 0b10:
                    return False
            start += prefix_one_count
        return True

    
    def get_prefixing_ones_count(self, num):
        count = 0
        for i in range(7, 2, -1):
            if not num >> i & 1:
                return count
            count += 1
        return count
    

# Solution from jiuzhang.com. 
def check(nums, start, size):
    for i in range(start + 1, start + size + 1):
        if i >= len(nums) or (nums[i] >> 6) != 0b10:
            return False
    return True

class Solution(object):
    def validUtf8(self, nums, start=0):
        if not nums:
            return False
        while start < len(nums):
            first = nums[start]
            if (first >> 3) == 0b11110 and check(nums, start, 3):
                start += 4
            elif (first >> 4) == 0b1110  and check(nums, start, 2): 
                start += 3
            elif (first >> 5) == 0b110   and check(nums, start, 1): 
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True
    
    
