class Solution:
    def countSetBits(self, n):
        count = 0
        while n > 0:
            count+=n&1
            n >>= 1
            
        return count
    
    def minBitFlips(self, start: int, goal: int) -> int:
        return self.countSetBits(start^goal)