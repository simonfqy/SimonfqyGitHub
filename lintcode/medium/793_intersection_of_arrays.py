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
