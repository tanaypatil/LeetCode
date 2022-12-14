class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = n-1
        profit = 0
        while i > 0:
            sell_price = prices[i]
            j = i-1
            last = sell_price
            while j >= 0 and prices[j] < last:
                last = prices[j]
                j -= 1
            profit += sell_price - last
            i = j
        return profit