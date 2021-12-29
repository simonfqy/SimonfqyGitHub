'''
Link: https://www.lintcode.com/problem/393
'''

# My implementation of the answer from jiuzhang.com. Has O(nk) time complexity, where n is the length of prices[] array. Uses dynamic programming. 
class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        n = len(prices)
        if not prices or n < 2:
            return 0
        # It is necessary to avoid time limit exceeded exception. 
        if K >= n // 2:
            max_profit = 0
            for i in range(1, n):
                max_profit += max(0, prices[i] - prices[i - 1])
            return max_profit
        dp = [[0] * n for _ in range(K + 1)]
        for transaction_count in range(1, K + 1):           
            max_diff = float('-inf')    
            for i in range(1, n):
                prev_profit = 0
                if i >= 2:
                    # Instead of using i - 1 in the answer, I used i - 2. It makes more sense though it doesn't change the end result.
                    prev_profit = dp[transaction_count - 1][i - 2]
                max_diff = max(max_diff, prev_profit - prices[i - 1])
                max_profit_containing_curr_price = prices[i] + max_diff  
                # It does not make perfect sense, though it works: consider an example where K = 3 and prices = [1, 3, 1, 4, 6, 2], then
                # dp[3][1] = 2. If we want to make the most sense, dp[3][1] should be 0.
                dp[transaction_count][i] = max(dp[transaction_count][i - 1], max_profit_containing_curr_price)             
            
        return dp[K][n - 1]
    
    
# Solution from jiuzhang.com. Has O(nk) time and space complexities.  
class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        n = len(prices)
        if n < 2 or K == 0:
            return 0
        # corner case: equal to infinite times of transaction
        if K >= n // 2:
            max_profit = 0
            for i in range(1, n):
                max_profit += max(0, prices[i] - prices[i - 1])
            return max_profit
        dp = [[0] * n for _ in range(K + 1)]
        for transaction_count in range(1, K + 1):           
            max_diff = float('-inf')    
            for i in range(1, n):
                # Maintaining a max_diff variable is actually an optimization from the prior version where the time complexity 
                # is O(kn^2). For each i, we want to calculate a value using dp[transaction_count - 1][t] + prices[i] - prices[t],
                # where t can be 0, 1, 2, ..., i - 1, we select the t which maximizes this expression. Using max_diff to record the
                # maximum value of dp[transaction_count - 1][i - 1] - prices[i - 1] as we traverse through i = 1 to n - 1 can save
                # time and avoid duplicate calculation.                 
                max_diff = max(max_diff, dp[transaction_count - 1][i - 1] - prices[i - 1])
                dp[transaction_count][i] = max(dp[transaction_count][i - 1], prices[i] + max_diff)             
            
        return dp[K][n - 1]
    
    
# Solution from a student on jiuzhang.com. Similar to 
# https://github.com/simonfqy/SimonfqyGitHub/blob/6d09fe4b1e5cd5beed9b14c14319edd79aa6b92b/lintcode/medium/151_best_time_to_buy_and_sell_stock_iii.py#L87.
# Uses dynamic programming focusing on the net cash in the account when the transactions happen.
class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        if len(prices) < 2 or K == 0:
            return 0
        if K >= len(prices) // 2:
            max_profit = 0
            for i in range(1, len(prices)):
                max_profit += max(0, prices[i] - prices[i - 1])
            return max_profit

        net_cash_while_holding = [-max(prices)] * K
        net_cash_after_selling = [0] * K
        for price in prices:
            for transaction_count in range(K):
                net_cash_while_holding[transaction_count] = max(net_cash_while_holding[transaction_count], 
                    net_cash_after_selling[transaction_count - 1] - price if transaction_count > 0 else -price)
                net_cash_after_selling[transaction_count] = max(net_cash_after_selling[transaction_count],
                    net_cash_while_holding[transaction_count] + price)
        return net_cash_after_selling[K - 1]
    
    
