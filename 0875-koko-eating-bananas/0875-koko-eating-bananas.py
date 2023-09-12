class Solution: 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(m):
            return sum(math.ceil(pile / m) for pile in piles) <= h
        
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l)//2
            if possible(m):
                r = m
            else:
                l = m + 1
        return l
        
        