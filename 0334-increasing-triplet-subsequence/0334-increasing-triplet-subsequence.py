class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        lis = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
                if len(lis) > 2:
                    return True
            else:
                lis[bisect_left(lis, nums[i])] = nums[i]
        return False
        