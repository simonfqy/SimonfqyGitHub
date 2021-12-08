'''
Link: https://www.lintcode.com/problem/403
'''

# My own solution which does not work correctly. I was trying to reuse my solution for question 402, but this case is different and this solution
# is incorrect.
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        if not A:
            return [0, 0]
        presum_list = [0]
        presum = 0
        n = len(A)
        for i in range(2 * n):
            presum += A[i % n]
            presum_list.append(presum)
        min_sum = 0
        start, end = 0, 0
        candidate_start = 0
        max_subarray_sum = float('-inf')
        for i in range(1, 2 * n + 1):
            curr_subarray_sum = presum_list[i] - min_sum
            if curr_subarray_sum > max_subarray_sum:
                max_subarray_sum = curr_subarray_sum
                end = (i - 1) % n
                start = candidate_start

            if i <= n and min_sum > presum_list[i]:
                min_sum = presum_list[i]
                candidate_start = i % n
        return [start, end]    
    
                
# Another of my solution, incorrect. For this, I tried to copy the solution from jiuzhang.com for question 402, 
# also failed.
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        if not A:
            return [0, 0]
        n = len(A)
        max_subarray_sum_ending_in_curr_element = 0
        max_subarray_sum = float('-inf')
        start, end = 0, 0
        start_ind_of_curr_subarray = 0
        for i in range(2 * n):
            index = i % n
            if i < n: 
                if max_subarray_sum_ending_in_curr_element < 0:
                    max_subarray_sum_ending_in_curr_element = A[i]
                    start_ind_of_curr_subarray = i
                else:
                    max_subarray_sum_ending_in_curr_element += A[i]
            else:
                if start_ind_of_curr_subarray > index:
                    max_subarray_sum_ending_in_curr_element += A[index]
                else:
                    start_ind_of_curr_subarray = (index + 1) % n

            if max_subarray_sum_ending_in_curr_element > max_subarray_sum:
                max_subarray_sum = max_subarray_sum_ending_in_curr_element
                start = start_ind_of_curr_subarray
                end = index                

        return [start, end]    
    
        
# My own solution, using queue to maintain the minimum prefix sum. Similar to 
# https://github.com/simonfqy/SimonfqyGitHub/blob/c6a67e9fe0e746390396ee2db18f7bb809cefe32/lintcode/medium/621_maximum_subarray_v.py#L41.
# Has O(n) space and time complexities.
from collections import deque
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        if not A:
            return [0, 0]
        n = len(A)
        presum = 0
        presum_list = [0]
        for i in range(2 * n):
            presum += A[i % n]
            presum_list.append(presum)
        max_sum = float('-inf')
        # Each tuple: (index + 1, prefix sum)
        min_presum_queue = deque([(0, 0)])
        for i in range(1, 2 * n + 1):
            index = (i - 1) % n
            if i > n:
                # In this case, we have to make the start index greater than the end index.
                while min_presum_queue[0][0] <= index:
                    min_presum_queue.popleft()
            subarray_sum = presum_list[i] - min_presum_queue[0][1]
            if subarray_sum > max_sum:
                max_sum = subarray_sum
                start = min_presum_queue[0][0]
                end = index
            # Add the current prefix sum to the queue. For earlier prefix sums which are larger than the current one, they won't be needed
            # in calculating the largest subarray sum anymore, so we can safely pop them without problems. This is similar to the solution
            # of question 621.
            while min_presum_queue and min_presum_queue[-1][1] > presum_list[i]:
                min_presum_queue.pop()
            min_presum_queue.append((i, presum_list[i]))

        return [start, end]
    
    
