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
    
    
# My own solution which tries to use something similar to binary search. Kinda slow, but passed.
import heapq
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        k = len(nums)
        total_length = 0
        self.lengths = []
        for num_list in nums:
            self.lengths.append(len(num_list))
            total_length += len(num_list)
        if total_length == 0:
            return 0
        is_odd = True
        largest_ind_needed = (total_length - 1) // 2
        if total_length % 2 == 0:
            is_odd = False
            largest_ind_needed += 1
        inds = [0] * k
        if is_odd:
            return self.find_mth_element(nums, largest_ind_needed + 1, inds, list(self.lengths))
        else:
            first_num = self.find_mth_element(nums, largest_ind_needed, inds, list(self.lengths))
            remaining_element_counts = [length - ind for (length, ind) in zip(self.lengths, inds)]
            second_num = self.find_mth_element(nums, 1, inds, remaining_element_counts)
            return (first_num + second_num) / 2
        
    # m starts from 1.
    def find_mth_element(self, nums, m, inds, remaining_element_counts):
        non_empty_lists = [i for i, count in enumerate(remaining_element_counts) if count > 0]
        ki = len(non_empty_lists)  
        if ki == 1:            
            return nums[non_empty_lists[0]][m - 1]       
        if m < ki:
            return self.find_mth_element_without_binary_search(nums, m, inds, non_empty_lists)
        
        increment = m // ki
        min_candidate, ind_of_array = float('inf'), None        
        for i in non_empty_lists:
            if remaining_element_counts[i] < increment:
                continue
            if nums[i][inds[i] + increment - 1] < min_candidate:
                min_candidate = nums[i][inds[i] + increment - 1]
                ind_of_array = i           
                
        inds[ind_of_array] += increment
        remaining_element_counts[ind_of_array] -= increment
        m -= increment
        return self.find_mth_element(nums, m, inds, remaining_element_counts)
        
            
    def find_mth_element_without_binary_search(self, nums, m, inds, non_empty_lists):    
        min_heap = []
        counter = 1
        res = 0
        for array_ind in non_empty_lists:
            ind_within_array = inds[array_ind]                
            heapq.heappush(min_heap, (nums[array_ind][ind_within_array], array_ind, ind_within_array))
        while counter <= m:
            val, array_ind, ind_within_array = heapq.heappop(min_heap)
            if counter == m:
                res = val                
            ind_within_array += 1
            inds[array_ind] += 1
            if ind_within_array < self.lengths[array_ind]:
                heapq.heappush(min_heap, (nums[array_ind][ind_within_array], array_ind, ind_within_array))
            counter += 1
        return res          

        
# Solution from jiuzhang.com. Uses 2 levels of binary search: the 1st level is value-based binary search, starting with the range of elements.
# It finds the proper mth value. The second level is index-based binary search on each array in the nums in the input, which returns the number
# of elements smaller than or equal to val.
import heapq
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        total_length = sum([len(arr) for arr in nums])
        if total_length == 0:
            return 0
        if total_length % 2 == 1:
            return self.get_mth_element(nums, total_length // 2 + 1)
        else:
            return (self.get_mth_element(nums, total_length // 2) + self.get_mth_element(nums, total_length // 2 + 1)) / 2

    # m starts from 1.
    def get_mth_element(self, nums, m):
        start, end = self.get_range(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            # There could be multiple values of "mid" that satisfy self.get_total_smaller_or_equal_number(nums, mid) == m, we want to get the first
            # among them. Otherwise it may not be a number existing in nums.
            if self.get_total_smaller_or_equal_number(nums, mid) < m:
                start = mid
            else:
                end = mid
        if self.get_total_smaller_or_equal_number(nums, start) >= m:
            return start
        return end
    
    def get_range(self, nums):
        start = min([arr[0] for arr in nums if len(arr)])
        end = max([arr[-1] for arr in nums if len(arr)])
        return start, end
    
    def get_total_smaller_or_equal_number(self, nums, val):
        count = 0
        for arr in nums:
            if not arr:
                continue
            count += self.get_smaller_than_or_equal_count(arr, val)
        return count

    def get_smaller_than_or_equal_count(self, arr, val):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            # We can let this condition be arr[mid] < val and still pass all the tests. But it is more intuitive to use <=, since we
            # want to count all the elements that are smaller than or equal to val.
            if arr[mid] <= val:
                left = mid
            else:
                right = mid
        if arr[left] > val:
            return left
        if arr[right] > val:
            return right
        return right + 1

                
