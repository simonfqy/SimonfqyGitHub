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

    
# My own solution. Used binary search. Much more complicated than other methods, the time complexity also not good.
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        ind_in_nums2 = 0
        res = []
        for i, element in enumerate(nums1):
            candidate_ind_in_nums2 = self.get_ind_in_nums(element, nums2, ind_in_nums2, m - 1)
            if candidate_ind_in_nums2 < 0:
                continue
            if candidate_ind_in_nums2 == m:
                break
            res.append(element)
            ind_in_nums2 = candidate_ind_in_nums2 + 1
        return res

    def get_ind_in_nums(self, val, nums, left, right):        
        start, end = left, right
        if start > end:
            return -2
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= val:
                start = mid
            else:
                end = mid
        if nums[start] > val:
            return -1
        if nums[start] == val:
            return start
        if nums[end] == val:
            return end
        if nums[end] < val:
            return right + 1
        return -2
    
    
    
