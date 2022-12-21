class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        firstMajor = secondMajor = float('inf')
        firstSum = secondSum = 0
        
        res = []
        
        for num in nums:
            if num == firstMajor:
                firstSum += 1
            elif num == secondMajor:
                secondSum += 1
            elif firstSum == 0:
                firstSum = 1
                firstMajor = num
            elif secondSum == 0:
                secondSum = 1
                secondMajor = num
            else:
                firstSum -= 1
                secondSum -= 1
                
        fs = ss = 0
        
        for num in nums:
            if num == firstMajor:
                fs += 1
            if num == secondMajor:
                ss += 1
        n = len(nums)        
        if fs > n//3:
            res.append(firstMajor)
            
        if ss > n//3:
            res.append(secondMajor)
            
        return res