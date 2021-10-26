'''
Link: https://www.lintcode.com/problem/median-of-two-sorted-arrays/description
'''

# A straightforward solution similar to merge sort. Has O(n + m) time complexity, not optimal.
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        if A is None or B is None:
            return None
        m, n = len(A), len(B)
        # points to the element not yet visited
        self.a_pointer, self.b_pointer = 0, 0
        if (m + n) % 2 == 1:
            return self.find_kth_element(A, B, (m + n + 1) // 2)
        left = self.find_kth_element(A, B, (m + n) // 2)
        right = self.find_kth_element(A, B, (m + n) // 2 + 1)
        return (left + right) / 2
    
    def find_kth_element(self, A, B, target_order):
        
        while self.a_pointer < len(A) and self.b_pointer < len(B) and self.a_pointer + self.b_pointer < target_order - 1:
            if A[self.a_pointer] <= B[self.b_pointer]:
                self.a_pointer += 1
            else:
                self.b_pointer += 1
                
        if self.a_pointer >= len(A):
            self.b_pointer = target_order - self.a_pointer
            return B[self.b_pointer - 1]
        if self.b_pointer >= len(B):
            self.a_pointer = target_order - self.b_pointer
            return A[self.a_pointer - 1]
            
        if A[self.a_pointer] <= B[self.b_pointer]:
            self.a_pointer += 1
            return A[self.a_pointer - 1]
        else:
            self.b_pointer += 1
            return B[self.b_pointer - 1]
        

# My own solution, long and tedious, yet not correct. Has bugs.
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        if A is None or B is None:
            return None
        m, n = len(A), len(B)
        return self.find_element_of_sorted_arrays(A, B, 0, m - 1, 0, n - 1, \
            (m + n + 1) / 2)
            
    def find_element_of_sorted_arrays(self, A, B, a_start, a_end, b_start, b_end, target_num_order):
        if target_num_order == 1:
            return min(A[a_start], B[b_start])
        if target_num_order == a_end - a_start + b_end - b_start + 2:
            return max(A[a_end], B[b_end])
        if a_start > a_end:
            return self.get_designated_element(B, b_start, target_num_order)
        if b_start > b_end:
            return self.get_designated_element(A, a_start, target_num_order)
        
        a_mid = (a_start + a_end) // 2
        b_mid = (b_start + b_end) // 2
        if target_num_order <= a_mid + b_mid + 2:
            in_first_half = True
        else:
            in_first_half = False
        if A[a_mid] > B[b_mid]:
            if in_first_half:
                return self.find_element_of_sorted_arrays(A, B, a_start, a_mid, b_start, b_end, target_num_order)
            # not in first half. Remove the first half of B.
            num_to_remove = b_mid - b_start + 1
            new_target_order = target_num_order - num_to_remove
            return self.find_element_of_sorted_arrays(A, B, a_start, a_end, b_mid + 1, b_end, new_target_order)
        elif A[a_mid] < B[b_mid]:
            if in_first_half:
                # Remove the second half of B.
                return self.find_element_of_sorted_arrays(A, B, a_start, a_end, b_start, b_mid, target_num_order)
            # Remove the first half of A.
            num_to_remove = a_mid - a_start + 1
            new_target_order = target_num_order - num_to_remove
            return self.find_element_of_sorted_arrays(A, B, a_mid + 1, a_end, b_start, b_end, new_target_order)
        else:
            if in_first_half:
                # Remove the second half of both.
                return self.find_element_of_sorted_arrays(A, B, a_start, a_mid, b_start, b_mid, target_num_order)
            # Remove the first half of both.
            num_to_remove = a_mid + b_mid - a_start - b_start + 2
            new_target_order = target_num_order - num_to_remove
            return self.find_element_of_sorted_arrays(A, B, a_mid + 1, a_end, b_mid + 1, b_end, new_target_order)            
        
            
    def get_designated_element(self, array, start, target_num_order):
        get_avg = False
        if target_num_order != int(target_num_order):
            # Need to get the average of adjacent values.
            get_avg = True
        if not get_avg:
            return array[start + target_num_order - 1]
        prev_ind = start + int(target_num_order) - 1
        avg_val = (array[prev_ind] + array[prev_ind + 1]) / 2
        return avg_val    
    
    
# Learned from jiuzhang.com. 
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        if A is None or B is None:
            return None
        m, n = len(A), len(B)
        if (m + n) % 2 == 1:
            return self.find_element_of_sorted_arrays(A, B, 0, 0, (m + n - 1) // 2)
        left_val = self.find_element_of_sorted_arrays(A, B, 0, 0, (m + n) // 2 - 1)
        right_val = self.find_element_of_sorted_arrays(A, B, 0, 0, (m + n) // 2)
        return (left_val + right_val) / 2
        
            
    def find_element_of_sorted_arrays(self, A, B, a_start, b_start, target_num_order):
        if a_start >= len(A):
            return B[b_start + target_num_order]
        if b_start >= len(B):
            return A[a_start + target_num_order]
        if target_num_order == 0:
            return min(A[a_start], B[b_start])
        mid_pos = (target_num_order - 1) // 2
        A_mid_val, B_mid_val = None, None
        if mid_pos + a_start <= len(A) - 1:
            A_mid_val = A[mid_pos + a_start]
        if mid_pos + b_start <= len(B) - 1:
            B_mid_val = B[mid_pos + b_start]
        
        new_target_order = target_num_order - mid_pos - 1
        # it used to be only "<" instead of "<=", but it introduced problem as stated below.
        if A_mid_val is None or (A_mid_val is not None and B_mid_val is not None and B_mid_val <= A_mid_val):
            # truncate the B array.            
            return self.find_element_of_sorted_arrays(A, B, a_start, b_start + mid_pos + 1, new_target_order)        
        # Truncate the A array.
        return self.find_element_of_sorted_arrays(A, B, a_start + mid_pos + 1, b_start, new_target_order)
        # The code below introduces problem (originally the previous line was the body of an if-block, the if
        # statement was "B_mid_val is None or ... B_mid_val > A_mid_val"). I used to think that we should handle the third 
        # scenario in which B_mid_val == A_mid_val, but it would cause infinite loop.
        # Truncate both arrays.
        # new_target_order = target_num_order - (mid_pos + 1) * 2
        # return self.find_element_of_sorted_arrays(A, B, a_start + mid_pos + 1, b_start + mid_pos + 1, \
        #     new_target_order)
        
        
# The original version of the previous solution on jiuzhang.com. It converts the original problem of finding median into finding
# the kth element in A and B, then each step it approaches the kth element by k/2, halving k in each recursion.
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, 0, B, 0, n // 2 + 1)
        else:
            smaller = self.findKth(A, 0, B, 0, n // 2)
            bigger = self.findKth(A, 0, B, 0, n // 2 + 1)
            return (smaller + bigger) / 2

    def findKth(self, A, index_a, B, index_b, k):
        if len(A) == index_a:
            return B[index_b  + k - 1]
        if len(B) == index_b:
            return A[index_a + k - 1]
        if k == 1:
            return min(A[index_a], B[index_b])
        
        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else None
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else None
        
        if b is None or (a is not None and a < b):
            return self.findKth(A, index_a + k // 2, B, index_b, k - k // 2)
        return self.findKth(A, index_a, B, index_b + k // 2, k - k // 2)
    
    
# My implementation based on the solution above. Now k starts from 1 rather than 0.
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        first_ind = (m + n - 1) // 2
        first_num = self.find_kth_element(A, B, 0, 0, first_ind)
        if (m + n) % 2 == 1:
            return first_num
        second_num = self.find_kth_element(A, B, 0, 0, first_ind + 1)
        return (first_num + second_num) / 2
        
    def find_kth_element(self, A, B, A_start_ind, B_start_ind, k):
        if A_start_ind >= len(A):
            return B[B_start_ind + k]
        if B_start_ind >= len(B):
            return A[A_start_ind + k]
        if k == 0:
            return min(A[A_start_ind], B[B_start_ind])
        if k == 1:
            candidates = sorted(A[A_start_ind : A_start_ind + 2] + B[B_start_ind : B_start_ind + 2])
            return candidates[1]        
        if A_start_ind + k // 2 >= len(A):
            # The logic is more complicated than necessary. See the simplified version of the function below, where these
            # if-branches are simplified.
            if A[-1] <= B[B_start_ind + k // 2]:
                increment = len(A) - A_start_ind
                return self.find_kth_element(A, B, len(A), B_start_ind, k - increment)  
            return self.find_kth_element(A, B, A_start_ind, B_start_ind + k // 2, k - k // 2)              
        if B_start_ind + k // 2 >= len(B): 
            if B[-1] <= A[A_start_ind + k // 2]:
                increment = len(B) - B_start_ind
                return self.find_kth_element(A, B, A_start_ind, len(B), k - increment)
            return self.find_kth_element(A, B, A_start_ind + k // 2, B_start_ind, k - k // 2)

        if A[A_start_ind + k // 2] <= B[B_start_ind + k // 2]:
            return self.find_kth_element(A, B, A_start_ind + k // 2, B_start_ind, k - k // 2)        
        return self.find_kth_element(A, B, A_start_ind, B_start_ind + k // 2, k - k // 2)    
    
    # This is a slightly simplified version of the helper function.    
    def find_kth_element2(self, A, B, A_start_ind, B_start_ind, k):
        if A_start_ind >= len(A):
            return B[B_start_ind + k]
        if B_start_ind >= len(B):
            return A[A_start_ind + k]
        if k == 0:
            return min(A[A_start_ind], B[B_start_ind])
        if k == 1:
            candidates = sorted(A[A_start_ind : A_start_ind + 2] + B[B_start_ind : B_start_ind + 2])
            return candidates[1]        
        if A_start_ind + k // 2 >= len(A):
            # If A[-1] is very small, B[B_start_ind + k // 2] will be smaller than the kth number, so we can safely
            # increment the B index; if A[-1] is very large, B[B_start_ind + k // 2] will also be smaller than the kth number,
            # we can still safely increment B index. In both cases, the A index remains unchanged. The same applies to the 
            # scenario where B_start_ind + k // 2 >= len(B)
            return self.find_kth_element(A, B, A_start_ind, B_start_ind + k // 2, k - k // 2)              
        if B_start_ind + k // 2 >= len(B): 
            return self.find_kth_element(A, B, A_start_ind + k // 2, B_start_ind, k - k // 2)

        if A[A_start_ind + k // 2] <= B[B_start_ind + k // 2]:
            return self.find_kth_element(A, B, A_start_ind + k // 2, B_start_ind, k - k // 2)        
        return self.find_kth_element(A, B, A_start_ind, B_start_ind + k // 2, k - k // 2)
    
    
# A tricky solution.     
# 本参考程序来自九章算法，由 @李助教 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

# 二分答案的办法
'''
算法描述：
1. 我们需要先确定二分的上下界限，由于两个数组 A, B 均有序，所以下界为 min(A[0], B[0])，上界为 max(A[A.length - 1], B[B.length - 1]).
2. 判断当前上下界限下的 mid(mid = (start + end) / 2) 是否为我们需要的答案；这里我们可以分别对两个数组进行二分来找到两个数组中小于等于
   当前 mid 的数的个数 cnt1 与 cnt2，sum = cnt1 + cnt2 即为 A 跟 B 合并后小于等于当前mid的数的个数.
3. 如果 sum < k，即中位数肯定不是 mid，应该大于 mid，更新 start 为 mid，否则更新 end 为 mid，之后再重复第二步。
4. 当不满足 start + 1 < end 这个条件退出二分循环时，再分别判断一下 start 跟 end ，最终返回符合要求的那个数即可。

该算法使用了两层二分法，一层用于寻找第K个数，另一层用于在寻找第K个数的过程中，计算小于候选值的数字个数，其结果反馈回去，用于在第一层寻找第
K个数。
'''

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        len_a, len_b = len(A), len(B)
        if (len_a + len_b) % 2 == 1:
            return self.finf_kth(A, B, (len_a + len_b) // 2 + 1)
        else:
            left = self.finf_kth(A, B, (len_a + len_b) // 2 )
            right = self.finf_kth(A, B, (len_a + len_b) // 2 + 1)
            return (left + right) / 2
            
    def finf_kth(self, A, B, k):
        if len(A) == 0:
            left, right = B[0], B[-1]
        elif len(B) == 0:
            left, right = A[0], A[-1]
        else:
            left, right = min(A[0], B[0]), max(A[-1], B[-1])
        # The tricky part of this solution is that, left and right are not indices, but values.
        while left + 1 < right:
            mid = (left + right) // 2
            count1 = self.helper(A, mid)
            count2 = self.helper(B, mid)
            if count1 + count2 < k:
                left = mid
            else:
                right = mid
        count1 = self.helper(A, left)
        count2 = self.helper(B, left)
        # In the while loop, we usually have self.helper(A, left) + self.helper(B, left) < k, so if here we have
        # count1 + count2 >= k, that is unusual and we can be certain that "left" is the first value that has at least
        # k numbers no larger than it, that is, "left" is the kth value.
        if count1 + count2 >= k:
            return left
        else:
            # Similarly, in this case we are certain that "right" is the first values with k numbers no larger than it,
            # which means "right" is the kth value.
            return right
    
    # Returns the number of elements in the array no larger than flag.
    def helper(self, array, flag):
        if len(array) == 0:
            return 0
        left, right = 0, len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] <= flag:
                left = mid
            else:                
                right = mid
        # Because in the while loop, array[right] is always > flag, you would expect it to be > flag here as well.
        # If array[right] <= flag, it is guaranteed to be the rightmost element that is no larger than flag.
        if array[right] <= flag:
            return right + 1
        # Similar to the above. We are ensured that either array[right] or array[left] is the last element with value
        # no larger than flag.
        if array[left] <= flag:
            return left + 1
        # Haven't found any elements with value no larger than flag. It is an indication that all the values in the
        # array have values larger than the flag, hence return 0.
        return 0
    
    
# This is my own solution. Uses recursion with binary search. In the binary search, we can't simply calculate a midpoint: it 
# will result in errors. We should calculate a proportion, based on which we compute a cut-off point to narrow down the search range. 
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        is_even = (m + n) % 2 == 0
        first_ind = (m + n - 1)//2
        first_num = self.find_order_num(A, B, 0, m - 1, 0, n - 1, first_ind)
        if not is_even:
            return first_num
        else:
            second_num = self.find_order_num(A, B, 0, m - 1, 0, n - 1, first_ind + 1)
            return (first_num + second_num) / 2
    
    # We cannot simply calculate a_mid and b_mid indices. We need to calculate based on proportion.
    def find_order_num(self, A, B, a_start, a_end, b_start, b_end, order_num):        
        if a_end - a_start <= 1 and b_end - b_start <= 1:
            all_nums = sorted(A[a_start : a_end + 2] + B[b_start : b_end + 2])
            return all_nums[order_num]
        a_length = a_end - a_start + 1
        b_length = b_end - b_start + 1
        # Initially I used order_num + 1 as the numerator and it resulted in errors. We should make it
        # smaller as appropriate (similar to using (left + end) // 2 to assign value to mid). So remove the "+1" part.
        proportion = order_num / (a_length + b_length)
        a_next, b_next = int(a_start + proportion * a_length), int(b_start + proportion * b_length)
        if A[a_next] <= B[b_next]:
            updated_order_num = order_num - (a_next - a_start) 
            return self.find_order_num(A, B, a_next, a_end, b_start, b_next, updated_order_num)
        else:
            updated_order_num = order_num - (b_next - b_start) 
            return self.find_order_num(A, B, a_start, a_next, b_next, b_end, updated_order_num)
        
        
# The solution is from jiuzhang.com. It has the best time complexity: O(log(min(m, n))), however there are a painful amount of details to
# take care of the indices which makes this implementation very hard to debug.
# 解题思路
# 对于长度为m的数组A，我们把A划分成两个部分A1 = A[0, i-1]和A2 = A[i, m-1]。对于长度为n的数组B，将B划分成B1 = B[0, j-1]和B2 = B[j, n-1]，
# 使得len(A1) + len(B1) == len(A2) + len(B2)（记作条件1），那么当A划分后，B的划分位置就是确定的。
# 如果我们能够确定max(A1[:], B1[:]) <= min(A2[:], B2[:])（记作条件2），说明我们已经找到合适的划分，能够把{A, B}分成长度相等的两份，
# 且一份中的元素全部大于等于另一份。那么，中位数就为(max(A1[:], B1[:]) + min(A2[:], B2[:])) / 2。
# 怎么找到满足条件2的划分呢？选择较短的数组，假设长度为m，对它可能的划分位置有m + 1种。我们可以进行二分搜索，那么时间复杂度能够进一步优化到O(log(min(m, n)))。
# 算法流程
# 如果A长度大于B，两者交换一下，保证A是更短的。
# 对A进行二分，low和high初始化为0和m，每次循环不断缩小二分区间 对A的划分位置partition_x为区间中点low + (high - low) // 2，根据条件1计算出B的划分
# 位置partition_y。 我们在划分处的两端，可以得到四个值：A左部分的最大值max_left_x，A右部分的最小值min_right_x，B左部分的最大值max_left_y，B右部分的最小值min_right_y。
# 如果某个值不存在，对于这种边界情况，我们把最大值设为无穷小，最小值设为无穷大，保证后一步的比较恒成立。 
# 如果此刻的划分满足了条件2，用上述四值来翻译一下就是max_left_x <= min_right_y and max_left_y <= min_right_x:，那么我们就找到了中位数，
# 是max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2。 如果不满足，如果max_left_x > min_right_y，说明partition_x位置靠右了，
# 令high = partition_x - 1；反之，说明partition_x位置靠左了，令low = partition_x + 1。继续我们的循环。
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # if input1 length is greater than switch them so that input1 is smaller than input2
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        
        m, n = len(A), len(B)
        # Detail #1: high starts from m rather than m - 1
        low, high = 0, m
        
        # Detail #2: instead of the typical low + 1 < high condition, we are using low <= high
        while low <= high:
            partition_x = low + (high - low) // 2
            # Detail #3: need to + 1.
            partition_y = (m + n + 1)// 2 - partition_x
            
            # if partition_x is 0 it means nothing is there on left side. Use -INF for max_left_x
            if partition_x == 0:
                max_left_x = float('-inf')
            else:
                max_left_x = A[partition_x - 1]
            
            # if partition_x is length of input then there is nothing on right side. Use +INF for min_right_x
            if partition_x == m:
                min_right_x = float('inf')
            else:
                min_right_x = A[partition_x]
            
            if partition_y == 0:
                max_left_y = float('-inf')
            else:
                max_left_y = B[partition_y - 1]
            
            if partition_y == n:
                min_right_y = float('inf')
            else:
                min_right_y = B[partition_y]
            
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Now get max of left elements and min of right elements to get the median in case of even length combined array size
                if (m + n) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                # or get max of left for odd length combined array size.
                else:
                    return max(max_left_x, max_left_y)
            # we are too far on right side for partitionX. Go on left side. 
            elif max_left_x > min_right_y:
                # Detail #4 and #5: the high and lows are not partition_x. We need to +1 or -1.
                high = partition_x - 1
            # we are too far on left side for partitionX. Go on right side.
            else:
                low = partition_x + 1
        return 0