# My own solution, slightly optimized from the one above. Now we no longer need to maintain a prefix sum list.
# The space and time complexities are still O(n).
from collections import deque
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        if not A:
            return [0, 0]
        n = len(A)
        presum = 0
        max_sum = float('-inf')
        # Each tuple: (index + 1, prefix sum)
        min_presum_queue = deque([(0, 0)])
        for i in range(2 * n):
            index = i % n
            presum += A[index]
            if i >= n:
                while min_presum_queue[0][0] <= index:
                    min_presum_queue.popleft()
            # The duplicate calculation will happen here if we don't have the "continue" statement when i >= n.
            subarray_sum = presum - min_presum_queue[0][1]
            if subarray_sum > max_sum:
                max_sum = subarray_sum
                start = min_presum_queue[0][0]
                end = index
            # If we don't have this if-statement, the result will still be correct, but that would result in
            # duplicate calculation and waste time.
            if i >= n:
                continue
            # Add the current prefix sum to the queue, when i < n.            
            while min_presum_queue and min_presum_queue[-1][1] > presum:
                min_presum_queue.pop()
            min_presum_queue.append((i + 1, presum))

        return [start, end]
    
    
# My implementation based on the instruction on jiuzhang.com. It has O(n) time complexity and O(1) space complexity.
# The time to execute is shorter than my own solution above.
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        if not A:
            return [0, 0]
        n = len(A)
        # Need to find the maximum sum continuous subarray and the minimum sum continuous subarray.
        max_subarray_sum = float('-inf')
        min_subarray_sum = float('inf')
        curr_max_subarray_sum = 0
        curr_min_subarray_sum = 0
        max_start, max_end = 0, 0
        min_start, min_end = 0, 0
        candidate_max_start, candidate_min_start = 0, 0
        total_sum = sum(A)
        for i, num in enumerate(A):
            if curr_max_subarray_sum < 0:
                curr_max_subarray_sum = num
                candidate_max_start = i
            else:
                curr_max_subarray_sum += num
            if curr_max_subarray_sum > max_subarray_sum:
                max_subarray_sum = curr_max_subarray_sum
                max_start = candidate_max_start
                max_end = i

            if curr_min_subarray_sum > 0:
                curr_min_subarray_sum = num
                candidate_min_start = i
            else:
                curr_min_subarray_sum += num
            if curr_min_subarray_sum < min_subarray_sum:
                min_subarray_sum = curr_min_subarray_sum
                min_start = candidate_min_start
                min_end = i
        # Handle the special case.
        if min_start == 0 and min_end == n - 1:
            return [max_start, max_end]
        wrapping_max_subarray_sum = total_sum - min_subarray_sum
        if max_subarray_sum >= wrapping_max_subarray_sum:
            return [max_start, max_end]
        # The wrapping_max_subarray_sum is actually larger.        
        return [min_end + 1, min_start - 1]
    
    
# A variant of the solution above. Now we use prefix sum to calculate. Like the above solution, this one also 
# has O(n) time complexity and O(1) space complexity. 
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        if not A:
            return [0, 0]
        n = len(A)
        # Need to find the maximum sum continuous subarray and the minimum sum continuous subarray.
        max_subarray_sum = float('-inf')
        min_subarray_sum = float('inf')
        curr_max_subarray_sum = 0
        curr_min_subarray_sum = 0
        max_start, max_end = 0, 0
        min_start, min_end = 0, 0
        min_prefix_sum, max_prefix_sum = 0, 0
        prefix_sum = 0
        candidate_max_start, candidate_min_start = 0, 0        
        for i, num in enumerate(A):
            prefix_sum += num
            curr_max_subarray_sum = prefix_sum - min_prefix_sum
            curr_min_subarray_sum = prefix_sum - max_prefix_sum
            if curr_max_subarray_sum > max_subarray_sum:
                max_subarray_sum = curr_max_subarray_sum
                max_start = candidate_max_start
                max_end = i
            if curr_min_subarray_sum < min_subarray_sum:
                min_subarray_sum = curr_min_subarray_sum
                min_start = candidate_min_start
                min_end = i
            if prefix_sum < min_prefix_sum:
                min_prefix_sum = prefix_sum
                candidate_max_start = i + 1
            if prefix_sum > max_prefix_sum:
                max_prefix_sum = prefix_sum
                candidate_min_start = i + 1            
        # Handle the special case.
        if min_start == 0 and min_end == n - 1:
            return [max_start, max_end]
        wrapping_max_subarray_sum = prefix_sum - min_subarray_sum
        if max_subarray_sum >= wrapping_max_subarray_sum:
            return [max_start, max_end]
        # The wrapping_max_subarray_sum is actually larger.        
        return [min_end + 1, min_start - 1]
    
    
