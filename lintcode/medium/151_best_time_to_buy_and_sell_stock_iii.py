'''
Link: https://www.lintcode.com/problem/151
'''

# My own solution. Has O(n) time complexity. Traverses through the array twice.
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        max_profit = 0
        n = len(prices)
        left_max_profits = [0] * n
        right_max_profits = [0] * (n + 1)
        self.get_maximum_profit_arrays(prices, left_max_profits, right_max_profits)
        for i in range(n):            
            max_profit = max(max_profit, left_max_profits[i] + right_max_profits[i + 1])
        return max_profit
    
    def get_maximum_profit_arrays(self, prices_list, left_max_profits, right_max_profits):
        n = len(prices_list)        
        reverse_negative_prices_list = prices_list[::-1]
        reverse_negative_prices_list = [-a for a in reverse_negative_prices_list]        
        min_price = prices_list[0]
        max_profit = 0            
        for i in range(n):
            price = prices_list[i]
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            left_max_profits[i] = max_profit
        min_price = reverse_negative_prices_list[0]
        max_profit = 0
        for i in range(n):
            price = reverse_negative_prices_list[i]
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            right_max_profits[n - i - 1] = max_profit
        return 
    
      
# My own solution, refactored from the above solution by using helper functions to remove duplicate code.
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        max_profit = 0
        n = len(prices)
        left_max_profits = [0] * n
        right_max_profits = [0] * n
        self.populate_maximum_profit_arrays(prices, left_max_profits, right_max_profits)
        # Add a 0 to the end to satisfy the query of right_max_profits[n].
        right_max_profits.append(0)
        for i in range(n):            
            max_profit = max(max_profit, left_max_profits[i] + right_max_profits[i + 1])
        return max_profit
    
    def populate_maximum_profit_arrays(self, prices_list, left_max_profits, right_max_profits):
        n = len(prices_list)        
        reverse_negative_prices_list = prices_list[::-1]
        reverse_negative_prices_list = [-a for a in reverse_negative_prices_list]        
        self.populate_single_array(prices_list, left_max_profits)
        self.populate_single_array(reverse_negative_prices_list, right_max_profits)
        # We have to use right_max_profits.reverse() here, not right_max_profits = right_max_profits[::-1]. Only
        # calling the reverse() function can actually change the underlying list referenced from the scope of 
        # the parent function. 
        right_max_profits.reverse()
        return 

    def populate_single_array(self, prices_list, max_profit_array):
        min_price = prices_list[0]
        max_profit = 0
        for i in range(len(prices_list)):
            curr_price = prices_list[i]
            max_profit = max(max_profit, curr_price - min_price)
            min_price = min(min_price, curr_price)
            max_profit_array[i] = max_profit
            
            
# Solution from jiuzhang.com. It is a general solution for K transactions. The generic version can be found in
# https://github.com/simonfqy/SimonfqyGitHub/blob/37fb0f9f2f8ce2ac00c7ed452b4f134cb0cfedb2/lintcode/medium/393_best_time_to_buy_and_sell_stock_iv.py#L40
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        n = len(prices)
        K = 2
        # corner case
        if n == 0:
            return 0
        # main part
        dp = [[0] * n for _ in range(K + 1)]
        for i in range(1, K + 1):
            max_diff = float('-inf')
            for j in range(1, n):
                max_diff = max(max_diff, dp[i - 1][j - 1] - prices[j - 1])
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
        return dp[K][n - 1]            
            
            
# Solution from jiuzhang.com. Uses 4 variables which represent the net cash in the account. It is greedy algorithm.
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        # h stands for hold, s stands for sell. H and s represent the net cash in the account while holding and after
        # selling the stock, respectively.
        h1 = h2 = -max(prices)
        s1 = s2 = 0
        for price in prices:
            h1, s1, h2, s2 = max(h1, -price), max(s1, h1 + price), max(h2, s1 - price), max(s2, h2 + price)
        return s2    
    
