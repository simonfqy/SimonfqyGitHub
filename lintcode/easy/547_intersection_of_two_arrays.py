'''
Link: https://www.lintcode.com/problem/547/
'''


# Used two pointers on sorted deduplicated lists.
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
      
      
# My own solution. Used set operations to extract common elements. Beats 100% of submissions in execution time.
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set & nums2_set)      

    
