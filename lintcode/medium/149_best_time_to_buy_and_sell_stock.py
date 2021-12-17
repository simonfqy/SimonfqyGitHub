'''
Link: https://www.lintcode.com/problem/149
'''

# My own solution. Uses two pointers. Has O(n) time complexity.
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            curr_profit = price - min_price
            max_profit = max(max_profit, curr_profit)
            min_price = min(min_price, price)
        return max_profit
      
      
