'''
Link: https://www.lintcode.com/problem/permutation-index/description
只需计算有多少个排列在当前排列A的前面即可。如何算呢?举个例子，[3,7,4,9,1]，在它前面的必然是某位置i对应元素比原数组小，
而i左侧和原数组一样。也即[3,7,4,1,X]，[3,7,1,X,X]，[3,1或4,X,X,X]，[1,X,X,X,X]。而第i个元素，比原数组小的情况有多少种，
其实就是A[i]右侧有多少元素比A[i]小，乘上A[i]右侧元素全排列数，即A[i]右侧元素数量的阶乘。i从右往左看，
比当前A[i]小的右侧元素数量分别为1,1,2,1，所以最终字典序在当前A之前的数量为1×1!+1×2!+2×3!+1×4!=39，故当前A的字典序为40。
'''

# Based on the algorithm given in Jiuzhang.com.
import math
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        index = 1
        index += self.get_count_earlier_arrays(A, 0)
        return index
        
    def get_count_earlier_arrays(self, A, start_index):
        if len(A) - start_index <= 1:
            return 0
        count = 0
        for number in A[start_index + 1:]:
            if number < A[start_index]:
                count += 1
        return count * math.factorial(len(A) - start_index - 1) + self.get_count_earlier_arrays(A, start_index + 1)

    
# Solution from Jiuzhang.com, uses iteration instead of recursion, and the calculation of factorial is much easier
# and economical.
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        result = 0
        permutation = 1
        for i in range(len(A) - 2, -1, -1):
            count_smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    count_smaller += 1
            permutation *= len(A) - i - 1
            result += permutation * count_smaller
        return result + 1
