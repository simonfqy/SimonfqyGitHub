'''
Link: https://www.lintcode.com/problem/548/
'''

# My own solution. Uses dictionary to store the occurrence of each element. Has O(n + m) time complexity, where n is the size of nums1, m is that of nums2.
# Space complexity is also O(n + m).
from collections import defaultdict
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # Let nums1 be the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
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
      
      
# My own solution using two pointers, which involve sorting in the beginning. Time complexity is O(nlogn + mlogm), where n is the size
# of nums1, m is the size of nums2.
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i = j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i, j = i + 1, j + 1

        return result
    
    
    
