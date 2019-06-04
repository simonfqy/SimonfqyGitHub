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
        # mid_pos = int((target_num_order - 1) / 2)
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
        # statement was "B_mid_val is None or ... B_mid_val > A_mid_val"). I used to think that we to handle the third 
        # scenario in which B_mid_val == A_mid_val, but it would cause infinite loop.
        # Truncate both arrays.
        # new_target_order = target_num_order - (mid_pos + 1) * 2
        # return self.find_element_of_sorted_arrays(A, B, a_start + mid_pos + 1, b_start + mid_pos + 1, \
        #     new_target_order)
        
        
# The original version of the previous solution on jiuzhang.com.
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
        if count1 + count2 >= k:
            return left
        else:
            return right
    
    def helper(self, array, flag):
        if len(array) == 0:
            return 0
        left, right = 0 ,len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] <= flag:
                left = mid
            else:
                right = mid
        if array[right] <= flag:
            return right + 1
        if array[left] <= flag:
            return left + 1
        return 0
