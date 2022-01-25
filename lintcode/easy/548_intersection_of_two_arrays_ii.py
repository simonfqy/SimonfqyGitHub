'''
Link: https://www.lintcode.com/problem/548/
'''

# My own solution. Uses dictionary to store the occurrence of each element. Has O(n + m) time complexity, where n is the size of nums1, m is that of nums2.
from collections import defaultdict
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        nums1_element_to_freq, common_element_to_freq = defaultdict(int), dict()
        for num in nums1:
            nums1_element_to_freq[num] += 1
        for num in nums2:
            if nums1_element_to_freq[num] == 0:
                continue
            if num in common_element_to_freq and common_element_to_freq[num] == nums1_element_to_freq[num]:
                continue
            if num not in common_element_to_freq:
                common_element_to_freq[num] = 0
            common_element_to_freq[num] += 1
        result = []
        for num in common_element_to_freq:
            occurrence = common_element_to_freq[num]
            result += [num] * occurrence
        return result
      
      
