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
