class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit += prices[r] - prices[l]
            l, r = r, r+1
        return profit