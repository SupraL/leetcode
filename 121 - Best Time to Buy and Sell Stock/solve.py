class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 10**4
        profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            profit = max(profit, p - min_price)
        return profit