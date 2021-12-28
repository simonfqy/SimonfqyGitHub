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
