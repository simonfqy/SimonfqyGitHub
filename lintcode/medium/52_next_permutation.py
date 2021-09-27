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
       
    
# Essentially the same solution as the one above. I wrote it after reading the solution above.
# The advantage compared to solutions below is that, this solution has O(n) time complexity, while the ones below
# involve sorting operations, hence O(nlogn) time complexity.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        ind_to_start_reverse = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                continue
            ind_to_start_reverse = i
            break
        if ind_to_start_reverse == 0:
            self.reverse_partial_list(nums, 0, len(nums) - 1)
        else:
            smaller_number = nums[ind_to_start_reverse - 1]
            for i in range(len(nums) - 1, ind_to_start_reverse - 1, -1):
                if nums[i] <= smaller_number:
                    continue
                nums[i], nums[ind_to_start_reverse - 1] = nums[ind_to_start_reverse - 1], nums[i]
                break
            self.reverse_partial_list(nums, ind_to_start_reverse, len(nums) - 1)
        return nums

    def reverse_partial_list(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
            
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
            
# Essentially this is the same solution as the previous one. But here we start from the beginning of the array, not the end.
# This solution is less succinct than the one above, we also need to handle the special case in the beginning.
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # we need to handle the case where nums is already the largest possible permutation.
        reverse_nums = sorted(nums)
        reverse_nums.reverse()
        if reverse_nums == nums:
            return sorted(reverse_nums)
        return self.get_next_perm(nums)

    def get_next_perm(self, numbers):
        if len(numbers) <= 1:
            return numbers
        suffix = numbers[1:]
        max_suffix_permutation = sorted(suffix)
        max_suffix_permutation.reverse()
        if max_suffix_permutation != suffix:
            return [numbers[0]] + self.get_next_perm(numbers[1:]) 
        # max suffix permutation equals to suffix. We need to change the numbers[0].
        larger_num = self.get_larger_num(numbers)
        numbers.remove(larger_num)
        return [larger_num] + sorted(numbers)
    
    def get_larger_num(self, numbers):
        first_num = numbers[0]
        for number in sorted(numbers):
            if number > first_num:
                return number
        return first_num
