class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        S=set(nums)
        return (3*sum(S)-sum(nums))//2