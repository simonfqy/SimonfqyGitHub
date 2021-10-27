'''
Link: https://www.lintcode.com/problem/merge-k-sorted-arrays/description
'''

# Based on the hint given in jiuzhang.com. Time complexity is O(Nlogk), where N is the total number of integers,
# k is the number of arrays.
import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        answer = []
        list_of_candidates = []
        arr_ind_to_pointer = {}
        for i, arr in enumerate(arrays):
            if len(arr) <= 0:
                continue
            heapq.heappush(list_of_candidates, (arr[0], i))
            arr_ind_to_pointer[i] = 0
        while len(list_of_candidates) > 0:
            val, array_ind = heapq.heappop(list_of_candidates)
            answer.append(val)
            if arr_ind_to_pointer[array_ind] >= len(arrays[array_ind]) - 1:
                continue
            arr_ind_to_pointer[array_ind] += 1
            pointer_now_in_the_arr = arr_ind_to_pointer[array_ind]
            heapq.heappush(list_of_candidates, (arrays[array_ind][pointer_now_in_the_arr], \
                array_ind))
        return answer
    
    
# A recursive approach, top-down.
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        if arrays is None or len(arrays) <= 0:
            return []
        m = len(arrays)
        if m == 1:
            return arrays[0]
        left_array = self.mergekSortedArrays(arrays[: m//2])
        right_array = self.mergekSortedArrays(arrays[m//2:])
        return self.merge_two_sorted_arrays(left_array, right_array)
        
        
    def merge_two_sorted_arrays(self, array_1, array_2):
        if array_1 is None or len(array_1) <= 0:
            return array_2
        if array_2 is None or len(array_2) <= 0:
            return array_1
        pointer_1, pointer_2 = 0, 0
        answer = []
        while pointer_1 < len(array_1) and pointer_2 < len(array_2):
            if array_1[pointer_1] <= array_2[pointer_2]:
                answer.append(array_1[pointer_1])
                pointer_1 += 1
                continue
            answer.append(array_2[pointer_2])
            pointer_2 += 1
        
        while pointer_1 < len(array_1):
            answer.append(array_1[pointer_1])
            pointer_1 += 1
            
        while pointer_2 < len(array_2):
            answer.append(array_2[pointer_2])
            pointer_2 += 1
            
        return answer
    
    
# An iterative solution, bottom-up. Provided by jiuzhang.com. 
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        if arrays is None or len(arrays) <= 0:
            return []
        
        while len(arrays) > 1:            
            new_arrays = []
            for i in range(0, len(arrays), 2):
                if i + 1 <= len(arrays) - 1:
                    array = self.merge_two_sorted_arrays(arrays[i], arrays[i+1])
                else:
                    array = arrays[i]
                new_arrays.append(array)
            arrays = new_arrays
        return arrays[0]            
        
    # The following function is identical to the one in the previous solution, so the implementation
    # is omitted.
    def merge_two_sorted_arrays(self, array_1, array_2):
        pass
    
    
# My own solution. Should be correct, but hits time limit exceeded error.
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        starting_inds = [0] * len(arrays)
        traversed_all = False
        results = []
        while not traversed_all:
            traversed_all = True
            ind_of_array_with_smallest_element = 0
            smallest_element = float('inf')
            for i, array in enumerate(arrays):
                if starting_inds[i] >= len(array):
                    continue
                traversed_all = False
                if array[starting_inds[i]] < smallest_element:
                    ind_of_array_with_smallest_element = i
                    smallest_element = array[starting_inds[i]]
            if traversed_all:
                break
            results.append(smallest_element)
            starting_inds[ind_of_array_with_smallest_element] += 1
        return results
