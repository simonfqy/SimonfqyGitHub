'''
Link: https://www.lintcode.com/problem/next-permutation/description
'''

# Based on the teachings from Jiuzhang.com.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        ind_start_reversal = -1
        for i in range(len(nums) - 1, -1, -1):
            if i > 0 and nums[i] <= nums[i - 1]:
                continue
            ind_start_reversal = i
            break
        if ind_start_reversal == 0:
            self.reverse_list(nums, ind_start_reversal, len(nums) - 1)
            return nums
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[ind_start_reversal - 1]:
                nums[i], nums[ind_start_reversal - 1] = nums[ind_start_reversal - 1], nums[i]
                break
        self.reverse_list(nums, ind_start_reversal, len(nums) - 1)
        return nums
        
        
    def reverse_list(self, nums, start, end):
        left, right = start, end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
            
# My own solution, using recursion.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        return self.get_next_perm(nums, len(nums) - 1, False)

    def get_next_perm(self, nums, start_ind, local_maximum_found):        
        if local_maximum_found:
            next_larger = self.get_larger(nums, start_ind + 1, nums[start_ind])
            prefix_numbers = nums[:start_ind] + [next_larger]
            suffix_numbers = nums[start_ind:]
            suffix_numbers.remove(next_larger)
            return prefix_numbers + sorted(suffix_numbers)
        if start_ind == 0:
            # The list is already the maximum permutation that can be achieved. Start all over again and return the smallest permutation as the next.
            return sorted(nums)
        next_ind = start_ind - 1
        # Don't forget the "return" keyword should be added at the beginning of this statement.
        # Otherwise the function won't return anything.
        return self.get_next_perm(nums, next_ind, nums[start_ind] > nums[next_ind])

    def get_larger(self, nums, start, number):
        for n in sorted(nums[start:]):
            if n > number:
                return n            
