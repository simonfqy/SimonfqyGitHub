'''
Link: https://www.lintcode.com/problem/931/
'''

# My own solution. Used a heap, took a lot of time to execute (but still within time limit). Time complexity is O(k + n)logk, where n is the
# total number of elements, k is the total number of arrays.
import heapq
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        total_length = 0
        for num_list in nums:
            total_length += len(num_list)
        if total_length == 0:
            return 0
        is_odd = True
        largest_ind_needed = (total_length - 1) // 2
        if total_length % 2 == 0:
            is_odd = False
            largest_ind_needed += 1
        min_heap = []
        counter = 0
        first_mid, second_mid = None, None
        for i, num_list in enumerate(nums):
            if not num_list:
                continue
            heapq.heappush(min_heap, (num_list[0], i, 0))

        while counter <= largest_ind_needed:
            val, list_ind, ind_in_list = heapq.heappop(min_heap)
            if is_odd and counter == largest_ind_needed:
                return val
            if not is_odd:
                if counter == largest_ind_needed - 1:
                    first_mid = val
                elif counter == largest_ind_needed:
                    second_mid = val
                    return (first_mid + second_mid) / 2
            ind_in_list += 1
            if ind_in_list < len(nums[list_ind]):
                heapq.heappush(min_heap, (nums[list_ind][ind_in_list], list_ind, ind_in_list))
            counter += 1
            
           
# My own solution which uses top-down recursive list merging. Should be correct, but causes time limit exceeded problem.
import heapq
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        k = len(nums)
        total_length = 0
        for num_list in nums:
            total_length += len(num_list)
        if total_length == 0:
            return 0
        is_odd = True
        largest_ind_needed = (total_length - 1) // 2
        if total_length % 2 == 0:
            is_odd = False
            largest_ind_needed += 1
        merged_list = self.get_merged_list(0, k - 1, nums)
        if is_odd:
            median = merged_list[largest_ind_needed]
        else:
            median = (merged_list[largest_ind_needed - 1] + merged_list[largest_ind_needed]) / 2
        return median


    def get_merged_list(self, first, last, nums):
        if first == last:
            return nums[first]
        mid = (first + last) // 2
        left_list = self.get_merged_list(first, mid, nums)
        right_list = self.get_merged_list(mid + 1, last, nums)
        return self.merge_two_lists(left_list, right_list)

    def merge_two_lists(self, list_1, list_2):
        i = j = 0
        merged_list = []
        while i < len(list_1) and j < len(list_2):
            if list_1[i] <= list_2[j]:
                candidate = list_1[i]
                i += 1
            else:
                candidate = list_2[j]
                j += 1
            merged_list.append(candidate)
        if i < len(list_1):
            merged_list.extend(list_1[i:])
        if j < len(list_2):
            merged_list.extend(list_2[j:])
        return merged_list
    
