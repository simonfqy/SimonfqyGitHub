'''
Link: https://www.lintcode.com/problem/150
'''

# My own solution. Has O(n) time complexity, traverses through the array once. It's a greedy algorithm: sell whenever
# the current price is higher than the local minimum prior to the current point (buying price), and (higher than the 
# price on the next day OR it is already the last day).
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        max_profit = 0
        min_price = None
        for i in range(n):
            if min_price is None:
                min_price = prices[i]
            curr_price = prices[i]
            if curr_price > min_price and (i == n - 1 or prices[i + 1] < curr_price):
                max_profit += curr_price - min_price
                min_price = None
            elif curr_price < min_price:
                min_price = curr_price
        return max_profit
      
      
# Solution from jiuzhang.com. Has O(n) time complexity, traverses through the array once. It's also greedy algorithm.
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        max_profit = 0
        for i in range(1, n):
            # You either sell at prices[i], or you don't sell at position i.
            max_profit += max(0, prices[i] - prices[i - 1])
        return max_profit
    
    
# My implementation of a solution from a student on jiuzhang.com. Has O(n) time complexity, similar to the solutions 
# above. Kinda uses dynamic programming.
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        max_profit = 0
        for i in range(1, n):
            # You either sell at prices[i], or you don't sell at position i.
            max_profit = max(max_profit, max_profit + prices[i] - prices[i - 1])
        return max_profit
    
    
