'''
Link: https://www.lintcode.com/problem/intersection-of-arrays/description
'''

# A straightforward Python solution by myself.
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        intersection_so_far = set()
        for i, arr in enumerate(arrs):
            if i == 0:
                intersection_so_far = set(arr)
                continue
            intersection_so_far.intersection_update(arr)
        return len(intersection_so_far)
    

'''
Based on the Java solution in jiuzhang.com using priority queues. Original explanation from jiuzhang:
基于 Priority Queue 的版本。
假设每个数组长度为 n, 一共 k 个数组。
时间复杂度为 O(knlogn + nklogk)
其中 knlogn是 k 个数组进行分别排序的时间复杂度
nklogk是 总共 nk 个数从 PriorityQueue 中进出，每次进出 logk。

相比使用 HashMap 的算法的时间复杂度 O(nk)这个方法并没有什么时间上的优势。
但是这个方法的空间复杂度很低，只有 O(k)，即多少个数组就花费多少的额外空间。

在面试中也是很有可能会被要求不用 HashMap 或者实现一个比 O(n)更低的空间复杂度的算法。因此这个程序的方法也是需要掌握的。
'''

import heapq
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        p_queue = []
        for i, arr in enumerate(arrs):
            if len(arr) == 0:
                return 0
            arr.sort()
            heapq.heappush(p_queue, (arr[0], (i, 0)))
            
        last_value, count, intersection = 0, 0, 0
        while p_queue:
            val, ind_tuple = heapq.heappop(p_queue)
            if count == 0 or val != last_value:
                if count == len(arrs):
                    intersection += 1
                last_value = val
                count = 1
            else:
                count += 1
                
            new_ind_tuple = (ind_tuple[0], ind_tuple[1] + 1)
            if new_ind_tuple[1] < len(arrs[new_ind_tuple[0]]):
                val = arrs[new_ind_tuple[0]][new_ind_tuple[1]]
                heapq.heappush(p_queue, (val, new_ind_tuple))
                
        if count == len(arrs):
            intersection += 1
        return intersection

    
# My own solution using heap. Very similar to the one above, but the code is neater.
import heapq
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        min_heap = []
        k = len(arrs)
        for i, arr in enumerate(arrs):
            if not arr:
                continue
            arr.sort()
            heapq.heappush(min_heap, (arr[0], i, 0))
        
        prev_val = float('inf')
        intersection_size = 0
        while min_heap:
            curr_val, arr_ind, ind_within_array = heapq.heappop(min_heap)
            if curr_val != prev_val:
                count_of_curr_val = 0
                prev_val = curr_val
            count_of_curr_val += 1
            if count_of_curr_val == k:
                intersection_size += 1
            ind_within_array += 1
            if len(arrs[arr_ind]) > ind_within_array:
                heapq.heappush(min_heap, (arrs[arr_ind][ind_within_array], arr_ind, ind_within_array))
        return intersection_size    
    
    
# My own solution using set.
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        set_1, set_2 = set(), set()
        for i, arr in enumerate(arrs):
            for element in arr:                
                if i > 0 and element not in set_1:
                    continue
                set_2.add(element)
            set_1, set_2 = set_2, set_1
            set_2.clear()
        return len(set_1)
    
    
# Answer from jiuzhang.com. Uses hash map.
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        count = {}
        # 记录每个数的出现次数
        for arr in arrs:
            for x in arr:
                if x not in count:
                    count[x] = 0
                count[x] += 1
        
        # 某个数出现次数等于数组个数，代表它在所有数组中都出现过
        result = 0
        for x in count.keys():
            if count[x] == len(arrs):
                result += 1
        return result
    
    
