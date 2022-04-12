'''
Link: https://www.lintcode.com/problem/1310/
'''


# My own solution. Used prefix and suffix product array, does not use division. Has O(n) time complexity.
class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def product_except_self(self, nums: List[int]) -> List[int]:
        prefix_products, suffix_products = [1], [1]
        n = len(nums)
        front_product = 1
        rear_product = 1
        for i in range(1, n):
            front_product *= nums[i - 1]
            prefix_products.append(front_product)
            rear_product *= nums[n - i]
            suffix_products.append(rear_product)
        suffix_products.reverse()
        output = []
        for i in range(n):
            output.append(prefix_products[i] * suffix_products[i])
        return output
      
      
      
