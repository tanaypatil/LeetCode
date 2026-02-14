class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        firstMajor, firstCount = float('inf'), 0
        for num in nums:
            if firstMajor == num:
                firstCount += 1
            elif firstCount == 0:
                firstMajor = num
                firstCount = 1
            else:
                firstCount -= 1
        
        c = 0
        for num in nums:
            if num == firstMajor:
                c += 1
        return -1 if c < len(nums)//2 else firstMajor
        