class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        j = len(prices)-1
        while j > 0:
            i = j-1
            while prices[i] <= prices[j] and i >= 0:
                mp = max(mp, prices[j]-prices[i])
                i -= 1
            # print(mp, i, j)
            j = i
        return mp