class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        smap = {}
        zeroes = 0
        for i, num in enumerate(nums):
            s += num
            if i > 0 and not s % k:
                return True
            if (s % k) in smap:
                if i-smap[s%k] >= 2: return True
            else: smap[s%k] = i
        return False
    
#         prefix_sum = 0
#         remainder_dict = {}

#         for i in range(len(nums)):

#             prefix_sum += nums[i]

#             if i >= 1 and prefix_sum % k == 0:
#                 return True

#             remainder = prefix_sum % k

#             if remainder in remainder_dict:
#                 if i - remainder_dict[remainder] >= 2:
#                     return True
                
#             else:
#                 remainder_dict[remainder] = i

        return False
                
        