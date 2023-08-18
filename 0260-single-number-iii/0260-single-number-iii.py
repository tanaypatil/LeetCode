class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        Xor1, Xor2, i = 0, 0, 0
        for n in nums:
            Xor1 ^= n
        for bit in range(32):
            if Xor1 & 1 << bit:
                i = bit
                break
        for n in nums:
            if n & 1 << i:
                Xor2 ^= n
        return [Xor1 ^ Xor2, Xor2]