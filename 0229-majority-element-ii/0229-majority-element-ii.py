class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        firstMajor = secondMajor = float('inf')
        firstCount = secondCount = 0
        n = len(nums)
        for num in nums:
            if num == firstMajor:
                firstCount += 1
            elif num == secondMajor:
                secondCount += 1
            elif firstCount == 0:
                firstMajor = num
                firstCount = 1
            elif secondCount == 0:
                secondMajor = num
                secondCount = 1
            else:
                firstCount -= 1
                secondCount -= 1
        
        firstCount = secondCount = 0
        for num in nums:
            if num == firstMajor:
                firstCount += 1
            elif num == secondMajor:
                secondCount += 1
        
        ret = []
        if firstCount > n//3:
            ret.append(firstMajor)
        if secondCount > n//3:
            ret.append(secondMajor)
        return ret
        