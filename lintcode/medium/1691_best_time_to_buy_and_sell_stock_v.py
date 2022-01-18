'''
Link: https://www.lintcode.com/problem/1691
'''

# My own solution. Uses dynamic programming, has O(n^2) time complexity. Causes time limit exceeded exception.
class Solution:
    """
    @param a: the array a
    @return: return the maximum profit
    """
    def getAns(self, a):
        n = len(a)
        cash = [0] * (n // 2 + 1)
        prev_cash = list(cash)
        max_stock_count_after_today = 0
        # Have to use this
        prev_max_stock_count = 0
        for i in range(n):
            curr_price = a[i]            
            max_stock_count_after_today = min(i + 1, n - 1 - i)
            for j in range(max_stock_count_after_today + 1):
                if j == 0:
                    if i > 0:
                        # Either do nothing or sell 1 stock at current price.
                        cash[j] = max(prev_cash[j], prev_cash[j + 1] + curr_price)
                elif j == max_stock_count_after_today:
                    if prev_max_stock_count <= j:
                        # Buy 1 stock
                        cash[j] = prev_cash[j - 1] - curr_price
                    else:
                        # Either sell 1 stock or buy 1, or do nothing.
                        cash[j] = max(prev_cash[j], prev_cash[j + 1] + curr_price, prev_cash[j - 1] - curr_price)
                elif prev_max_stock_count > j:
                    cash[j] = max(prev_cash[j], prev_cash[j + 1] + curr_price, prev_cash[j - 1] - curr_price)
                else:
                    cash[j] = max(prev_cash[j], prev_cash[j - 1] - curr_price)         
            prev_max_stock_count = max_stock_count_after_today
            prev_cash = list(cash)              
            
        return cash[0]
