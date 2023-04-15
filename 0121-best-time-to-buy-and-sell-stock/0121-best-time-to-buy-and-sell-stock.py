class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = n-1
        max_profit = 0
        while i >= 0:
            j = i-1
            while j >= 0 and prices[j] < prices[i]:
                max_profit = max(max_profit, prices[i]-prices[j])
                j -= 1
            i = j
        return max_profit