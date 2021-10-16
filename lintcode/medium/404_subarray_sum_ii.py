'''
https://www.lintcode.com/problem/404
'''

# My own solution. Should be correct, but causes time limit exceeded exception.
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        prefix_sum = []
        curr_sum = 0
        count = 0
        for i, num in enumerate(A):
            curr_sum += num
            prefix_sum.append(curr_sum)
            count += start <= curr_sum <= end
            for starting_ind in range(1, i + 1):
                subarray_sum = prefix_sum[i] - prefix_sum[starting_ind - 1]
                count += start <= subarray_sum <= end
        return count
    
    
# An optimized version of the previous solution, but still causes time limit exceeded exception.
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        prefix_sum_list = []
        count = 0
        curr_sum = 0
        can_start_subarray_from_ind = [True] * len(A)
        for i, num in enumerate(A):
            curr_sum += num
            prefix_sum_list.append(curr_sum)

        for i in range(len(A)):
            if i == 0:
                prefix_sum = 0
            else:
                prefix_sum = prefix_sum_list[i - 1]
            subarray_sum = prefix_sum_list[-1] - prefix_sum
            if subarray_sum < start:
                for j in range(i, len(A)):
                    can_start_subarray_from_ind[j] = False
                break

        # Go through the list and check whether the subarray sum is too large. i should be the 
        # ending index.
        for i, prefix_sum in enumerate(prefix_sum_list):            
            # Start the subarray index from 0 to i. j is the starting index.
            for j in range(i, -1, -1):
                if not can_start_subarray_from_ind[j]:
                    continue
                if j == 0:
                    prev_sum = 0
                else:
                    prev_sum = prefix_sum_list[j - 1]
                past_subarray_sum = prefix_sum - prev_sum
                if past_subarray_sum > end:
                    # From now on, we cannot start from j or any earlier elements. Otherwise the subarray sum will be too large.
                    for k in range(j, -1, -1):
                        can_start_subarray_from_ind[k] = False
                    break
                if past_subarray_sum < start:
                    continue
                count += 1     
        return count              

                  
# This is an official solution from lintcode.com with O(n) time complexity, using two pointers. I actually came up with a very
# similar solution before referring to it, but my own solution was too complicated and had some nasty details which I cannot 
# fix correctly. My own solution was still constrained by the thinking of maintaining a list of prefix sum. We should think out of the box.
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        n = len(A)
        count = 0
        smaller_end, smaller_sum = 0, 0
        bigger_end, bigger_sum = 0, 0
        for start_ind in range(n):
            smaller_end = max(smaller_end, start_ind)
            bigger_end = max(bigger_end, start_ind)
            while smaller_end < n and smaller_sum + A[smaller_end] < start:
                smaller_sum += A[smaller_end]
                # Note that, after this increment, A[smaller_end] is not counted towards the smaller_sum.
                smaller_end += 1
            while bigger_end < n and bigger_sum + A[bigger_end] <= end:
                bigger_sum += A[bigger_end]
                bigger_end += 1
            if bigger_end > smaller_end:
                count += bigger_end - smaller_end
            if smaller_end > start_ind:
                smaller_sum -= A[start_ind]
            if bigger_end > start_ind:
                bigger_sum -= A[start_ind]
        
        return count                
    
                  
# Another official solution from lintcode.com. Uses binary search and has time complexity O(nlogn),
# not as good as the two pointer approach. Besides, it has lots of small details to take care of, which
# makes it error-prone.
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        n = len(A)
        count = 0
        presum = [0]
        for i in range(n):
            presum.append(A[i] + presum[i])
        for right in range(1, n + 1):
            if A[right - 1] > end or presum[right] < start:
                continue
            left_start = self.find_start_ind(presum, right, end)
            left_end = self.find_end_ind(presum, right, start)
            count += left_end - left_start + 1
        return count

    def find_start_ind(self, presum, right, end):
        start_ind, end_ind = 0, right - 1
        while start_ind + 1 < end_ind:
            mid_ind = (start_ind + end_ind) // 2
            if presum[right] - presum[mid_ind] <= end:
                end_ind = mid_ind
            else:
                start_ind = mid_ind
        if presum[right] - presum[start_ind] <= end:
            return start_ind
        return end_ind
    
    def find_end_ind(self, presum, right, start):
        start_ind, end_ind = 0, right - 1
        while start_ind + 1 < end_ind:
            mid_ind = (start_ind + end_ind) // 2
            if presum[right] - presum[mid_ind] > start:
                start_ind = mid_ind
            else:
                end_ind = mid_ind
        if presum[right] - presum[end_ind] >= start:
            return end_ind
        return start_ind      
            
