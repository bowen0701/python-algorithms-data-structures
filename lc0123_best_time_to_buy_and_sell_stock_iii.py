"""Leetcode 123. Best Time to Buy and Sell Stock III
Hard

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Say you have an array for which the ith element is the price of a given stock on
day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must
sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3),
             profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4),
             profit = 4-1 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), 
             profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later,
             as you are engaging multiple transactions at the same time.
             You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class SolutionIter(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not prices:
            return 0

        # Continue tracking min prices 1 & 2 and max profits 1 & 2.
        min_price1 = float('inf')
        min_price2 = float('inf')
        max_profit1 = 0
        max_profit2 = 0

        for i in range(len(prices)):
            cur_price = prices[i]

            # Track 1st buy and sell.
            min_price1 = min(cur_price, min_price1)
            max_profit1 = max(cur_price - min_price1, max_profit1)

            # Track 2nd buy and sell, with asset max_profit1.
            min_price2 = min(cur_price - max_profit1, min_price2)
            max_profit2 = max(cur_price - min_price2, max_profit2)

        return max_profit2


def main():
    # Output: 6
    prices = [3,3,5,0,0,3,1,4]
    print SolutionIter().maxProfit(prices)

    # Output: 4
    prices = [1,2,3,4,5]
    print SolutionIter().maxProfit(prices)

    # Output: 0
    prices = [7,6,4,3,1]
    print SolutionIter().maxProfit(prices)


if __name__ == '__main__':
    main()
