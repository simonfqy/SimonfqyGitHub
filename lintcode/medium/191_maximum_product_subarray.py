'''
Link: https://www.lintcode.com/problem/191
'''

# My own solution. Took a VERY long time to come up with. Time complexity is O(n).
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        max_product = float('-inf')
        min_product = float('inf')
        # These numbers record the maximum and minimum products of subarrays ending at nums[right]. I only came to this clear realization
        # after finishing the code. Next time should try to clarify it earlier.
        candidate_max_product, candidate_min_product = 1, 1
        for right in range(len(nums)):
            new_num = nums[right]
            if new_num > 0:                
                if candidate_max_product > 0:
                    candidate_max_product *= new_num
                else:
                    candidate_max_product = new_num                           
                if candidate_min_product > 0:
                    candidate_min_product = new_num
                else:
                    candidate_min_product *= new_num               
                                
            elif new_num < 0:
                if candidate_max_product > 0:
                    candidate_max_product, candidate_min_product = candidate_min_product * new_num, candidate_max_product * new_num
                elif candidate_max_product < 0:
                    candidate_max_product, candidate_min_product = candidate_min_product * new_num, new_num
                else:
                    candidate_max_product, candidate_min_product = candidate_min_product * new_num, new_num
            else:
                candidate_max_product, candidate_min_product = 0, 0    
            min_product = min(min_product, candidate_min_product)
            max_product = max(max_product, candidate_max_product)             
                                                            
        return max_product
    

# A simplified version of the solution above. Much more succinct, also has O(n) time complexity.
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        max_product = float('-inf')
        # These numbers record the maximum and minimum products of subarrays ending at nums[right]. I only came to this clear realization
        # after finishing the code. Next time should try to clarify it earlier.
        candidate_max_product, candidate_min_product = 1, 1
        for right in range(len(nums)):
            new_num = nums[right]
            triplet = (candidate_max_product * new_num, candidate_min_product * new_num, new_num)
            candidate_min_product, candidate_max_product = min(triplet), max(triplet)
            max_product = max(max_product, candidate_max_product)             
                                                            
        return max_product

